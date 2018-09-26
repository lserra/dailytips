activate_this = '/home/datafresh/.virtualenvs/dailytips/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
 
import sys
 
sys.path.append('/home/datafresh/apps_wsgi/dailytips')
 
import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

# ... build or import your bottle application here ...
import bottle
import app

# Do NOT use bottle.run() with mod_wsgi
application = bottle.default_app()