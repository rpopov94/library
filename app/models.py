from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 

tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'))
)

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