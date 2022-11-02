from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': os.environ.get('DB_ENGINE', default='django.db.backends.postgresql'),
#         'NAME': os.environ.get('DB_NAME', default=None),
#         'USER': os.environ.get('POSTGRES_USER', default=None),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD', default=None),
#         'HOST': os.environ.get('DB_HOST', default=None),
#         'PORT': os.environ.get('DB_PORT', default=None)
#     }
# }