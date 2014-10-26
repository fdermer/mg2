from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__)) #'/Users/Fred/www/mg2/mg2'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__)) #'/Users/Fred/www/mg2/mg2/mg2'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i4d8p52pr$!5bsc4oxw82fsadz=#!x)bdx1qsn(7w01u8%s7k_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


STATIC_ROOT = os.path.join(SITE_ROOT, "static")
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    #    "django.contrib.staticfiles.finders.DefaultStorageFinder",
    #"compressor.finders.CompressorFinder",
    )

TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
    )

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    )


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'recipe',
    'pagination',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)

ROOT_URLCONF = 'mg2.urls'

WSGI_APPLICATION = 'mg2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


##from local_settings import ENABLE_DEBUG_TOOLBAR
#ENABLE_DEBUG_TOOLBAR = True
#if ENABLE_DEBUG_TOOLBAR:
#    MIDDLEWARE_CLASSES += (
#        "debug_toolbar.middleware.DebugToolbarMiddleware",
#        )
#
#    INSTALLED_APPS += (
#        "debug_toolbar",
#        )
#
#    DEBUG_TOOLBAR_CONFIG = {
#        "INTERCEPT_REDIRECTS": False
#    }