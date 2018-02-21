#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import tweepy
from tweeter import twitter, StreamListener


# Dealing With Unicode Stuff for scraping
reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
    """
    Create a Custom Tweepy stream listener and start listening for Tweets tagged with @IsThisTrueBot
    """
    stream = tweepy.Stream(auth=twitter.auth, listener=StreamListener())
    stream.filter(track=['@IsThisTrueBot'], async=True)
