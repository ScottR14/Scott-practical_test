import os
import sys

path = '/home/ScottR14/Scott-practical_test/pets/'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pets.settings')
# Set up Django-- let it instantiate everything!
import django
django.setup()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler
