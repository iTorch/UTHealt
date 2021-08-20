import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'uthealt',
        'USER' : 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : '3306',
        'OPTIONS' : {
            'sql_mode' : 'traditional',
        }
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uthealt',
        'USER': 'postgres',
        'PASSWORD': '1598753',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}