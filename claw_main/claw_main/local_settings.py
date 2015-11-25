from .settings import *
import os

DEBUG = True

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bookclaw_db',
        'USER': 'petarp',
        'PASSWORD': 'gnomeregan',
        'HOST': 'localhost',
        'POST': '5432',
    }
}

# Email configuration
EMAIL_HOST_USER = 'testcopser@gmail.com'
EMAIL_HOST_PASSWORD = 'Test84Applications'
