from decouple import config
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EKKPASS_BASE_URL = config('EKKPASS_BASE_URL', '127.0.0.1')

DASHBOARD_SECRET = 'e77248431da41a6ec096469592871cdd108fc369dk77248431da41a6ec096469592871cdd108fc369dk'

SECRET_KEY = 'EKKBAZ2015BUSINESSBLOCKCHAINSMARTCONTRACTEKKBAZ'

# SECURE_SSL_REDIRECT = False

# AUTH = 'https://dapi.ekkbaz.com/auth/v4/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

ALLOWED_HOSTS = ["*"]

# ALLOWED_HOSTS = [
#     'localhost:8000',
#     '127.0.0.1:8000',
#     '18.136.144.107',
#     '172.18.0.6',
#     'ekkpay.ekkbaz.com',
#     'ekkpay-dev.ekkbaz.com',
#     'dpay.ekkbaz.com',
#     'ekkpay-stage.ekkbaz.com',
#     'saepayp2.azurewebsites.net'
# ]

APPEND_SLASH = False

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'app_origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'dashboard-secret',
#     'content-type',
#     'dnt',
#     'origin',
#     'app_origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# )

# Application definition

INSTALLED_APPS = [
    # 'behave_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    
    # 'drf_yasg',
    # 'drf_spectacular',
    # 'drf_spectacular_sidecar',

    # 'oauth2_provider',
    # 'rest_framework_simplejwt',
    'rest_framework',
    # 'rest_framework_swagger',
    'rest_framework.authtoken',
    
    'import_export',

    'apps.posts',
    # 'apps.product',
    'apps.charliauth',

    # 'silk',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    "corsheaders.middleware.CorsPostCsrfMiddleware",
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'silk.middleware.SilkyMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': config('DB_ENGINE'),
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_LOCAL_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data/db.sqlite3',
    }
}

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'public/staticfiles'

STATICFILES_DIRS = (BASE_DIR / 'static', )

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'public/media'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.BasicAuthentication',
        
        # 'rest_framework_simplejwt.authentication.JWTStatelessUserAuthentication',
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        # 'rest_framework.permissions.IsAuthenticated',

    ]
}




# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=10),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'UPDATE_LAST_LOGIN': False,

#     'ALGORITHM': 'HS256',
#     'SIGNING_KEY': SECRET_KEY,
#     'VERIFYING_KEY': None,
#     'AUDIENCE': None,
#     'ISSUER': None,
#     'JWK_URL': None,
#     'LEEWAY': 0,

#     'AUTH_HEADER_TYPES': ('Bearer',),
#     'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
#     'USER_ID_FIELD': 'id',
#     'USER_ID_CLAIM': 'user_id',
#     'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
#     'TOKEN_TYPE_CLAIM': 'token_type',
#     'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

#     'JTI_CLAIM': 'jti',

#     'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
#     'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
#     'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
# }
