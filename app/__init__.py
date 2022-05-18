import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint


app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)

bp = Blueprint('routes', __name__)




