#!/usr/bin/env python3
''' data mining fun'''

import praw
import pickle
import requests
import re
import time

theUsers = dict()
theSubreddits = dict()
r = praw.Reddit(user_agent='funwithdataapplication0.01')

# fetch list of most popular subreddits by subscribers by scrapping redditmetrics, up to offset 100000, this goes to approximately 2500 subscribers
# log subreddit name and subscriber number

BASE_URL = 'http://redditmetrics.com/top/offset/'
LIMIT = 100000
JUMP = 100
TIME = 1 # time in seconds
subredditDict = dict()

for pageNumber in range(0, LIMIT+JUMP, JUMP):
    print('Parsing page: ' + str(pageNumber))
    statusCode = 999
    while statusCode != 200:
        time.sleep(TIME)
        url = BASE_URL + str(pageNumber)
        page = requests.get(url)
        statusCode = page.status_code
        if statusCode != 200:
          print('Page fetch failed! retrying...')

    subredditmatches = re.findall('href="/r/(.*)"', page.text)
    numbermatches = re.findall('tod">([1234567890,]+)<', page.text)
    
    for index in range(len(subredditmatches)):
        subredditDict[subredditmatches[index]] = {'subscriberNumber':numbermatches[index]}

# pickle the data

with open('subredditdata.pickle', 'wb') as f:
    pickle.dump(subredditDict, f, pickle.HIGHEST_PROTOCOL)
