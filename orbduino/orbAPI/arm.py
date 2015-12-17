# This file provides control for the arm.
import requests
baseurl = 'http://tnhsmith.dyndns.org:2100/ard?'
def pincher(angle):
    ''' Moves the pincher, +- 255'''
    requests.get(baseurl + 'armp=255'*(angle//255) + 'armp=-255'*(-angle//255) + 'armp=' + str(int(abs(angle)%255 * abs(angle)/angle)))

def spotlight(brightness):
    ''' Sets the spotlight's brightness, 0-255'''
    requests.get(baseurl+'arml='+str(int(brightness%256)))

def wrist(angle):
    ''' Moves the wrist, +- 255'''
    requests.get(baseurl + 'armw=255'*(angle//255) + 'armw=-255'*(-angle//255) + 'armw=' + str(int(abs(angle)%255 * abs(angle)/angle)))

def elbow(angle):
    ''' Moves the elbow, +- 255'''
    requests.get(baseurl + 'arme=255'*(angle//255) + 'arme=-255'*(-angle//255) + 'arme=' + str(int(abs(angle)%255 * abs(angle)/angle)))

def shoulder(angle):
    ''' Moves the shoulder, +- 255'''
    requests.get(baseurl + 'arms=255'*(angle//255) + 'arms=-255'*(-angle//255) + 'arms=' + str(int(abs(angle)%255 * abs(angle)/angle)))

def base(angle):
    ''' Moves the baseurl, +- 255'''
    requests.get(baseurl + 'armb=255'*(angle//255) + 'armb=-255'*(-angle//255) + 'armb=' + str(int(abs(angle)%255 * abs(angle)/angle)))
