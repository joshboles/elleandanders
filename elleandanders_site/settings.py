import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
ADMINS = [
    ("Josh Boles", "jaboles@gmail.com"),
]

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'no.db',
    }
}

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False

TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
]

SEND_BROKEN_LINK_EMAILS = True
APPEND_SLASH = True
PREPEND_WWW = False
USE_ETAGS = True
        

MIDDLEWARE_CLASSES = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'derpitude'
    }
}
CACHE_MIDDLEWARE_ALIAS = "default"
CACHE_MIDDLEWARE_SECONDS = 1
CACHE_MIDDLEWARE_KEY_PREFIX = "servelocally_org"

ROOT_URLCONF = 'elleandanders_site.urls'

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
]

INSTALLED_APPS = [
    
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

try:
    from local_settings import *
except ImportError:
    pass
