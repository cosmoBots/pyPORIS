"""Model serialization tests; no server, credentials or user models needed."""
import contextlib
import copy
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'PORIS'))
from PORIS import PORISDoc, PORISSys, PORISParam, PORISMode, PORISValueFloat, PORISValueString, PORISValue, PORISCmd
from poris_codegen import build_nodes_tree, createPythonCode
from poris_python2xml import load_model_class


class PorisYamlTest(unittest.TestCase):
    def fixture(self):
        doc = PORISDoc(42)
        root = PORISSys('Telescope')
        param = PORISParam('Elevation')
        mode = PORISMode('Pointing')
        numeric = PORISValueFloat('Position', -90.0, 0.0, 77.5)
        text = PORISValueString('Caption', 'Cúpula: #1')
        enum = PORISValue('Park')
        command = PORISCmd('Move')
        for item in (root, param, mode, numeric, text, enum, command):
            doc.addItem(item)
        doc.setRoot(root)
        root.addParam(param)
        param.addMode(mode)
        for value in (numeric, text, enum):
            param.addValue(value)
            mode.addValue(value)
        command.setParent(root)
        return doc, numeric

    def test_definition_and_references(self):
        doc, numeric = self.fixture()
        numeric.setData(40)
        data = yaml.safe_load(doc.toYAML())
        rows = {row['subject']: row for row in data['items'].values()}
        self.assertEqual(data['format'], 'cosmosys-model')
        self.assertEqual(len(rows), 7)
        self.assertNotIn('UNKNOWN', rows)
        self.assertNotIn('Engineering', rows)
        self.assertEqual(rows['Position']['fields'], {'value_kind': 'float', 'min': -90.0, 'default': 0.0, 'max': 77.5})
        self.assertEqual(rows['Caption']['fields']['default_text'], 'Cúpula: #1')
        self.assertEqual(rows['Park']['fields']['value_kind'], 'enum')
        self.assertEqual(rows['Move']['type'], 'command')
        self.assertEqual(len(data['relations']), 3)
        for row in data['items'].values():
            self.assertNotIn('csid', row)
            if 'parent' in row:
                self.assertIn(row['parent'], data['items'])
        for relation in data['relations']:
            self.assertIn(relation['from'], data['items'])
            self.assertIn(relation['to'], data['items'])
            self.assertEqual(relation['type'], 'precedes')
        self.assertEqual(doc.toYAML(), doc.toYAML())

    def test_invalid_range_rejected(self):
        doc, numeric = self.fixture()
        numeric.setDefaultData(float('nan'))
        with self.assertRaisesRegex(ValueError, 'Invalid numeric range'):
            doc.toYAML()

    def test_generated_engineering_is_opt_in_in_both_formats(self):
        nodes = {}
        for key, name, tracker, parent, blocking in [
            ('root', 'Instrument', 'prSys', None, []),
            ('operation', 'Operation', 'prMode', 'root', ['user_eng']),
            ('param', 'Position', 'prParam', 'root', []),
            ('user_eng', 'Engineering', 'prMode', 'param', ['value']),
            ('value', 'Park', 'prValue', 'param', [])
        ]:
            nodes[key] = dict(ident=key, id=key, subject=name, tracker=tracker,
                              parent=parent, blocking=blocking, precedents=[],
                              children=[], virtual=False, description='', min='',
                              default_data='', max='', deftext='')
        for enabled in [False, True]:
            with self.subTest(eng=enabled), tempfile.TemporaryDirectory() as directory:
                tree = build_nodes_tree(copy.deepcopy(nodes), include_engineering=enabled)
                createPythonCode(tree, 'Generated', directory, '')
                doc = load_model_class(Path(directory) / 'GeneratedPORIS.py', None)(0)
                xml = doc.toXML()
                definitions = [node for node in xml.documentElement.childNodes if node.nodeType == node.ELEMENT_NODE]
                identifiers = [node.getElementsByTagName('ident')[0].firstChild.nodeValue for node in definitions]
                self.assertEqual(any(value.startswith('ENG') for value in identifiers), enabled)
                data = yaml.safe_load(doc.toYAML())
                engineering = [row for row in data['items'].values() if row['subject'] == 'Engineering']
                self.assertEqual(len(engineering), 2 if enabled else 1)
                # A user-declared mode named Engineering always survives.
                self.assertIn('user_eng', identifiers)
                self.assertEqual(len(data['items']), len(definitions))
                ids = {node.getElementsByTagName('id')[0].firstChild.nodeValue for node in definitions}
                for node in definitions:
                    for destination in node.getElementsByTagName('destination'):
                        self.assertIn(destination.getElementsByTagName('id')[0].firstChild.nodeValue, ids)

    def test_explicit_system_engineering_is_not_replaced(self):
        nodes = {}
        for key, name, kind, parent in [
            ('root', 'Instrument', 'prSys', None),
            ('param', 'Position', 'prParam', 'root'),
            ('engineering', 'Engineering', 'prMode', 'root'),
            ('mode', 'Normal', 'prMode', 'param')
        ]:
            nodes[key] = dict(ident=key, subject=name, tracker=kind, parent=parent,
                              blocking=[], children=[], virtual=False)
        tree = build_nodes_tree(nodes, include_engineering=True)
        self.assertEqual(set(tree), {'root', 'param', 'engineering', 'mode'})
        self.assertEqual(tree['engineering']['blocking'], [])

    def test_cli_always_writes_both_formats(self):
        with tempfile.TemporaryDirectory() as directory:
            model = Path(directory) / 'DemoPORIS.py'
            model.write_text('from PORIS import *\nclass DemoPORIS(PORISDoc):\n'
                             ' def __init__(self, project_id):\n'
                             '  super().__init__(project_id)\n'
                             '  root = PORISSys("Demo")\n'
                             '  root.ident = "demo"\n'
                             '  self.addItem(root)\n  self.setRoot(root)\n')
            output = Path(directory) / 'demo.xml'
            result = subprocess.run([sys.executable, str(Path(__file__).with_name('poris_python2xml.py').resolve()), str(model), '-o', str(output)], capture_output=True, text=True, cwd=directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(b'<poris', output.read_bytes())
            poris_file = Path(directory) / 'output/poris/demo.poris'
            self.assertEqual(yaml.safe_load(poris_file.read_text())['project_profile'], 'poris')
            self.assertFalse(output.with_suffix('.poris').exists())


if __name__ == '__main__':
    with contextlib.redirect_stdout(io.StringIO()):
        unittest.main()
