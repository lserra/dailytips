#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
This task should be run in a daily cronjob to look for new tips and update
stats (number of likes and retweets) on existing tweets.
The tables are recreated daily.
"""
import os
import re
import sys
import tweepy
from collections import Counter
from tips.db import (
    truncate_tables, get_hashtags, add_hashtags, get_tips, add_tips
)


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')
TWITTER_ACCOUNT = os.environ.get('BIGDATA_TIP_APP_TWITTER_ACCOUNT')
EXCLUDE_PYTHON_HASHTAG = True

# Extracting hashtags from the tips
TAG = re.compile(r'#([a-z0-9]{3,})')


def _get_twitter_api_session():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    # This will make the rest of the code obey the rate limit
    # Rate limits are divided into 15 minute intervals
    return tweepy.API(auth, wait_on_rate_limit=True)


def _get_tweets(screen_name=TWITTER_ACCOUNT):
    """
    The exclude_replies=True and include_rts=False arguments are convenient
    because we only want Daily Big Data Tip’s own tweets (not re-tweets).
    Total archive is limited to 3200 tweets but there is a Daily limit of 1500
    """
    api = _get_twitter_api_session()
    # Sample 1: get tweets by timeline of user
    # return tweepy.Cursor(api.user_timeline,
    # screen_name=screen_name,
    # exclude_replies=True,
    # include_rts=False)

    # Sample 2: get tweets by timeline of home
    # return tweepy.Cursor(
    #     api.home_timeline,
    #     screen_name=screen_name,
    #     exclude_replies=True,
    #     include_rts=False)

    # Sample 3: get tweets by searching a hashtag
    results = []
    # Get the first 150 items based on the search query and store it
    for tweet in tweepy.Cursor(api.search, q='bigdata', lang='en').items(150):
        results.append(tweet)

    return results


def get_hashtag_counter(tips):
    """
    The collections.Counter returns a dict like object with the tags as keys,
    and counts as values, ordered in descending order by values (most common).
    I excluded the too common python tag which would skew the results.
    """
    blob = ' '.join(t.text.lower() for t in tips)
    cnt = Counter(TAG.findall(blob))    # to get all tags

    if EXCLUDE_PYTHON_HASHTAG:
        cnt.pop('python', None)

    return cnt


def get_tweet(tweets=None):
    if tweets is None:
        tweets = _get_tweets(TWITTER_ACCOUNT)
    add_tips(tweets)


def get_hashtag():
    tips = get_tips()
    hashtags_cnt = get_hashtag_counter(tips)
    add_hashtags(hashtags_cnt)
