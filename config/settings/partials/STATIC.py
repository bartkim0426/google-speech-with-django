import os

from .BASE import ROOT_DIR, CONFIG_DIR

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(ROOT_DIR, 'staticfiles')
STATIC_ROOT = str(ROOT_DIR('staticfiles'))
STATICFILES_DIRS = [
    str(CONFIG_DIR.path('static')),
    # os.path.join(str(CONFIG_DIR), 'static'),
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
