"""
Django settings for redcross project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

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
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret('IMS_DEV_SECRET')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['arceny.ulstercorps.org',
                 'www.arceny.ulstercorps.org',]


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
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# add request so we can access request url in 404 handler page
TEMPLATE_CONTEXT_PROCESSORS = (
"django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"django.core.context_processors.request"
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

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL='/accounts/login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = '/home3/ulsterc3/public_html/arc/eny/static'
MEDIA_ROOT = '/home3/ulsterc3/public_html/arc/eny/uploads'
MEDIA_URL = '/uploads/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home3/ulsterc3/Rob/python27/lib/python2.7/site-packages/ims/static',
)

LOG_FILE=os.path.join(BASE_DIR, 'ims_dev.log')

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates'),
                '/home3/ulsterc3/Rob/python27/lib/python2.7/site-packages/ims/templates',]
# DJANGO_LOG_LEVEL=DEBUG
# # Logging setup
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'redcross.log'),
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers':['file'],
#             'propagate': True,
#             'level':'DEBUG',
#         },
#         'ims': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#         },
#     }
# }
