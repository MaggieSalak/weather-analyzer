import json
import requests

def query_url(url):
    resp = requests.get(url=url)
    resp_json = json.dumps(resp.json())
    return json.loads(resp_json)