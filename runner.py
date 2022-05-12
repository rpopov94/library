import os
from app import app, db, admin
from app import models
from flask_admin.contrib.sqla import ModelView
from app.fileUpdoader import BookView



admin.add_view(ModelView(models.User, db.session))
#admin.add_view(ModelView(models.Book, db.session))
admin.add_view(ModelView(models.Tag, db.session))
admin.add_view(ModelView(models.Level, db.session))
admin.add_view(BookView(model=models.Book, session=db.session, name='Book'))

def build_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    
if __name__ == '__main__':
    build_db()
    app.run()
    