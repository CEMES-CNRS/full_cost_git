"""
Django settings for full_cost project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import ldap
from django_auth_ldap.config import LDAPSearch

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2f(m(f*l*z*atuz9sxe%9@^#qu*qn&3t!rsqv=4684%f71y!#q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = [('Seb', 'sebastien.weber@cemes.fr')]

ALLOWED_HOSTS = ['10.47.3.21', '127.0.0.1', 'full-cost.cemes.fr', 'localhost']

LOGIN_REDIRECT_URL = '/lab/logged/'

# Application definition

INSTALLED_APPS = [
    'osp.apps.OspConfig',
    'lab.apps.LabConfig',
    'met.apps.MetConfig',
    'prepa.apps.PrepaConfig',
    'fib.apps.FibConfig',
    'mphys.apps.MphysConfig',
    'chem.apps.ChemConfig',
    'imag.apps.ImagConfig',
    'fab.apps.FabConfig',
    'implant.apps.ImplantConfig',
    'engi.apps.EngiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_tables2',
    'django_filters',
    'bootstrap4',
    'crispy_forms',
    'simple_history',
    'post_office',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
]

ROOT_URLCONF = 'full_cost.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'lab.context_processors.get_all_activity',
            ],
        },
    },
]

WSGI_APPLICATION = 'full_cost.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'full_cost',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# LDAP configuration

AUTH_LDAP_GLOBAL_OPTIONS = {ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER, ldap.OPT_REFERRALS: 0}
AUTH_LDAP_CONNECTION_OPTIONS = AUTH_LDAP_GLOBAL_OPTIONS = {ldap.OPT_X_TLS_REQUIRE_CERT: ldap.OPT_X_TLS_NEVER, ldap.OPT_REFERRALS: 0}
AUTH_LDAP_SERVER_URI = "ldaps://ldap-slave1.cemes.fr"
AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=People,dc=cemes,dc=fr"
AUTH_LDAP_BIND_DN = ""
AUTH_LDAP_BIND_PASSWORD = ""
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    "ou=People,dc=cemes,dc=fr", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    }
AUTHENTICATION_BACKENDS = [
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
    ]


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = False

USE_L10N = False

USE_TZ = True

SHORT_DATE_FORMAT = 'd/m/Y'

DATE_FORMAT = 'j N Y'

SHORT_DATETIME_FORMAT = 'd/m/Y H:i'

SHORT_DATETIME_FORMAT = 'j N Y H:i'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    '/usr/lib/python3.6/site-packages/django/contrib/admin/static'
    ]


#emailing
EMAIL_BACKEND = 'post_office.EmailBackend'

EMAIL_HOST = 'bluemind.cemes.fr'
EMAIL_PORT = 25

EMAIL_FROM_EMAIL = 'christine.viala@cemes.fr'
