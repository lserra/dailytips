#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os

from bottle import route, run, request, static_file, view
from tips.db import get_hashtags, get_tips


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')


@route('/')
@route('/<tag>')
@view('index')
def index(tag=None):
    tag = tag or request.query.get('tag') or None
    tags = get_hashtags()
    tips = get_tips(tag)

    return {'search_tag': tag or '',
            'tags': tags,
            'tips': tips}


if os.environ.get('APP_LOCATION') == 'kinghost':
    # run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    run(host='0.0.0.0', port=80)
else:
    run(host='localhost', port=8080, debug=True, reloader=True)
