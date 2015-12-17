import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def status():
    ''' Retruns the status of the server (up or down)'''
    return json.loads(requests.get(base_url + 'status').text)['status']
