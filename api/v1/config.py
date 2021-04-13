'''
Default configuration
'''
import os


class Config(object):
    ENV = os.getenv("FLASK_ENV")
    DEBUG = ENV == "development"
    SECRET_KEY = 'gues me!'  # os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:aarizat@localhost/projects_db' # os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

