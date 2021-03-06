import os
from kavik.settings import BASE_DIR

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

SECRET_KEY = ''


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Basic auth user/pass
BASIC_USER = ''
BASIC_PASS = ''

EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = 'no-reply@klatrerosen.no'
REGISTER_FROM_MAIL = DEFAULT_FROM_EMAIL
EMAIL_PORT = 25
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # real
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # prints
