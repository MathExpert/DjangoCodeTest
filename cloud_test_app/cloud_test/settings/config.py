from __future__ import absolute_import, unicode_literals
import os

from cloud_test.utils import parse_boolean

from .base import * # noqa

# The hostnames that Django is allowed to serve from.
# https://docs.djangoproject.com/en/1.11/ref/settings/#allowed-hosts
#
# DJANGO_ALLOWED_HOSTS: a comma separated list.
#
# SECURITY WARNING: Default of '*' is unsafe for production.

_allowed_hosts = os.environ.get('DJANGO_ALLOWED_HOSTS')
if _allowed_hosts:
    ALLOWED_HOSTS = _allowed_hosts.split(',')
else:
    ALLOWED_HOSTS = ['*']

# Controls if Djangos debug mode is turned on.
# https://docs.djangoproject.com/en/1.11/ref/settings/#debug
#
# DJANGO_DEBUG: a boolean like string
#
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = parse_boolean(os.environ.get('DJANGO_DEBUG', True))

# A key used by Django for cryptographic signing of sessions, and
# token generation.
# https://docs.djangoproject.com/en/1.11/ref/settings/#secret-key
#
# DJANGO_SECRET_KEY: a long unpredictable string value
#
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    "This is a terrible secret key. Don't use me in production."
)


# Database configuration
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
#
# DJANGO_DATABASE_ENGINE: module name for engine
# DJANGO_DATABASE_NAME: name of the db or path to db file if sqlite3
# DJANGO_DATABASE_USER: name of db user
# DJANGO_DATABASE_PASSWORD: password for db user
# DJANGO_DATABASE_HOST: host address for db, default is localhost
# DJANGO_DATABASE_PORT: port for db, defaults to default port for db type
_db_engine = os.environ.get(
    'DJANGO_DATABASE_ENGINE', 'django.db.backends.sqlite3')
if _db_engine == 'django.db.backends.sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': _db_engine,
            'NAME': os.environ.get(
                'DJANGO_DATABASE_NAME',
                os.path.join(BASE_DIR, 'db.sqlite3')), # noqa
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': _db_engine,
            'NAME': os.environ.get('DJANGO_DATABASE_NAME', ''),
            'USER': os.environ.get('DJANGO_DATABASE_USER', ''),
            'PASSWORD': os.environ.get('DJANGO_DATABASE_PASSWORD', ''),
            'HOST': os.environ.get('DJANGO_DATABASE_HOST', ''),
            'PORT': os.environ.get('DJANGO_DATABASE_PORT', ''),
        }
    }

# Logging settings
# https://docs.djangoproject.com/en/1.11/ref/settings/#logging
#
# These are setup to go to console for ease of use with containers.
# Override if needed with `local.py`.
#
# DJANGO_LOGGING_LEVEL: one of DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'cloud': {
            'format':
                'DJANGO: %(levelname)s %(asctime)s %(pathname)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': os.environ.get('DJANGO_LOGGING_LEVEL', 'INFO'),
            'class': 'logging.StreamHandler',
            'formatter': 'cloud',
        },
    },
    'loggers': {
        'django': {
            'handlers': [
                'console',
            ],
            'level': os.environ.get('DJANGO_LOGGING_LEVEL', 'INFO'),
            'propagate': False,
        }
    }
}

# Email settings
#
# EMAIL_BACKEND: module of email backend
# https://docs.djangoproject.com/en/1.11/ref/settings/#email-backend
#
# smtp backend settings:
# EMAIL_HOST: host address for smtp server
# EMAIL_HOST_PASSWORD: email user password
# EMAIL_HOST_USER: email user name
# EMAIL_PORT: smtp server port
# EMAIL_USE_TLS: boolean like, use explict TLS\
# https://docs.djangoproject.com/en/1.11/ref/settings/#email-use-tls
# EMAIL_USE_SSL: boolean like, use implict TLS
# https://docs.djangoproject.com/en/1.11/ref/settings/#email-use-tls
#
# file backend settings:
# EMAIL_FILE_PATH: location of email files
EMAIL_BACKEND = os.environ.get(
    'DJANGO_EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
if EMAIL_BACKEND == 'django.core.mail.backends.smtp.EmailBackend':
    EMAIL_HOST = os.environ.get('DJANGO_EMAIL_HOST', 'localhost')
    EMAIL_HOST_PASSWORD = os.environ.get('DJANGO_EMAIL_HOST_PASSWORD', '')
    EMAIL_HOST_USER = os.environ.get('DJANGO_EMAIL_HOST_USER', '')
    EMAIL_PORT = int(os.environ.get('DJANGO_EMAIL_PORT', 25))
    EMAIL_USE_TLS = parse_boolean(
        os.environ.get('DJANGO_EMAIL_USE_TLS', False))
    EMAIL_USE_SSL = parse_boolean(
        os.environ.get('DJANGO_EMAIL_USE_SSL', False))
    DEFAULT_FROM_EMAIL = os.environ.get(
        'DJANGO_DEFAULT_FROM_EMAIL', 'django@localhost')
elif EMAIL_BACKEND == 'django.core.mail.backends.filebased.EmailBackend':
    EMAIL_FILE_PATH = os.environ.get(
        'DJANGO_EMAIL_FILE_PATH', '/tmp/django-messages')

# Timezone used for datetime when presenting datetimes to users
# https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-TIME_ZONE
#
# DJANGO_TIME_ZONE: A name of valid timezone.
TIME_ZONE = os.environ.get('DJANGO_TIME_ZONE', 'Pacific/Auckland')


# Date and Datetime formats
# https://docs.djangoproject.com/en/1.11/ref/settings/#date-format
# https://docs.djangoproject.com/en/1.11/ref/settings/#datetime-format
#
# DATE_FORMAT, DATETIME_FORMAT: a valid date or datetime filter string
# https://docs.djangoproject.com/en/1.11/ref/templates/builtins/#std:templatefilter-date
DATE_FORMAT = os.environ.get('DJANGO_DATE_FORMAT', 'j F, Y')
DATETIME_FORMAT = os.environ.get('DJANGO_DATETIME_FORMAT', 'j F, Y, P')
