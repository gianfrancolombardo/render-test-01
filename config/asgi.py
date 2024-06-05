"""
ASGI config for Django project.

This module contains the ASGI application used by Django's development server
and any ASGI deployments. It should expose a module-level variable named
``application``. Django's ``runserver`` command will discover this application
via the ``ASGI_APPLICATION`` setting.

Usually you will have the standard Django ASGI application here, but it also
might make sense to replace the whole Django ASGI application with a custom one
that later delegates to the Django one. For example, you could introduce ASGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import sys

from django.core.asgi import get_asgi_application

# This allows easy placement of apps within the interior
# render_test_01 directory.
app_path = os.path.abspath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.pardir))
sys.path.append(os.path.join(app_path, 'render_test_01'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = get_asgi_application()