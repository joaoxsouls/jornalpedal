from .. import *

DATABASES = {
    'default': {
        #insert your live settings here
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}
WSGI_APPLICATION = 'pedal.settings.live.wsgi.application'

#uncomment this if you want to use sentry
#INSTALLED_APPS += (
#     'raven.contrib.django.raven_compat',
# )
# RAVEN_CONFIG = {
#     'dsn': 'sentry url',
# }
# MIDDLEWARE_CLASSES += (
#     'raven.contrib.django.middleware.Sentry404CatchMiddleware',
# )

DEBUG = False

STATIC_ROOT = ''
STATIC_URL = ''

MEDIA_ROOT = ''
MEDIA_URL = ''

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
