'''
Default configuration
'''
from os import getenv


class Config(object):
    ENV = getenv('FLASK_ENV')
    DEBUG = ENV == 'development'
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        getenv('DB_USER'), getenv('DB_PWD'), getenv('DB_HOST'),
        getenv('DB_NAME')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
