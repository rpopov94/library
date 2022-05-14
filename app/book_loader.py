from app.models import *
from markupsafe import Markup
from flask_admin.contrib.sqla import ModelView
from gettext import gettext
from wtforms.widgets import FileInput
from werkzeug.datastructures import FileStorage
from wtforms import fields
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from werkzeug.datastructures import FileStorage

class BlobUploadField(fields.StringField):
    widget = FileInput()
    def __init__(self, label=None, allowed_extensions=None,
                 size_field=None, filename_field=None, mimetype_field=None, **kwargs):
        self.allowed_extensions = allowed_extensions
        self.size_field = size_field
        self.filename_field = filename_field
        self.mimetype_field = mimetype_field
        validators = [DataRequired()]

        super(BlobUploadField, self).__init__(label, validators, **kwargs)
    
    def is_file_allowed(self, filename):
        if not self.allowed_extensions:
            return True

        return ('.' in filename and
                filename.rsplit('.', 1)[1].lower() in
                map(lambda x: x.lower(), self.allowed_extensions))

    def _is_uploaded_file(self, data):
        return (data and isinstance(data, FileStorage) and data.filename)

    def pre_validate(self, form):
        super(BlobUploadField, self).pre_validate(form)
        if self._is_uploaded_file(self.data) and not self.is_file_allowed(self.data.filename):
            raise ValidationError(gettext('Invalid file extension'))

    def process_formdata(self, valuelist):
        if valuelist:
            data = valuelist[0]
            self.data = data

    def populate_obj(self, obj, name):

        if self._is_uploaded_file(self.data):

            _blob = self.data.read()

            setattr(obj, name, _blob)

            if self.size_field:
                setattr(obj, self.size_field, len(_blob))

            if self.filename_field:
                setattr(obj, self.filename_field, self.data.filename)

            if self.mimetype_field:
                setattr(obj, self.mimetype_field, self.data.content_type)

class BookView(ModelView):

    column_list = ('name', 'size', 'filename', 'mimetype', 'download')
    form_columns = ('name', 'blob')

    form_extra_fields = {'blob': BlobUploadField(
        label='File',
        allowed_extensions=['pdf', 'doc', 'docx', 'xls', 'xlsx', 'png', 'jpg', 'jpeg', 'gif'],
        size_field='size',
        filename_field='filename',
        mimetype_field='mimetype'
    )}

    def _download_formatter(self, context, model, name):
        return Markup("<a href='{url}' target='_blank'>Download</a>".format(url=self.get_url('download_blob', id=model.id)))

    column_formatters = {
        'download': _download_formatter,
    }