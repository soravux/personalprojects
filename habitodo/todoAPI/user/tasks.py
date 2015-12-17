import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def score(headers, tid, direction):
    ''' Scores a task'''
    return json.loads(requests.post(base_url + 'user/tasks/' + tid + '/' + direction, headers=headers).text)

def list(headers):
    ''' Gets all user's tasks'''
    return json.loads(requests.get(base_url + 'user/tasks', headers=headers).text)

def create(headers):
    ''' Creates a task'''
    #Todo

def get(headers):
    return None

def update(headers):
    return None

def delete(headers):
    return None

def sort(headers):
    return None

def clear_completed(headers):
    return None

def unlink(headers):
    return None
