"""Download a cosmoSys PORIS model and launch the existing XML viewer."""
import argparse
from pathlib import Path
import subprocess
import sys
import tempfile
from urllib.parse import quote, urlsplit, parse_qs, unquote

import requests
from defusedxml import ElementTree
from defusedxml.common import DefusedXmlException
from csys_config import load_instance, load_instances


def get(session, url, params=None):
    response = session.get(url, params=params, timeout=30, allow_redirects=False)
    if response.status_code != 200:
        raise ValueError(f'cosmoSys returned HTTP {response.status_code}; check URL, API key and permissions')
    return response


def resolve_url(url, config=None):
    parts = urlsplit(url)
    if parts.username or parts.password:
        raise ValueError('URLs must not contain credentials')
    matches = []
    for name in load_instances(config):
        instance = load_instance(name, config)
        base = urlsplit(instance['url'])
        prefix = base.path.rstrip('/')
        if (parts.scheme, parts.netloc) == (base.scheme, base.netloc) and parts.path.startswith(prefix + '/'):
            matches.append((len(prefix), instance, parts.path[len(prefix):]))
    if not matches:
        raise ValueError('No configured instance matches this URL; add it to csys.yaml')
    matches.sort(key=lambda match: match[0], reverse=True)
    if len(matches) > 1 and matches[0][0] == matches[1][0]:
        raise ValueError('Several instances match this URL; use instance-name arguments')
    _, instance, path = matches[0]
    segments = path.strip('/').split('/')
    query = parse_qs(parts.query)
    scope = query.get('scope', [None])[0]
    if scope not in (None, 'node', 'project', 'node_down'):
        raise ValueError('Invalid scope in URL')
    if len(segments) == 2 and segments[0] == 'issues' and segments[1].isdecimal():
        return instance, None, segments[1], scope
    if len(segments) >= 2 and segments[0] == 'projects' and segments[2:] in ([], ['poris'], ['poris', 'model.xml'], ['poris', 'model']):
        return instance, unquote(segments[1]), query.get('issue_id', [None])[0], scope
    raise ValueError('Expected a project, PORIS viewer or /issues/<id> URL')


def order_model_xml(xml):
    """Java loads destinations in one pass and takes the last item as root."""
    root = ElementTree.fromstring(xml)
    if root.tag != 'poris':
        raise ValueError('The server did not return a PORIS XML model')
    items = {}
    for item in root:
        identifier = item.findtext('id')
        if not identifier or identifier in items:
            raise ValueError('PORIS XML contains missing or duplicate item IDs')
        items[identifier] = item
    dependencies = {
        key: [ref.text for ref in item.findall('./destinations/destination/id')]
        for key, item in items.items()
    }
    referenced = {key for refs in dependencies.values() for key in refs}
    roots = [key for key, item in items.items()
             if item.findtext('type') in ('PORISNode', 'PORISSys', 'PORISParam')
             and key not in referenced]
    if len(roots) != 1:
        raise ValueError('Expected exactly one PORIS system root')
    ordered, done, active = [], set(), set()

    def visit(key):
        if key in active:
            raise ValueError('Cyclic PORIS destination references')
        if key not in items:
            raise ValueError('Unresolved PORIS destination reference')
        if key in done:
            return
        active.add(key)
        for dependency in dependencies[key]:
            visit(dependency)
        active.remove(key)
        done.add(key)
        ordered.append(items[key])

    for key in items:
        if key != roots[0]:
            visit(key)
    visit(roots[0])
    root[:] = ordered
    return ElementTree.tostring(root, encoding='utf-8', xml_declaration=True)


def download_model(instance, project, item=None, scope=None, *, java_order=True):
    scope = scope or ('node_down' if item else 'project')
    if scope != 'project' and not item:
        raise ValueError('node and node_down scopes require an item')
    with requests.Session() as session:
        session.verify = not instance['ignorecert']
        if instance['key']:
            session.headers['X-Redmine-API-Key'] = instance['key']
        base = instance['url']
        params = {'scope': scope}
        if project is None:
            data = get(session, f'{base}/issues/{int(item)}.json').json()['issue']
            project = str(data['project']['id'])
            params['issue_id'] = data['id']
        elif item:
            lookup = f'id/{int(item)}' if item.isdecimal() else quote(item, safe='')
            data = get(session, f'{base}/{quote(project, safe="")}/cosmosys/items/{lookup}.json').json()['item']
            # Native CSIDs are tree-scoped; the viewer needs the item's own project.
            project = data['project']['identifier']
            params['issue_id'] = data['id']
        response = get(session, f'{base}/projects/{quote(project, safe="")}/poris/model.xml', params)
        if java_order:
            return order_model_xml(response.content)
        root = ElementTree.fromstring(response.content)
        if root.tag != 'poris':
            raise ValueError('The server did not return a PORIS XML model')
        return response.content


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('instance', help='instance name in csys.yaml, or a project/item URL')
    parser.add_argument('project', nargs='?', help='project identifier (name-based form)')
    parser.add_argument('item', nargs='?', help='native CSID or numeric issue ID')
    parser.add_argument('--scope', choices=['node', 'project', 'node_down'])
    parser.add_argument('--config', help='alternative instance YAML file')
    parser.add_argument('--web', action='store_true')
    parser.add_argument('--no-panel', action='store_true', help='download only; requires --output')
    parser.add_argument('--output', type=Path, help='keep the downloaded XML at this path')
    args = parser.parse_args()
    if args.no_panel and not args.output:
        parser.error('--no-panel requires --output')
    try:
        if args.instance.startswith(('http://', 'https://')):
            if args.project or args.item:
                raise ValueError('Do not combine a URL with project/item arguments')
            instance, project, item, url_scope = resolve_url(args.instance, args.config)
            scope = args.scope or url_scope
        else:
            if not args.project:
                raise ValueError('An instance name requires a project identifier')
            instance = load_instance(args.instance, args.config)
            project, item, scope = args.project, args.item, args.scope
        xml = download_model(instance, project, item, scope, java_order=not args.web)
        with tempfile.TemporaryDirectory(prefix='poris-csys-') as temp:
            path = args.output or Path(temp) / 'model.xml'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(xml)
            if args.output:
                print(f'PORIS XML: {path}')
            if not args.no_panel:
                launcher = Path(__file__).resolve().parents[1] / 'xmlporispanel.sh'
                subprocess.run([str(launcher), *(['--web'] if args.web else []), str(path.resolve())], check=True)
    except (ValueError, KeyError, OSError, requests.RequestException, ElementTree.ParseError, DefusedXmlException, subprocess.CalledProcessError) as error:
        # HTTP library errors may contain request details; never print credentials.
        print(str(error) if isinstance(error, ValueError) else f'Cannot open PORIS model ({type(error).__name__})', file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
