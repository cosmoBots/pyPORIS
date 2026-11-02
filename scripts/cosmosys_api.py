from urllib.parse import quote

import requests


class CosmosysApi:
    """Read native cosmoSys item identities through its authenticated API."""

    def __init__(self, base_url, api_key, verify=True):
        self.session = requests.Session()
        self.session.headers.update({'X-Redmine-API-Key': api_key})
        self.base_url = base_url.rstrip('/')
        self.verify = verify

    def _item(self, project_identifier, path):
        url = f"{self.base_url}/{quote(project_identifier, safe='')}/cosmosys/items/{path}.json"
        response = self.session.get(url, verify=self.verify)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()['item']

    def by_csid(self, project_identifier, csid):
        return self._item(project_identifier, quote(csid, safe='-'))

    def by_id(self, project_identifier, issue_id):
        return self._item(project_identifier, f"id/{int(issue_id)}")

    def update_by_id(self, project_identifier, issue_id, attributes):
        url = f"{self.base_url}/{quote(project_identifier, safe='')}/cosmosys/items/id/{int(issue_id)}.json"
        response = self.session.patch(url, json={'item': attributes}, verify=self.verify)
        response.raise_for_status()
        return response.json()['item']
