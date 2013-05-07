from ..import *

DATABASES = {
    'default': {
        #INSERT YOUR LOCAL DATABASE SETTINGS HERE
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}

WSGI_APPLICATION = 'pedal.settings.local.wsgi.application'


ROOT_URLCONF = 'pedal.settings.local.urls'

STATICFILES_DIRS += (
    os.path.join(PROJECT_ROOT, 'media'),
)
INSTALLED_APPS += (
    'devserver',
)
DEVSERVER_TRUNCATE_SQL = False
