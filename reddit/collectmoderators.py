#!/usr/bin/env python3
''' data mining fun'''

import praw
import pickle
import requests
import re
import time

TIME = 2

theUsers = dict()
theSubreddits = dict()
r = praw.Reddit(user_agent='funwithdataapplication0.01b')

# unpickle the data

with open('subredditdata.pickle', 'rb') as f:
    subredditDict = pickle.load(f)

# collects a list of the moderators for each subreddit in the dictionary

for subredditname in subredditDict.keys():
    print('Collecting for subreddit: ' + str(subredditname))
    hasFetched = false
    while not hasFetched:
        time.sleep(TIME)
        theModerators = r.get_moderators(subredditname)
        hasFetched = theModerators.hasFetched
        if not hasFetched:
            print('Fetch failed! retrying...')
    if 'moderatorList' not in subredditDict[subredditname].keys():
        subredditDict[subredditname]['moderatorList'] = list()
    for moderator in theModerators:
        subredditDict[subredditname]['moderatorList'].append(moderator.name)

# save the data
with open('subredditdata2.pickle', 'wb') as f:
    pickle.dump(subredditDict, f, pickle.HIGHEST_PROTOCOL)
