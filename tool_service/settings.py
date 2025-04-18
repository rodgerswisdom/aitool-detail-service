"""
For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
import dj_database_url
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_!c4&%oi8d$jl+#sbxgc=$#2l^#gl64v#ti%ianxk*n&lv!0vu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = []
# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['0.0.0.0','127.0.0.1', '.vercel.app', '.netlify.app']

#RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
#if RENDER_EXTERNAL_HOSTNAME:
    #    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
# ALLOWED_HOSTS = ['http://127.0.0.1:8000','aitool-detail-service.onrender.com','.onrender.com','https://tool-service.onrender.com','localhost']


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'tools',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # Whitenoise Middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",  # Add this if you use 'localhost' instead of '127.0.0.1'
    ".vercel.app",
    ".netlify.app",
]

CORS_ALLOW_ALL_ORIGINS = True

ROOT_URLCONF = 'tool_service.urls'

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

WSGI_APPLICATION = 'tool_service.wsgi.application'


# SQLite Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

"""
     Replace the SQLite DATABASES configuration with PostgreSQL:
"""

DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        # default='postgresql://postgres:postgres@localhost:5432/tool_service',
        # default='postgres://postgres:postgres@localhost:5432/tool_service_db',
       # default='postgresql://tool_service:aijTGjtjVhSnj0WhTZAy3MhEVSH87NIW@dpg-csbqt7btq21c73a6fit0-a.oregon-postgres.render.com/tool_service',
       default = 'postgresql://neondb_owner:u9eQLGR8xYSD@ep-lingering-dawn-a5oiytlk.us-east-2.aws.neon.tech/neondb?sslmode=require',
       conn_max_age=600
    )
}


# settings.py
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aitool_detail_service',
        'USER': 'ratego',
        'PASSWORD': 'ubuntu/2025',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

# STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#CATEGORY_SERVICE_URL = os.getenv('CATEGORY_SERVICE_URL', 'http://127.0.0.1:8001')
CATEGORY_SERVICE_URL = os.getenv('CATEGORY_SERVICE_URL', 'https://aitools-category-service.vercel.app')

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# The directory where collectstatic will collect static files for production
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# Enable WhiteNoise to serve static files in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# This production code might break development mode, so we check whether we're in DEBUG mode
"""
REFACTORING ADMIN STYLES
"""
# if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    # STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,  # Default page size
}

