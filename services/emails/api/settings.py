import os
from pathlib import Path
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure--z+(i3vahs9$t*u=tfk40l&7k+0y3xuq4^!jsy5%mkyliy0u56'

DEBUG = True

ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
	'rest_framework',
	'api'

]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api.urls'

WSGI_APPLICATION = 'api.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES = {
# 	'default': {
# 		'ENGINE': 'djongo',
# 		'NAME': 'emails',
# 		'HOST': 'mongod',
# 		'PORT': 27017
# 	}
# }

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
	'UNAUTHENTICATED_USER': None
}

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = "587"
EMAIL_HOST_USER = "logformat4@gmail.com"
EMAIL_HOST_PASSWORD = "logformat444"
EMAIL_USE_TLS = True
