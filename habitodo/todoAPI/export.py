import requests

base_url = 'https://habitrpg.com/api/v2/'

def history(headers):
    ''' Returns the user's history'''
    return requests.get(base_url + 'export/history', headers=headers).text.split('\n')
