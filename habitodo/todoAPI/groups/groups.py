import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def list(headers):
    ''' Returns a list of all the groups'''
    return json.loads(requests.get(base_url + 'groups', headers=headers).text)

def create(headers):
    ''' Creates a group'''
    #Todo Needs schema

def info(headers, gid = 'party'):
    ''' Get a group's info, defaults to the user's party'''
    return json.loads(requests.get(base_url + 'groups/' + gid, headers=headers).text)

def edit(headers, gid = 'party'):
    ''' Edits a group'''
    #Todo Needs schema

def join(headers, gid):
    ''' Joins a group'''
    return json.loads(requests.post(base_url + 'groups/' + gid + '/join', headers=headers).text)

def leave(headers, gid):
    ''' Leave a group'''
    return requests.post(base_url + 'groups/' + gid + '/leave', headers=headers).text

def invite(headers, gid, uuid):
    ''' Invites a user to a group'''
    return json.loads(requests.post(base_url + 'groups/' + gid + '/invite?uuid=' + uuid, headers=headers).text)

def remove(headers, gid, uuid):
    ''' Removes a member from a group'''
    return json.loads(requests.post(base_url + 'groups/' + gid + '/removeMember?uuid=' + uuid, headers=headers).text)

def accept(headers, gid, key=None):
    ''' Accepts a quest invitation'''
    return json.loads(requests.post(base_url + 'groups/' + gid + '/questAccept', headers=headers).text)

def reject(headers, gid):
    ''' Rejects a quest invitation'''
    return json.loads(requests.post(base_url + 'groups/' + gid + '/questReject', headers=headers).text)

def abort(headers, gid):
    ''' Aborts a quest'''
    return json.loads(requests.post(base_url + 'groups/' + gid + '/questAbort', headers=headers).text)
