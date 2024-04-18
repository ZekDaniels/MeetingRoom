"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import dotenv

from django.core.asgi import get_asgi_application
dotenv.load_dotenv(
    os.path.join(os.path.dirname(__file__), '.env')
)
os.environ['DJANGO_SETTINGS_MODULE'] = os.environ.get('DJANGO_SETTINGS_MODULE', 'core.settings.development')

application = get_asgi_application()
