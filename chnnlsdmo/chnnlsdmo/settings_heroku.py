import os
from os.path import abspath, basename, dirname, join, normpath
from sys import path

from .settings import *

DEBUG = True 

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)
DATABASES['default'] =  dj_database_url.config()
ROOT_URLCONF = 'chnnlsdmo.chnnlsdmo.urls'

