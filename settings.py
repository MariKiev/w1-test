import os

SECRET_KEY = os.environ.get('SECRET_KEY')

try:
    from local_settings import *
except ImportError:
    pass