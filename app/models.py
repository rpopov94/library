from app import db, login_manager, app
from flask import Flask, url_for, redirect, render_template, request, abort
from flask_admin.contrib import sqla
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    def __str__(self):
        return self.email


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

class BlobMixin(object):
    mimetype = db.Column(db.Unicode(length=255), nullable=False)
    filename = db.Column(db.Unicode(length=255), nullable=False)
    blob = db.Column(db.LargeBinary(), nullable=False)
    size = db.Column(db.Integer, nullable=False)

class Book(db.Model, BlobMixin):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.String(64))
    name = db.Column(db.String(64), index=True, unique=True)
    publisher = db.Column(db.String(64), index=True, unique=True)
    year = db.Column(db.Integer)
    level = db.relationship('Level', backref='book', lazy='dynamic')
    tag = db.relationship("Tag", backref='books', secondary=tags, lazy="dynamic")
    book_file  = db.Column(db.LargeBinary)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class Level(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    level_id = db.Column(db.String(50), db.ForeignKey('book.book_id'))

@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)