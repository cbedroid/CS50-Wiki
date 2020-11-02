
import os
import os
import mimetypes
import django_heroku
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = os.environ.get("WIKI_SECRET_KEY")
if not SECRET_KEY:
    raise TypeError("Invalid or Missing Secret Key")



DEBUG = (os.environ.get("WIKI_DEBUG") == "True")

Production = not DEBUG


if Production:
    ALLOW_HOST = ["cbedroid-wiki.herokuapp.com"]
else:  # Development
    ALLOWED_HOSTS = [ ]


# Application definition

INSTALLED_APPS = [
    "encyclopedia",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "wiki.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "wiki.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

if Production:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("WIKI_DB_NAME"),
            "USER": os.environ.get("WIKI_DB_USER"),
            "PASSWORD": os.environ.get("WIKI_DB_PASSWORD"),
            "HOST": os.environ.get("WIKI_DB_HOST"),
            "PORT": "5432",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = "/static/"
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
mimetypes.add_type("text/css", ".css", True)
django_heroku.settings(locals())
handler404 = "encyclopedia.views.handle_404"
