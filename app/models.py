from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Book(db.Model):
    id = db.Column(db.String(50))
    title = db.Column(db.String(64), index=True, unique=True)
    publisher = db.Column(db.String(64), index=True, unique=True)
    year = db.Column(db.Integer)
    level = db.relationship('Level', backref='book', lazy='dynamic')
    tag = db.relationship("Tag", backref='book', lazy="dynamic")
    book_file  = db.Column(db.LargeBinary)

class Levels(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.String(50), db.ForeignKey('book.id'))

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_id = db.Column(db.String(50), db.ForeignKey('book.id'))