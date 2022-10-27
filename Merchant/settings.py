"""
Django settings for Merchant project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from decouple import config



# Image Cropping ...............!
from easy_thumbnails.conf import Settings as thumbnail_settings


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_thumbnails',
    'image_cropping',
    'adminapp',
    'account',
    'Products',
    'realshop',
    'cart_mangment',
    'orders',
    'payment',
    'wishlist',
    'razorpay',
    'paypal.standard.ipn',
]
THUMBNAIL_PROCESSORS = (
    'image_cropping.thumbnail_processors.crop_corners',
) + thumbnail_settings.THUMBNAIL_PROCESSORS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Merchant.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'orders.template_context.get_filters',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'Merchant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'KDandCO',
        'USER':'postgres',
        'PASSWORD':'1998',
        'HOST':'localhost',
    }
}







# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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



# !..................SINGLE SIGN ON.......................!

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)





AUTH0_DOMAIN = config('AUTH0_DOMAIN')
AUTH0_CLIENT_ID = config('AUTH0_CLIENT_ID')
AUTH0_CLIENT_SECRET = config('AUTH0_CLIENT_SECRET')







# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

TIME_ZONE = 'Asia/Kolkata'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
MEDIA_URL ='/'
MEDIA_ROOT=os.path.join(BASE_DIR,'media')

AUTH_USER_MODEL = "account.CustomUser"

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ACCOUNT_SID = config('ACCOUNT_SID')
AUTH_TOKEN = config('AUTH_TOKEN')
COUNTRY_CODE='+91'
TWILIO_PHONE_NUMBER= config('TWILIO_PHONE_NUMBER')






# RAZORPAY KEY_ID AND SECRET_KEY
RAZOR_KEY_ID = config('RAZOR_KEY_ID')
RAZOR_KEY_SECRET = config('RAZOR_KEY_SECRET')



#...PAYPAL......CONFIG...!
PAYPAL_RECEIVER_EMAIL = config('PAYPAL_RECEIVER_EMAIL')
PAYPAL_TEST = True



# email configs
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')