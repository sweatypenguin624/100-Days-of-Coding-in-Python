"""
ASGI config for demoproj project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
# ASGI AND WSGI are special config files that we dont have to deal with
# these files will allow django to communicate with the web server

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproj.settings')

application = get_asgi_application()
