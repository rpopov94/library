import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    # DATABASE_FILE='sqlite:///:memory:'
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'sqlite:///data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '123456790'
    SQLALCHEMY_ECHO = True