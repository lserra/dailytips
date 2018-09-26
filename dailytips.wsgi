activate_this = '/home/datafresh/.virtualenvs/dailytips/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
 
import sys
 
sys.path.append('/home/datafresh/apps_wsgi/dailytips')
 
from app import app as application