from cattery.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cattrydb',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static') #canlya atarken burayı aç yukarısını kapat