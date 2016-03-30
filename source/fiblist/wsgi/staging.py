"""
WSGI config for fiblist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/nick/sites/fiblist/source')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fiblist.settings")

application = get_wsgi_application()
