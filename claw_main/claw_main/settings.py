"""
Django settings for claw_main project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@aw@3&c0-8m+9)47!3du_&-mz9mvatl*y&&wny3l8+b4qt__o+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Setup Email credential for receving mail messages
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'testcopser@gmail.com'
EMAIL_HOST_PASSWORD = 'Test84Applications'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'main',
    'django.contrib.flatpages',
    'contact',
    'portfolio',
    'boto',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'claw_main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'claw_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'POST': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Zagreb'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# Crispy forms configuration
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Heroku Configuration
# Extending settings.py to loacal_settings.py
ALLOWED_HOSTS = ["*"]

# Parse database configuration from $DATABASES_URL
import dj_database_url

DATABASES = {'default': dj_database_url.config()}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# try load local_settings.py if it exists
try:
    from .local_settings import *
except Exception, e:
    pass

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

# Configuration S3 Amazon Web Service for static serving
# Storage on S3 settings are stored as os.environs to keep settings.py clean
# if not DEBUG:
#     AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
#     AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
#     AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
#     STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#     S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#     STATIC_URL = S3_URL

# Memcachier configuration
os.environ["MEMCACHE_SERVERS"] = os.environ.get("MEMECACHE_SERVERS", '').\
    replace(',', ';')
os.environ["MEMCACHE_USERNAME"] = os.environ.get("MEMECACHE_USERNAME", '')
os.environ["MEMCACHE_PASSWORD"] = os.environ.get("MEMECACHE_PASSWORD", '')

CACHES = {
    'default': {
        # Use pylibmc
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',

        # Use binary memcache protocol (needed for authentication)
        'BINARY': True,

        'TIMEOUT': None,

        'OPTIONS': {
            # Enable faster IO
            'no_block': True,
            'tcp_nodelay': True,

            # Keep connection alive
            'tcp_keeplive': True,

            # Timeout for set/get requests
            '_poll_timeout': 2000,

            # Use consistent hashing for failover
            'ketama': True,

            # Configure failover timings
            'connect_timeout': 2000,
            'remove_failed': 4,
            'retry_timeout': 2,
            'dead_timeout': 10
        }
    }
}
