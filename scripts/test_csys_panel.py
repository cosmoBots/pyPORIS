import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from csys_config import load_instance
from csys_panel import download_model, resolve_url, order_model_xml


class CsysPanelTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.config = Path(self.temp.name) / 'csys.yaml'
        self.config.write_text('local:\n  url: http://localhost:3001\n  key: test-key\n  ignorecert: false\n')
        self.instance = load_instance('local', self.config)

    def test_urls_and_scope(self):
        _, project, item, scope = resolve_url('http://localhost:3001/projects/osiris/poris?issue_id=22&scope=node_down', self.config)
        self.assertEqual((project, item, scope), ('osiris', '22', 'node_down'))
        self.assertEqual(resolve_url('http://localhost:3001/issues/22#poris', self.config)[1:], (None, '22', None))
        with self.assertRaises(ValueError):
            resolve_url('https://different.example/projects/osiris', self.config)
        with self.assertRaises(ValueError):
            load_instance('missing', self.config)

    @patch('csys_panel.requests.Session')
    def test_web_preserves_original_bytes(self, factory):
        session = factory.return_value.__enter__.return_value
        xml = b'<poris><sub-system><id>1</id><type>PORISNode</type></sub-system><mode><id>2</id><type>PORISMode</type></mode></poris>'
        session.get.return_value = Mock(status_code=200, content=xml)
        with patch('csys_panel.order_model_xml', side_effect=AssertionError('Must not reorder')):
            self.assertEqual(download_model(self.instance, 'osiris', java_order=False), xml)

    def test_java_dependency_order(self):
        from defusedxml import ElementTree as ET
        xml = b'<poris><sub-system><id>1</id><type>PORISNode</type><destinations><destination><id>2</id></destination></destinations></sub-system><mode><id>2</id><type>PORISMode</type></mode></poris>'
        root = ET.fromstring(order_model_xml(xml))
        self.assertEqual([item.findtext('id') for item in root], ['2', '1'])
        with self.assertRaises(ValueError):
            order_model_xml(xml.replace(b'<destination><id>2', b'<destination><id>99'))

    @patch('csys_panel.requests.Session')
    def test_csid_resolves_own_project(self, factory):
        session = factory.return_value.__enter__.return_value
        session.headers = {}
        identity = Mock(status_code=200)
        identity.json.return_value = {'item': {'id': 22, 'project': {'identifier': 'subsystem'}}}
        xml = Mock(status_code=200, content=b'<poris><sub-system><id>1</id><type>PORISNode</type></sub-system></poris>')
        session.get.side_effect = [identity, xml]
        self.assertEqual(download_model(self.instance, 'osiris', 'OSIRIS-0006', 'node_down'), order_model_xml(xml.content))
        self.assertEqual(session.headers['X-Redmine-API-Key'], 'test-key')
        self.assertTrue(session.verify)
        self.assertEqual(session.get.call_args.args[0], 'http://localhost:3001/projects/subsystem/poris/model.xml')
        self.assertEqual(session.get.call_args.kwargs['params'], {'scope': 'node_down', 'issue_id': 22})
        self.assertFalse(session.get.call_args.kwargs['allow_redirects'])

    @patch('csys_panel.requests.Session')
    def test_issue_url_resolution(self, factory):
        session = factory.return_value.__enter__.return_value
        identity = Mock(status_code=200)
        identity.json.return_value = {'issue': {'id': 22, 'project': {'id': 7}}}
        session.get.side_effect = [identity, Mock(status_code=200, content=b'<poris><sub-system><id>1</id><type>PORISNode</type></sub-system></poris>')]
        download_model(self.instance, None, '22')
        self.assertEqual(session.get.call_args.args[0], 'http://localhost:3001/projects/7/poris/model.xml')
        self.assertEqual(session.get.call_args.kwargs['params']['scope'], 'node_down')

    @patch('csys_panel.requests.Session')
    def test_rejects_login_redirects_and_non_poris(self, factory):
        session = factory.return_value.__enter__.return_value
        for response in [Mock(status_code=302), Mock(status_code=401), Mock(status_code=200, content=b'<html/>')]:
            session.get.return_value = response
            with self.assertRaises(ValueError):
                download_model(self.instance, 'osiris')
        with self.assertRaises(ValueError):
            download_model(self.instance, 'osiris', scope='node')


if __name__ == '__main__':
    unittest.main()
