"""
WSGI config for project_48_3 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from waitress import serve

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_48_3.settings')

application = get_wsgi_application()

if __name__ == '__main__':
    serve(application, host='0.0.0.0', port=8000)
