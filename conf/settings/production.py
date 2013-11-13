
import dj_database_url

from .base import *


DATABASES['default'] =  dj_database_url.config()

# Allow all host headers
ALLOWED_HOSTS = ['*']