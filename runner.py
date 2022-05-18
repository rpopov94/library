from app import *
from app.models import *
from app.views import *
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.book_loader import BookView


admin = Admin(app, 'Library for developers', index_view=MyAdminIndexView(), base_template='my_master.html', template_mode='bootstrap4')

admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Tag, db.session))
admin.add_view(MyModelView(Level, db.session))
admin.add_view(MyModelView(Role, db.session))
admin.add_view(BookView(model=Book, session=db.session, name='Book'))

if __name__ == '__main__':
    app.run(debug=True)