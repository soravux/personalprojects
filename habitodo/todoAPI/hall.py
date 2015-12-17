import json
import requests

base_url = 'https://habitrpg.com/api/v2/'

def heroes(headers):
    ''' Returns a list of the heroes of HabitRPG'''
    return json.loads(requests.get(base_url + 'hall/heroes', headers=headers).text)

#def hero(headers, herouid):
#   ''' NEEDS ADMIN ACCESS '''
#   return json.loads(requests.get(base_url + 'hall/heroes/' + herouid, headers=headers).text)

#def heroespost(headers):
#   ''' NEEDS ADMIN ACCESS PROBABLY'''
#    return None

def patrons(headers, pagenumber=0):
    ''' Returns a list of the patrons of HabitRPG, page can be from 0 to 42'''
    return json.loads(requests.get(base_url + 'hall/patrons?page='+ str(pagenumber), headers=headers).text)
