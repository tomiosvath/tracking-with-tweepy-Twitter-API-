#!/usr/bin/env python
# tweepy-bots/bots/favretweet.py

import tweepy
import logging
from config import create_api
import json
from datetime import datetime, timedelta

now = datetime.today().now()
prev=now-timedelta(days=1)
now=now.strftime("%Y-%m-%d")
prev=prev.strftime("%Y-%m-%d")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

file = open("Trump.txt", "w")

class Last24(tweepy.StreamListener):
    def __init__(self, api, account):
        self.account = account
        self.api = api
        #self.me = api.me()

    def last24(self):
        now = datetime.today().now()
        prev=now-timedelta(days=1)
        now=now.strftime("%Y-%m-%d")
        prev=prev.strftime("%Y-%m-%d")

        nr = 0
        for tweet in tweepy.Cursor(self.api.search, q = self.account, since=prev, until=now).items():
            nr += 1
            ##print('Tweet by: @' + tweet.user.screen_name + '\n')
        
        print(nr)

def main():
    api = create_api()
    list24 = Last24(api, 'PSG')
    list24.last24()

if __name__ == "__main__":
    main()