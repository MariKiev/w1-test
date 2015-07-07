import os

SECRET_KEY = os.environ.get('SECRET_KEY')
DB_URL = os.environ.get('DATABASE_URL')

try:
    from local_settings import *
except ImportError:
    pass