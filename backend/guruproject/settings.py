""" django 4.1.3 """
from split_settings.tools import include
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

include(
    'components/auth_password_validators.py',
    'components/installed_apps.py',
    'components/middleware.py',
    'components/tempates.py',
    'components/databases.py',
) 

DEBUG = True
ALLOWED_HOSTS = ["*"]
SECRET_KEY = os.environ.get('SECRET_KEY', default=None),

BASE_DIR = Path(__file__).resolve().parent.parent
ROOT_URLCONF = 'guruproject.urls'
WSGI_APPLICATION = 'guruproject.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'