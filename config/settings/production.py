import os

from .partials import *


DEBUG = True
# INTERNAL_IPS = ['1.234.21.73', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["POSTGRES_DB_NAME"],
        'USER': os.environ["POSTGRES_USER"],
        'PASSWORD': os.environ["POSTGRES_PASSWORD"],
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
