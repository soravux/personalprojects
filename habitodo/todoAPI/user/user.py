import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def get(headers): 
    ''' Scores a task'''
    return json.loads(requests.post(base_url + 'user/tasks/' + tid + '/' + direction, headers=headers).text)

def update(headers):
    ''' Gets all user's tasks'''
    return json.loads(requests.get(base_url + 'user/tasks', headers=headers).text)

def delete(headers):
    ''' Creates a task'''
    #Todo

def revive(headers):
    #todo

def reroll(headers):
    #todo

def reset(headers):
    #todo

def sleep(headers):
    #todo

def rebirth(headers):
    #todo

def batch_update(headers):
    #todo

