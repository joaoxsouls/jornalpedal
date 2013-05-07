import os
import sys

from django.core.handlers.wsgi import WSGIHandler

os.environ['DJANGO_SETTINGS_MODULE'] = 'pedal.settings.live'
application = WSGIHandler()
