'''
Default configuration
'''
from os import getenv


class Config(object):
    ENV = getenv('FLASK_ENV')
    DEBUG = ENV == 'development'
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}/{}'.format(
        getenv('USER_DB'), getenv('PWD'), getenv('HOST'), getenv('DB_NAME')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# 'mysql+pymysql://root:aarizat@localhost/projects_db' # os.getenv("DATABASE_URI")