from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, request, session, flash
from database import opendb, DB_URL
from database import AutomobileImage
from werkzeug.utils import secure_filename
from db_helper import *
import os


app = Flask(__name__)
app.secret_key = "hello world of secret keys"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'

def session_add(key, value):
    session[key] = value

def save_file(file):
    filename = secure_filename(file.filename)
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(path)
    return path

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg','tiff']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():

    return render_template('upload.html')

@app.route('/process/form', methods=['GET','POST'])
def process_form():
    file = request.files['file']
    if file.filename == '':
        flash('No file selected', 'danger')
        return redirect('/upload')
    if file and allowed_file(file.filename):
        path = save_file(file)
        automobile = AutomobileImage(path=path, name = file.filename)
        db_save(automobile)
        session_add('last_upload', path)
        flash('File uploaded successfully', 'success')
    return redirect('/upload')

@app.route('/uploads/all')
def all_uploads():
    automobiles = db_get_all(AutomobileImage)
    return render_template('list.html', images=automobiles)

@app.route('/<filename>/view')
def view(filename):
    return render_template('view.html', filename=filename)

@app.route('/<filename>/delete')
def delete(filename):
    try:
        automobile = db_get_by_field(AutomobileImage, name=filename)
        path = automobile.path
        db_delete(automobile)
        os.remove(path)
        flash('File deleted successfully', 'success')
        return redirect('/')
    except:
        flash('File not found', 'danger')
        return redirect('/')

@app.route('/<filename>/predict', methods=['GET', 'POST'])
def predict_part(filename):
    return render_template('predict.html', filename=filename)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)