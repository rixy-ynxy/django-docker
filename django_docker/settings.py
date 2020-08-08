import os
from django.contrib.messages import constants as messages

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 's_6n_1tbb75j=%p02hv)zas39tip6#rlpr$!u!&wxofp2h*a64'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'diary.apps.DiaryConfig',
    'accounts.apps.AccountsConfig',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', 
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

ROOT_URLCONF = 'django_docker.urls'

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

WSGI_APPLICATION = 'django_docker.wsgi.application'


DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django_docker',
    'USER': os.environ.get('DB_USER'),
    'HOST': 'db',
    'POST': 33306
  }
}


AUTH_USER_MODEL = 'accounts.CustomUser'

SITE_ID = 1

AUTHENTICATION_BACKENDS = (
  'allauth.account.auth_backends.AuthenticationBackend',
  'django.cotrib.auth.backends.ModelBackend',
)

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USERNAME_REQUIRED = False

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

LOGIN_REDIRECT_URL = 'diary:diary_list'
ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

ACCOUNT_LOGOUT_ON_GET = True

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


LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_DIRS = (
  os.path.join(BASE_DIR, 'static'),
)

MESSAGE_TAGS = {
    messages.ERROR: 'alert alert-danger',
    messages.WARNING: 'alert alert-warning',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}

MEDIA_URL = '/media/'
MEDIA_ROOT = (
  os.path.join(BASE_DIR, 'media'),
)
