from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Agregar para mejor debugging en desarrollo
INTERNAL_IPS = [
    "127.0.0.1",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [BASE_DIR / 'static']

# Deshabilitar algunas configuraciones de seguridad en desarrollo
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Agregar después de DEBUG
DEVELOPMENT = True

# Agregar configuración de email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Configuración de caché para desarrollo
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
