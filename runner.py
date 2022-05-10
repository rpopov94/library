import os
from flask_admin import Admin
from app import *
from app import models
from flask_admin.contrib.sqla import ModelView
from config import Config
from app.fileUpdoader import BookView

admin = Admin(app, name='microblog', url="/", template_mode='bootstrap3')

app.config.from_object(Config)

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
    app_dir = os.path.realpath(os.path.dirname(__file__))
    database_path = os.path.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_db()
    app.run()