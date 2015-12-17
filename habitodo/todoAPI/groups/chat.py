import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def list(headers, gid):
    ''' Get all chat messages'''
    return json.loads(requests.get(base_url + 'groups/' + gid + '/chat', headers=headers).text)

def send(headers, gid, message):
    ''' Sends a message'''
    return requests.post(base_url + 'groups/' + gid + '/chat?message=' + message, headers=headers)

def seen(headers, gid):
    ''' Flags messages as seen for a group'''
    return requests.post(base_url + 'groups/' + gid + '/chat/seen', headers=headers).text

def delete(headers, gid, mid):
    ''' Deletes a chat message in a given group'''
    return requests.delete(base_url + 'groups/' + gid + '/chat/' + mid, headers=headers).text

def like(header, gid, mid):
    '''Likes a chat message'''
    return requests.post(base_url + 'groups/' + gid + '/chat/' + mid + '/like', header=header).text

