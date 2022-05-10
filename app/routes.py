import io
from flask import render_template, send_file
from app import app
from app.models import *
from app.fileUpdoader import *


@app.route('/test')
def index():
    return "test"

@app.route("/download/<int:id>", methods=['GET'])
def download_blob(id):
    _book = Book.query.get_or_404(id)
    return send_file(
        io.BytesIO(_book.blob),
        attachment_filename=_book.filename,
        mimetype=_book.mimetype
    )