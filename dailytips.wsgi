activate_this = '/home/datafresh/.virtualenvs/dailytips/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
 
import sys
 
sys.path.append('/home/datafresh/apps_wsgi/dailytips')
 
import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

# ... build or import your bottle application here ...
# import bottle
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


# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()