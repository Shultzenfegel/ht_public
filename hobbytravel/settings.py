"""
Django settings for hobbytravel project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'htapp.apps.HtappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hobbytravel.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'htapp.context_processors.languages',
                'htapp.context_processors.currencies',
                'htapp.context_processors.user_forms',
            ],
        },
    },
]

WSGI_APPLICATION = 'hobbytravel.wsgi.application'


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

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_ROOT = BASE_DIR / 'upload'
MEDIA_URL = '/upload/'

STATIC_ROOT = BASE_DIR / 'static'
STATIC_URL = '/static/'


# Variables with environment values for production

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('WEB_DEBUG', default=1)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('WEB_SECRET_KEY', default='k&n4tnt*6-mb=i*0sd2bf0@&7t$5(191_*cw__0amz90m2q7mi')

ALLOWED_HOSTS = os.environ.get('WEB_ALLOWED_HOSTS', default='127.0.0.1').split(',')

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('WEB_DB_NAME', default='hobbytravel'),
        'USER': os.environ.get('WEB_DB_USER', default='hobbytravel_user'),
        'PASSWORD': os.environ.get('WEB_DB_PASSWORD', default='zBZjrLDka2mJ'),
        'HOST': os.environ.get('WEB_DB_HOST', default='127.0.0.1'),
        'PORT': os.environ.get('WEB_DB_PORT', default='5432'),
    }
}

CSRF_COOKIE_SECURE = bool(int(os.environ.get('WEB_CSRF_COOKIE_SECURE', default=0)))

SESSION_COOKIE_SECURE = bool(int(os.environ.get('WEB_SESSION_COOKIE_SECURE', default=0)))