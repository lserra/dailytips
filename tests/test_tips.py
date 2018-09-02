#!/usr/bin/python
# -*- coding: utf-8 -*-


import json
import os
import pytest

from collections import namedtuple, Counter
from tips.db import truncate_tables, get_hashtags, add_hashtags, get_tips, add_tips
from tasks.import_tweets import import_tweets, import_hashtags


tweet = namedtuple('Tweet', 'id text created_at favorite_count retweet_count')


def _gen_tweets():
    tweets = os.path.join('tests', 'tweets.json')

    with open(tweets) as f:
        data = json.loads(f.read())

    for entry in data:
        yield tweet(id=entry['id'],
                    text=entry['text'],
                    created_at=entry['created_at'],
                    favorite_count=entry['favorite_count'],
                    retweet_count=entry['retweet_count'])


@pytest.fixture()
def db_setup(request):

    tweets = list(_gen_tweets())
    import_tweets(tweets)
    import_hashtags()

    def fin():
        truncate_tables()

    request.addfinalizer(fin)


def test_get_tips(db_setup):
    tips = get_tips()
    assert len(tips) == 10
    jupyter_tips = get_tips('jupyter')
    assert len(jupyter_tips) == 2
    numpy_tips = get_tips('numpy')
    assert len(numpy_tips) == 2


def test_add_tips(db_setup):
    tweets = list(_gen_tweets())[:2]
    add_tips(tweets)
    tips = get_tips()
    assert len(tips) == 12


def test_get_hashtags(db_setup):
    hashtags = get_hashtags()
    assert len(hashtags) == 3
    assert hashtags[0].name == 'jupyter'
    assert hashtags[0].count == 2
    assert hashtags[-1].name == 'selfpromo'
    assert hashtags[-1].count == 1


def test_add_hashtags(db_setup):
    new_hashtags = Counter({'pandas': 5,
                            'itertools': 1,
                            'python3': 1})
    add_hashtags(new_hashtags) == 6
    hashtags = get_hashtags()
    assert hashtags[1].name == 'jupyter'
    assert hashtags[1].count == 2
    assert hashtags[-1].name == 'selfpromo'
    assert hashtags[-1].count == 1
