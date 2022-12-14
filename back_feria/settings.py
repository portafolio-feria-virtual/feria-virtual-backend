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

ALLOWED_HOSTS = ["127.0.0.1","localhost"]

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
    "Apps.reportes",

    # Aplicaciones utilitarias
    "corsheaders",
    "rest_framework",
    "django_rest_passwordreset",
    "drf_spectacular",
    "django_celery_beat",


    


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

LANGUAGE_CODE = 'es-CL'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
    'rest_framework.permissions.IsAuthenticated'],

    "DEFAULT_AUTHENTICATION_CLASSES": ["rest_framework.authentication.SessionAuthentication"],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    
    }


SPECTACULAR_SETTINGS = {
        'TITLE': 'FeriaVirtualMaipoGrande API',
        'DESCRIPTION': 'Documentación de los Endpoints pertenecientes a la aplicación de Feria Virtual Maipo Grande',
        'VERSION': '1.0.0',
        'SERVE_INCLUDE_SCHEMA': False,
                'COMPONENT_SPLIT_REQUEST': True
        # OTHER SETTINGS
    }

#Celery, Celery Beat and Redis settings
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER", "redis://redis:6379")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_BACKEND", "redis://redis:6379")
if CELERY_RESULT_BACKEND == 'django-db':
    INSTALLED_APPS += ['django_celery_results',]
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'America/Santiago'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'




#Configuracion CORS
#

CORS_ALLOWED_ORIGINS = ['http://localhost:3000','http://localhost:5173','https://portafolio-frontend.onrender.com',"http://127.0.0.1:5501"]
#CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ('content-disposition', 'accept-encoding',
                      'content-type', 'accept', 'origin', 'authorization')


#Configuracion CSRF
#
CSRF_TRUSTED_ORIGINS = ['http://localhost:3000','http://localhost:5173','https://portafolio-frontend.onrender.com']

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/



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

#Configuracion correo

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

if DEBUG:
    EMAIL_HOST_USER += env("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD += env("EMAIL_HOST_PASSWORD")
else:
    EMAIL_HOST_USER += os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD += os.environ.get("EMAIL_HOST_PASSWORD")




# Configuración Firebase Storage
'''
TODO: añadir estos campos como requisito del archivo env, por ahora estan escritos en el archivo views de productor para facilidad de uso

API_KEY = env("API_KEY")
DOMAIN = env("DOMAIN")
PROJECT_ID = env("PROJECT_ID")
BUCKET = env("BUCKET")
SENDER_ID= env("SENDER_ID")
APP_ID = env("APP_ID")
MEASUREMENT_ID = env("MEASUREMENT_ID")
DATABASE_URL = env("DATABASE_URL")
'''