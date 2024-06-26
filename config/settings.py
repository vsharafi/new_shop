"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n0(+)0^qtln_za(hbn5&j7#$_+nr!#$qc6yam@x478y=ya7h-7'

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
    'django.contrib.humanize',

    # third party apps
    'jalali_date',
    'crispy_forms',
    'crispy_bootstrap5',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rosetta',
    'ckeditor',


    # my app
    'accounts',
    'pages',
    'products',
    'cart',
    'orders.apps.OrdersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Add the account middleware:
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` needs this from django
                'django.template.context_processors.request',

                # Custom Context Processors
                'cart.context_processors.cart'
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]


WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql',
	        'NAME': 'new_shop',
	        'USER': 'postgres',
	        'PASSWORD': 'postgres',
	        'HOST': 'localhost',
	        'PORT': 5432,
	    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

#LANGUAGE_CODE='en-us'
LANGUAGE_CODE='fa'
#TIME_ZONE='UTC'
Time_Zone='Asia/Tehran'
USE_I18N=True
USE_L10N=True
USE_TZ=True
LOCALE_PATHS = (BASE_DIR.joinpath('products/locale'), BASE_DIR.joinpath('templates/locale'), BASE_DIR.joinpath('accounts/locale'))
LANGUAGES = [('en', 'English'), ('fa', 'Persian'),]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIR = [
    str(BASE_DIR.joinpath('static'))
]

STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# accounts config

AUTH_USER_MODEL = 'accounts.CustomUser'
LOGIN_REDIRECT_URL = 'product_list'
LOGOUT_REDIRECT_URL = 'product_list'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
ACCOUNT_EMAIL_REQUIRED = False

# crispy forms config
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"


from django.contrib import messages
# messages tags:
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# Cover Image configs
MEDIA_URL='/media/'
	
MEDIA_ROOT=str(BASE_DIR.joinpath('media'))