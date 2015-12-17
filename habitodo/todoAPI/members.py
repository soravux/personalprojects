import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def members(headers, uid):
    ''' Returns an information dict about a member'''
    return json.loads(requests.get(base_url + 'members/' + uid, headers=headers).text)
