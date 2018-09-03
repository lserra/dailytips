#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
This task should be run in a daily cronjob to look for new tips and update stats (number of likes and retweets)
on existing tweets. The tables are recreated daily.
"""
import os
import re
import sys
import tweepy

from collections import Counter
from tips.db import add_tips, truncate_tables, get_tips, add_hashtags


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

TWITTER_ACCOUNT = os.environ.get('BIGDATA_TIP_APP_TWITTER_ACCOUNT') or 'datafresh'
EXCLUDE_PYTHON_HASHTAG = True
TAG = re.compile(r'#([a-z0-9]{3,})')    # Extracting hashtags from the tips


def _get_twitter_api_session():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return tweepy.API(auth)


def get_tweets(screen_name=TWITTER_ACCOUNT):
    """
    The exclude_replies=True and include_rts=False arguments are convenient because we only want Daily Big Data Tip’s
    own tweets (not re-tweets).
    """
    api = _get_twitter_api_session()
    return tweepy.Cursor(api.user_timeline,
                         screen_name=screen_name,
                         exclude_replies=True,
                         include_rts=False)


def get_hashtag_counter(tips):
    """
    The collections.Counter returns a dict like object with the tags as keys, and counts as values, ordered in
    descending order by values (most common). I excluded the too common python tag which would skew the results.
    """
    blob = ' '.join(t.text.lower() for t in tips)
    cnt = Counter(TAG.findall(blob))    # to get all tags

    if EXCLUDE_PYTHON_HASHTAG:
        cnt.pop('python', None)

    return cnt


def import_tweets(tweets=None):
    if tweets is None:
        tweets = get_tweets(screen_name)
    add_tips(tweets)


def import_hashtags():
    tips = get_tips()
    hashtags_cnt = get_hashtag_counter(tips)
    add_hashtags(hashtags_cnt)


if __name__ == '__main__':
    try:
        screen_name = sys.argv[1]
    except IndexError:
        screen_name = TWITTER_ACCOUNT

    truncate_tables()

    import_tweets()
    import_hashtags()
