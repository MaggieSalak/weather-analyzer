import json
import requests

def query_url(url):
    print('Querying URL')
    resp = requests.get(url=url)
    resp_json = json.dumps(resp.json())
    return json.loads(resp_json)