import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    DATABASE_FILE='sqlite:///:memory:'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = DATABASE_FILE
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG=True
    SQLALCHEMY_ECHO=True