from .base import *  # noqa type:ignore

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o7%k=z)w$5n^!ejzdv-d9!-q)#15m%%(ir_e+bj1-#vy=d9%jf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
  "127.0.0.1",
    "localhost",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db_dev.sqlite3',
    }
}

MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")
INSTALLED_APPS += ("debug_toolbar",)  # and other apps for local development

INTERNAL_IPS = [
    "127.0.0.1",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "../static/media/"