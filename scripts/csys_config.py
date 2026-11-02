"""Named cosmoSys connections shared by importers and the remote viewer."""
import os
from pathlib import Path
from urllib.parse import urlsplit

import yaml

DEFAULT_CONFIG = Path(__file__).resolve().parents[1] / 'csys.yaml'


def load_instances(path=None):
    path = Path(path or os.environ.get('PORIS_CSYS_CONFIG', DEFAULT_CONFIG))
    try:
        instances = yaml.safe_load(path.read_text())
    except (OSError, yaml.YAMLError):
        raise ValueError(f'Cannot read instance configuration: {path}') from None
    if not isinstance(instances, dict):
        raise ValueError('Instance configuration must be a mapping')
    return instances


def load_instance(name, path=None):
    instances = load_instances(path)
    if name not in instances:
        raise ValueError(f'Unknown cosmoSys instance: {name}')
    entry = instances[name]
    if not isinstance(entry, dict):
        raise ValueError('Instance configuration must be a mapping')
    url, key, ignore = entry.get('url'), entry.get('key', ''), entry.get('ignorecert', False)
    if not isinstance(url, str) or not isinstance(key, str) or not isinstance(ignore, bool):
        raise ValueError('Expected url/key strings and an ignorecert boolean')
    parts = urlsplit(url)
    if parts.scheme not in ('http', 'https') or not parts.netloc or parts.username or parts.password or parts.query or parts.fragment:
        raise ValueError('Instance url must be an explicit http(s) URL without credentials, query or fragment')
    return {'url': url.rstrip('/'), 'key': key, 'ignorecert': ignore}


csys_use = bool(os.environ.get('PORIS_CSYS_INSTANCE'))
csys_server_url = csys_key_txt = csys_ignorecert = None
if csys_use:
    _instance = load_instance(os.environ['PORIS_CSYS_INSTANCE'])
    csys_server_url = _instance['url']
    csys_key_txt = _instance['key']
    csys_ignorecert = _instance['ignorecert']


if __name__ == '__main__':
    for name in load_instances():
        print(name)
