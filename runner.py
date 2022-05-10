import os
from flask_admin import Admin
from app import app, db
from app import models
from flask_admin.contrib.sqla import ModelView
from config import Config
from app.fileUpdoader import BookView

admin = Admin(app, name='microblog', url="/", template_mode='bootstrap3')

app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

admin.add_view(ModelView(models.User, db.session))
#admin.add_view(ModelView(models.Book, db.session))
admin.add_view(ModelView(models.Tag, db.session))
admin.add_view(ModelView(models.Level, db.session))
admin.add_view(BookView(model=models.Book, session=db.session, name='Book'))

def build_db():
    db.create_all()
    db.session.commit()

@app.before_first_request
def first_request():
    build_db()
    
if __name__ == '__main__':
    app.run()