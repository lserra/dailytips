#!/usr/bin/python3
# -*- coding: utf-8 -*-


from os import environ
import re
import sys
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tips.models import Base, Hashtag, Tip

VALID_TAG = re.compile(r'^[a-z0-9]+$')
DATABASE_URL = 'postgres://postgres:postgres@localhost:5432/datafresh'


def _create_session():
    # db_url = os.environ.get('DATABASE_URL')
    db_url = DATABASE_URL

    if 'datafresh' in sys.argv:
        db_url += '_test'

    if not db_url:
        raise EnvironmentError('Need to set the DATABASE_URL parameter')

    engine = create_engine(db_url, echo=True)
    Base.metadata.create_all(engine)
    create_session = sessionmaker(bind=engine)
    return create_session()


session = _create_session()


def truncate_tables():
    session.query(Tip).delete()
    session.query(Hashtag).delete()
    session.commit()


def get_hashtags():
    return session.query(Hashtag).order_by(Hashtag.name.asc()).all()


def add_hashtags(hashtags_cnt):
    for tag, count in hashtags_cnt.items():
        session.add(Hashtag(name=tag, count=count))
    session.commit()


def get_tips(tag=None):
    if tag is not None and VALID_TAG.match(tag.lower()):
        filter_ = "%{}%".format(tag.lower())
        tips = session.query(Tip)
        tips = tips.filter(Tip.text.ilike(filter_))
    else:
        tips = session.query(Tip)

    tips = tips.order_by(Tip.likes.desc())
    return tips.all()


def add_tips(tweets):
    tweets = tweets if isinstance(tweets, list) else tweets.items()
    for tw in tweets:
        session.add(Tip(tweetid=tw.id,
                        text=tw.text,
                        created=tw.created_at,
                        likes=tw.favorite_count,
                        retweets=tw.retweet_count))
    session.commit()
