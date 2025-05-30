"""
WSGI config for permai_ayu_dki_jakarta project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import sys
import os

path = '/home/andiliani/permai_ayu_dki_jakarta'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'permai_ayu_dki_jakarta.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
