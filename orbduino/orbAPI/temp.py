# This file provides control for the light orb.
import requests
base = 'http://tnhsmith.dyndns.org:2100/ard?'

def read():
    ''' Reads the temps and returns them as (indoor, outdoor)'''
    temp = requests.get(base+'tmp0=')
    return (temp.text[20:24], temp.text[50:54])
