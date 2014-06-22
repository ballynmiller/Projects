import os
import sys

path = '/svn'
sys.path.append(path)
sys.path.append('/svn/websites')

os.environ['DJANGO_SETTINGS_MODULE'] = 'websites.jakore_settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

