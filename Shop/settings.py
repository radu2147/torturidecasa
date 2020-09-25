"""
Django settings for Shop project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import django_heroku
from django.conf.global_settings import FILE_CHARSET

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ua(44@*9n_j$76()$_)^iuimiex6n%i3&e8gl&^lku_%px*%z6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['radu2147.pythonanywhere.com', 'localhost', '127.0.0.1']

FILE_CHARSET = 'utf-8'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'HomePage',
    'Social',
    'Personalize',
    'allauth',
    'allauth.account',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount',
    'cloudinary_storage',
    'cloudinary',
    'User',
    'Cart',
    'Comm'
    
]
AUTH_USER_MODEL = 'User.CustomUser'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates', 'accounts'), os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'social_django.context_processors.backends',  # this
                'social_django.context_processors.login_redirect',  # and this
            ],
        },
    },
]

WSGI_APPLICATION = 'Shop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd85dqp5vks1ki5',
        'USER': 'wkivhetloypnzv',
        'PASSWORD': '5aae610bec4b02d786d04986c9a8f8e3990dd2450b02758b049ffc449aafe76d',
        'HOST': 'ec2-52-22-216-69.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'htrlerdoj',
    'API_KEY': '552147323933463',
    'API_SECRET': 'h9ecPuLUFs1TXxMdqF8_BMOToNU',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4'}}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_SIGNUP_FORM_CLASS = 'User.forms.RegisterForm'

SERVER_EMAIL = 'radudjango@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_PASSWORD ='dovle2147'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'radudjango@gmail.com'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

LOGIN_REDIRECT_URL = "/clean"

LOGIN_URL = '/accounts/login'


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

SOCIAL_AUTH_FACEBOOK_KEY = '1359884140887669'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET ='af1fc61c96064370729d5a1f7b7d1b13' #app key

django_heroku.settings(locals())