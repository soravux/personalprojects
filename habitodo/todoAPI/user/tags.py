import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def create(headers, tid, direction):
    ''' Scores a task'''
    #todo needs schema

def edit(headers):
    ''' Gets all user's tasks'''
    #todo needs schema

def delete(headers, tid):
    ''' Creates a task'''
    return requests.delete(base_url + 'user/tags/' + tid, headers=headers).text
