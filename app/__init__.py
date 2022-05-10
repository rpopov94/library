from flask import Config, Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

from app import routes