from pathlib import Path

from dotenv import load_dotenv
import os
load_dotenv()


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get("SECRET_KEY")


DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")


INSTALLED_APPS = [
          'jazzmin',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'api'

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

ROOT_URLCONF = 'api.urls'

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
            ],
        },
    },
]



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



STATIC_URL = 'static/'

#STATICFILES_DIRS=[BASE_DIR.joinpath("static")]
STATIC_ROOT = BASE_DIR / 'static'

MEDIA_URL = 'media/'
MEDIA_ROOT  = BASE_DIR.joinpath('media')

#####  emails
####
