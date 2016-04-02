"""
Django settings for fiblist project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(*_DIR, ...)
import os

# /home/nick/dev/django/projects/fiblist
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))

# /home/nick/dev/django/projects/fiblist/source
SOURCE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__name__)))

# /home/nick/dev/django/projects/fiblist/source/fiblist/conf
CONF_DIR = os.path.dirname(os.path.dirname(__file__))

# /home/nick/dev/django/projects/fiblist/source/fiblist/conf/settings
SETTINGS_DIR = os.path.dirname(__file__)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(SOURCE_DIR, 'templates'),
)

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lists',
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

ROOT_URLCONF = 'fiblist.conf.urls'

WSGI_APPLICATION = 'fiblist.conf.wsgi.local.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'database/db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# static files
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(SOURCE_DIR, 'lists/static')
]

STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
