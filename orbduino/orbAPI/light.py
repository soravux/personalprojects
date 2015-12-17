# This file provides control for the light orb.
import requests
base = 'http://tnhsmith.dyndns.org:2100/ard?'

def level(lvl):
    ''' Changes the level of the light in the room, {0, 1, 2, 3}'''
    requests.get(base+'mlts='+str(lvl))
