"""
WSGI config for chnnlsdmo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

if 'DYNO' in os.environ:
    debug = False
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chnnlsdmo.chnnlsdmo.settings_heroku")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chnnlsdmo.chnnlsdmo.settings")
    debug = True



application = get_wsgi_application()
application = DjangoWhiteNoise(application)
