from cattery.settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'catterydb',
        'USER': 'catterydb',
        'PASSWORD': 'cattery147852963.',
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static') #canlya atarken burayı aç yukarısını kapat