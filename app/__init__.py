from flask import Config, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

from app import routes