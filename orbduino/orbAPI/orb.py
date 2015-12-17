# This file provides control for the light orb.
import requests
base = 'http://tnhsmith.dyndns.org:2100/ard?'

def off():
    '''sets the orb off'''
    requests.get(base+'ored=0&ogrn=0&oblu=0')
def flow():
    ''' starts the random flow of colors'''
    requests.get(base+'oflo=')
def color(*rgb):
    ''' sets the color, 0-255 * 3'''
    requests.get(base+'ored='+str(rgb[0])+'ogrn='+str(rgb[1])+'oblu='+str(rgb[2]))
