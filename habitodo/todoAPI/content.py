import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def content():
    ''' Returns a dictionary containing the game's content'''
    return json.loads(requests.get(base_url + 'content').text)
