from flask import Blueprint, render_template, abort, send_file
import os

files = Blueprint('files', __name__)

@files.route('/', defaults={'req_path': ''})
@files.route('/<path:req_path>')
def dir_listing(req_path):
    BASE_DIR = '/Users/Ignacio/Documents/DuocUC/VisualStudioCode/flask/small-web'

    # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, req_path)

    # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)

    # Check if path is a file and serve
    if os.path.isfile(abs_path):
        return send_file(abs_path)

    # Show directory contents
    files = os.listdir(abs_path)
    return render_template('files.html', files=files)