import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{user}:{passwd}@db:5432/{db}'.format(
        user=os.environ.get('DBUSER'),
        passwd=os.environ.get('DBPASS'),
        db=os.environ.get('DBNAME'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG=True
    SQLALCHEMY_ECHO=True