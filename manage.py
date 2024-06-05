#!/usr/bin/env python

"""Django's manage.py."""

import os
import sys
import environ

env = environ.Env()

if __name__ == "__main__":
    DEBUG = env.bool('DJANGO_DEBUG', False)
    
    config = "config.settings.local" if DEBUG else "config.settings.production"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", config)


    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django  # noqa
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )

        raise

    # This allows easy placement of apps within the interior
    # render_test_01 directory.
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, "render_test_01"))

    execute_from_command_line(sys.argv)
