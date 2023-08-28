import pandas as pd
import requests
import json
import csv
import time
import datetime

#! DOES NOT WORK BECAUSE REDDIT IS BEING A BITCH RN

def getReddit(query, after_date, before_date, sub):
    url = 'https://api.pushshift.io/reddit/search/submission/?q='+str(query)+'&size=1000&after='+str(after_date)+'&before='+str(before_date)+'&subreddit='+str(sub)
    print(url)
    r = requests.get(url)
    data = json.loads(r.text)
    print(data)
    return data['data']

after = datetime.datetime(2023, 1, 1)
before = datetime.datetime(2023, 1, 5)

after = time.mktime(after.timetuple())
before = time.mktime(before.timetuple())

print(getReddit('Amazon', int(after), int(before), 'all'))