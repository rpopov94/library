import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin

from config import Config



app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
admin = Admin(app, name='microblog', template_mode='bootstrap3')
app.config.from_object(Config)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql+psycopg2://{user}:{passwd}@db:5432/{db}'.format(
        user=os.environ.get('DBUSER'),
        passwd=os.environ.get('DBPASS'),
        db=os.environ.get('DBNAME'))

from app import routes