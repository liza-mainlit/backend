from datetime import timedelta
from pathlib import Path
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(BASE_DIR / "django_core" / ".env")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "fzxUxspoPbJsJqm9xDgpFvHte7xa0vyZkhP6N4x8"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", False)

ALLOWED_HOSTS = ["*"]

# Application definition

DJANGO_APPS = [
    "constance",  # Needs to be placed before jazzmin
    "jazzmin",  # Needs to be placed before django.contrib.admin
    "filebrowser",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:1337",
    "http://127.0.0.1:1337",
    "http://89.108.70.118:1337",
    "http://89.108.70.118",
    "https://aim.club",
    "http://194.67.67.200",     # dev server
    "http://194.67.67.200:3000"
]

THIRD_PARTY_APPS = [
    "ckeditor",
    "corsheaders",
    "drf_spectacular",
    "djoser",
    "rest_framework",
    "django_filters",
    "tinymce",
    "constance.backends.database",
    "import_export",
    "colorfield",
]

LOCAL_APPS = [
    "users",
    "news",
    "subscriptions",
    "contacts",
    "marketplaces",
    "tags",
    "storage",
    "registration_on_event",
    "info",
    "laboratories",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

AUTH_USER_MODEL = "users.User"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "django_core.urls"

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

WSGI_APPLICATION = "django_core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env.str("POSTGRES_DB"),
        "USER": env.str("POSTGRES_USER"),
        "PASSWORD": env.str("POSTGRES_PASSWORD"),
        "HOST": env.str("POSTGRES_HOST"),
        "PORT": env.str("POSTGRES_PORT"),
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

# CORS headers
# https://pypi.org/project/django-cors-headers/

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://194.67.67:3000",
    "http://localhost:3002",
]

CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]

CORS_ALLOW_CREDENTIALS = True

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "ru-ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_L10N = True

USE_TZ = True

CONN_MAX_AGE = None

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
MEDIA_ROOT = BASE_DIR / "media/"
MEDIA_URL = "/media/"


# Rest Framework

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
}


# SECURITY

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "SAMEORIGIN"
USE_HTTPS_STORAGE = env.bool("USE_HTTPS_STORAGE", False)

if env.bool("USE_HTTPS", False):
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    USE_HTTPS_STORAGE = True

# DRF Spectacular

SPECTACULAR_SETTINGS = {
    "TITLE": "AIM Django REST API",
    "DESCRIPTION": "AIM Django REST API",
    "VERSION": "0.0.1",
}


# Djoser

DJOSER = {
    "TOKEN_MODEL": None,  # We use only JWT
    "HIDE_USERS": True,
}


# Simple JWT

SIMPLE_JWT = {"ROTATE_REFRESH_TOKENS": True}

if DEBUG:
    SIMPLE_JWT.update(
        {
            "ACCESS_TOKEN_LIFETIME": timedelta(days=365),
            "REFRESH_TOKEN_LIFETIME": timedelta(days=366),
        }
    )


# Constance
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_CONFIG = {
    "EMAIL": ("", "Адрес электронной почты"),
    "PHONE_NUMBER": ("", "Номер телефона"),
    "VK_URL": ("", "Ссылка на VK"),
    "TELEGRAM_URL": ("", "Ссылка на Telegram"),
    "YOUTUBE_URL": ("", "Ссылка на YouTube"),
    "MARKETPLACE_ORDER": ("", "Почта, на которую отправляются сообщения"),
    "MARKETPLACE_PAGE_HEADER": ("", "Заголовок страницы Интеллектуальных решений"),
}

# Jazzmin

JAZZMIN_SETTINGS = {
    "hide_apps": ("auth", "users", "filebrowser"),
    "site_title": "AIM club",
    "site_header": "AIM club",
    "site_brand": "AIM club",
    "custom_css": "storage/css/filebrowser_edited.css"  # FIXME: разобраться
}


# Sentry
# ------------------------------------------------------------------------------
if env.bool("USE_SENTRY", False):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import ignore_logger

    SENTRY_DSN = env("SENTRY_DSN")
    integrations = [DjangoIntegration()]
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=integrations,
    )

    ignore_logger("django.security.DisallowedHost")

# Filebrowser
FILEBROWSER_DIRECTORY = "uploaded_files/"
ABSOLUTE_FILEBROWSER_DIR = MEDIA_ROOT / FILEBROWSER_DIRECTORY
if not ABSOLUTE_FILEBROWSER_DIR.exists():
    ABSOLUTE_FILEBROWSER_DIR.mkdir(parents=True, exist_ok=True)

# TinyMCE

TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": True,  # Changed from default
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
    "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
    "code,help,wordcount",
    "toolbar": "undo redo | formatselect | "
    "bold italic backcolor | alignleft aligncenter "
    "alignright alignjustify | bullist numlist outdent indent | "
    "removeformat | help",
}

# todo: create env vars
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = env.str('EMAIL_HOST')
# EMAIL_PORT = env.int('EMAIL_PORT')
# EMAIL_USE_SSL = env.bool('EMAIL_USE_SSL')
# EMAIL_HOST_USER = env.str('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD')

# Celery conf
REDIS_HOST = env.str("REDIS_HOST", "redis")
REDIS_PORT = env.str("REDIS_PORT", "6379")
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", f"redis://{REDIS_HOST}:{REDIS_PORT}/0")
CELERY_RESULT_BACKEND = env.str(
    "CELERY_BROKER_BACKEND", f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
)
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Shanghai"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}

# CKEditor conf
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor', 'Format',
             '-', 'Maximize',
             '-', 'Table', 'Image',
             '-', 'Source',
             '-', 'NumberedList', 'BulletedList'
            ],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
             '-', 'Font', 'FontSize', 'TextColor',
             '-', 'Outdent', 'Indent',
             '-', 'HorizontalRule', 'Blockquote'
            ]
        ]
    }
}


DATA_UPLOAD_MAX_NUMBER_FIELDS = None
