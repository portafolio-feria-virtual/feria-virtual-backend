from pathlib import Path
import os
import dj_database_url
import environ

# inciailización de variables de entorno

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-svv6v0rfjwv76zacd$v@jmalcu%rqt97!y4-yrppg8z=c%3_)7'
SECRET_KEY = os.environ.get('SECRET_KEY', default=env("SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = ["127.0.0.1",]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


AUTH_USER_MODEL = 'cuentas.UserAccount'
ACCOUNT_UNIQUE_EMAIL = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #Aplicaciones creadas por equipo

    'Apps.cuentas',
    'Apps.administrador',
    'Apps.comercianteExtranjero',
    'Apps.comercianteLocal',
    'Apps.consultor',
    'Apps.productor',
    'Apps.transportista',
    "Apps.serviciosInternos",

    # Aplicaciones utilitarias
    "corsheaders",
    "rest_framework",


    


]



MIDDLEWARE = [
    # Modulo de Cors
  
    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    
    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'back_feria.urls'

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

WSGI_APPLICATION = 'back_feria.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default':  dj_database_url.config(
        default=f'postgres://{env("DATABASE_USER")}:{env("DATABASE_PASS")}@localhost:{env("DATABASE_PORT")}/{env("DATABASE_NAME")}',        conn_max_age=600  )
}
# DATABASES = {
#     'default':  dj_database_url.config(
#         default='sqlite://db.sqlite3',        conn_max_age=600  )
# }


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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated'],

    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.SessionAuthentication"]
    
    }





#Configuracion CORS
#

CORS_ALLOWED_ORIGINS = ['http://localhost:3000','http://localhost:5173','https://portafolio-frontend.onrender.com']
#CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


#Configuracion CSRF
#
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000','http://localhost:5173','https://portafolio-frontend.onrender.com']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# This setting tells Django at which URL static files are going to be served to the user.
# Here, they well be accessible at your-domain.onrender.com/static/...
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Following settings only make sense on production and may break development environments.
if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
