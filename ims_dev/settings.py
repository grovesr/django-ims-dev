"""
Django settings for redcross project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from django.core.exceptions import ImproperlyConfigured
import os
import json
import re
try:
    from . import VERSION as SITE_VERSION # used in templates to display site version
    SITE_VERSION = SITE_VERSION[0]
except ImportError:
    SITE_VERSION = ''
try:
    from ims import VERSION as IMS_VERSION # used in templates to display ims version
    IMS_VERSION=IMS_VERSION[0]
except ImportError:
    IMS_VERSION=''
from getpass import getuser

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_NAME = BASE_DIR.rsplit(os.sep,1)[-1]
# JSON secrets module
with open(os.path.join(BASE_DIR, '.ims_dev_secret.json')) as f:
    secrets=json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """
    get the secret setting or return explicit exception
    """
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable in the secret file".format(setting)
        raise ImproperlyConfigured(error_msg)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

PICTURE_SIZE = 600
THUMBNAIL_SIZE = 90
PAGE_SIZE = 20

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('IMS_DEV_SECRET')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['.imsdev.ulstercorpsdev.org',
                 'localhost',
                 '127.0.0.1',]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ims',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
                 os.path.join(BASE_DIR, 'templates'),
                 '/home/grovesr/.virtualenvs/rims-django1.9/local/lib/python2.7/site-packages/ims/templates',
                 #'ims/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug':DEBUG,
            'context_processors': [
                #add request so we can access request url in 404 handler page:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                "django.template.context_processors.request",
            ],
        },
    },
]

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

ROOT_URLCONF = 'ims_dev.urls'

WSGI_APPLICATION = 'ims_dev.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': get_secret('IMS_DEV_DB'),
        'USER': get_secret('IMS_DEV_DB_USER'),
        'PASSWORD': get_secret('IMS_DEV_DB_PASS'),
        'HOST': 'localhost',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Eastern'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL='/login/'
LOGIN_REDIRECT_URL = '/'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
]
#
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = get_secret('IMS_DEV_EMAIL_HOST')
EMAIL_PORT = int(get_secret('IMS_DEV_EMAIL_PORT'))
EMAIL_HOST_USER = get_secret('IMS_DEV_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_secret('IMS_DEV_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = eval(get_secret('IMS_DEV_EMAIL_USE_TLS'))
EMAIL_USE_SSL = eval(get_secret('IMS_DEV_EMAIL_USE_SSL'))
SERVER_EMAIL = get_secret('IMS_DEV_EMAIL_FROM_USER')
DEFAULT_FROM_EMAIL = SERVER_EMAIL


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/var/www/html/ims/dev/static_root'
MEDIA_ROOT = '/var/www/html/ims/dev/uploads'
#MEDIA_ROOT = os.path.join(BASE_DIR,'uploads')
MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'

TEMP_DIR = '/tmp'

# SITE_ADMIN will display as contact person on each page
SITE_ADMIN = ('Rob Groves','robgroves0@gmail.com')
# add other admins if you like to be contacted in case of errors
ADMINS = (SITE_ADMIN,)

SITE_MANAGER = ('Rob Groves','robgroves0@gmail.com')
# managers get notified of 404 errors and possibly other minor iussues
MANAGERS = (SITE_MANAGER,)
EMAIL_SUBJECT_PREFIX = '[IMS-DEV]'

DJANGO_LOG_FILE=os.path.join(BASE_DIR, 'log/' + getuser()+ '_django.log')
IMS_LOG_FILE=os.path.join(BASE_DIR, 'log/' + getuser()+ '_ims.log')
LOG_FILES= (
            DJANGO_LOG_FILE,
            IMS_LOG_FILE,
            )


IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)
# Logging setup
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
                   'verbose': {
                               'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                               'datefmt' : "%d/%b/%Y %H:%M:%S"
                               },
                   'simple': {
                              'format': '%(levelname)s %(message)s'
                              },
                   },
    'handlers': {
                 'django_file': {
                          'level': 'INFO',
                          'class': 'logging.handlers.RotatingFileHandler',
                          'filename': DJANGO_LOG_FILE,
                          'formatter': 'verbose',
                          'maxBytes':1048576,
                          'backupCount':10,
                          },
                 'ims_file': {
                                  'level': 'DEBUG',
                                  'class': 'logging.handlers.RotatingFileHandler',
                                  'filename': IMS_LOG_FILE,
                                  'formatter': 'verbose',
                                  'maxBytes':1048576,
                                  'backupCount':10,
                                  },
                 'mail_admins': {
                                 'level': 'ERROR',
                                 'class': 'django.utils.log.AdminEmailHandler',
                                 'include_html': True,
                                 }
                 
                 },
    'loggers': {
                'django': {
                           'handlers':['django_file','mail_admins',],
                           'propagate': True,
                           'level':'DEBUG',
                           },
                'ims': {
                           'handlers':['ims_file','mail_admins',],
                           'propagate': False,
                           'level':'DEBUG',
                           },
                }
}
