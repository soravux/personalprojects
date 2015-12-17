import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def list(headers):
    ''' Returns a list of the challenges available'''
    return json.loads(requests.get(base_url + 'challenges', headers=headers).text)

def create(headers):
    ''' Creates a challenge'''
    #Todo (requires schema)

def get(headers, cid):
    ''' Get a challenge'''
    return json.loads(requests.get(base_url + 'challenges/' + cid, headers=headers).text)

def getcsv(headers, cid):
    ''' Get a challenge, csv edition'''
    return requests.get(base_url + 'challenges/' + cid + '/csv', headers=headers).text

def update(headers, cid):
    ''' Update a challenge'''
    #Todo (requires schema)
    
def delete(headers, cid):
    ''' Deletes a challenge'''
    return requests.delete(base_url + 'challenges/' + cid, headers=headers).text

def close(headers, cid, uid):
    ''' Closes a challenge'''
    return requests.post(base_url + 'challenges/' + cid + '/close?uid=' + uid, headers=headers).text

def join(headers, cid):
    ''' Joins a challenge'''
    return requests.post(base_url + 'challenges/' + cid + '/join', headers=headers).text

def leave(headers, cid):
    ''' Leaves a challenge'''
    return requests.post(base_url + 'challenges/' + cid + '/leave', headers=headers).text

def progress(headers, cid, uid):
    ''' Get a member's progress in a particular challenge'''
    return json.loads(requests.get(base_url + 'challenges/' + cid + '/member/' + uid, headers=headers).text)


