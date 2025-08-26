import os,sys
from django.core.wsgi import get_wsgi_application

from Core.wsgi import application

project_name='/home/cp63891715512/myproject/core'
if project_name not in sys.path:
    sys.path.append(project_name)
os.environ['DJANGO_SETTINGS_MODULE']='myproject.settings'

application=get_wsgi_application()