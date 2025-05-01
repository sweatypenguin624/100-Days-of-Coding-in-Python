"""
WSGI config for demoproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""
# ASGI AND WSGI are special config files that we dont have to deal with
# these files will allow django to communicate with the web server
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproj.settings')

application = get_wsgi_application()
