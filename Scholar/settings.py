"""
Django settings for Scholar project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+x4!f602mag83_ul4jez)x$h+bh^&#dh51x@ow(s3@1u@46-g6'

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = True

# ALLOWED_HOSTS = []

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'fptscholar.azurewebsites.net']

import logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'register',
    'article',
    'storages',
    'django_filters',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Scholar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'Scholar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



# DATABASES = {
#     'default': {
#         'ENGINE': 'sql_server.pyodbc',
#         'NAME': 'testData',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': 'DESKTOP-EF058DF',
#         'PORT': '',
#         'OPTIONS': {
#             'unicode_results':True,
#             'extra_params': 'ClientCharset=utf8',
#             'driver': 'ODBC Driver 17 for SQL Server',
#         },
#     },
# }

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'dataScholar',
        'USER': 'giakinh0823',
        'PASSWORD': 'Danhancach0823',
        'HOST': 'tcp:database-giakinh.database.windows.net',
        'PORT': '',
        'OPTIONS': {
            'unicode_results':True,
            'extra_params': 'ClientCharset=utf8',
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
}

# set this to False if you want to turn off pyodbc's connection pooling
# DATABASE_CONNECTION_POOLING = False

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/




# MEDIA_URL = '/media/'



# DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
# STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'


AZURE_ACCOUNT_NAME = 'giakinh'
AZURE_ACCOUNT_KEY = 's4PvaBqtyGwMpUCn5VbQ8EzjpYMVf2yMD+Sf26y0IO3Ei7EqT0+AaUumTSENR2JVnFYUF0x60sWke+uZ1TIMYg=='



STATICFILES_STORAGE = 'storages.backends.azure_storage.AzureStorage'
DEFAULT_FILE_STORAGE = 'Scholar.custom_azure.AzureMediaStorage'

STATIC_LOCATION = "static"
MEDIA_LOCATION = "http://{AZURE_ACCOUNT_NAME}.blob.core.windows.net/media"

MEDIA_ROOT='http://{AZURE_ACCOUNT_NAME}.blob.core.windows.net'

AZURE_CUSTOM_DOMAIN = f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
# AZURE_LOCATION=f'{AZURE_ACCOUNT_NAME}.blob.core.windows.net'
AZURE_LOCATION = 'sqldbauditlogs'
AZURE_CONTAINER = 'sqldbauditlogs'
STATIC_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
MEDIA_URL = f'https://{AZURE_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    STATIC_DIR,
]


LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = 'index'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_POST = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
