"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import dotenv
from django.core.wsgi import get_wsgi_application
dotenv.load_dotenv(
    os.path.join(os.path.dirname(__file__), '.env')
)

os.environ['DJANGO_SETTINGS_MODULE'] = os.environ.get('DJANGO_SETTINGS_MODULE', 'core.settings.development')

application = get_wsgi_application()