import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Create Flask application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'
# Create in-memory database
app.config['DATABASE_FILE'] = 'sample_db.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + app.config['DATABASE_FILE']
SQLALCHEMY_DATABASE_URI='sqlite:///:memory:'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)




