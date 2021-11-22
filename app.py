import os
from ocr import *
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(filename)
        message = ocr_function(filename)[0]
        print(message)
        # print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        return render_template('index.html', filename=filename, message=message)
    else:
        flash('Allowed image types are -> png, jpg, jpeg, gif')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    print("jestem tuuuu")
    # print('display_image filename: ' + filename)
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


@app.route('/ocr<filename>')
def ocr(filename):
    print(filename)
    given_url = "https://scontent-vie1-1.xx.fbcdn.net/v/t1.15752-9/256775408_3140666182820284_8243182282827745946_n.jpg?_nc_cat=102&ccb=1-5&_nc_sid=ae9488&_nc_ohc=aJ6GnagHtvYAX8JEq9e&_nc_ht=scontent-vie1-1.xx&oh=d80b7aa9d7e69abc2357225cb44d57db&oe=61BF7429"

    message = ocr_function()
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()