from flask import Flask, request, render_template, redirect, flash
from werkzeug.utils import secure_filename
from main import Predict
import os


app = Flask(__name__, static_folder='static')


UPLOAD_FLODER = 'static/images/'

app.secret_key = "HI THIS IS A SECRET KEY!!!!"

app.config['UPLOAD_FLODER'] = UPLOAD_FLODER




@app.route('/')
def index():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def submit_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No files present")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("No files are selected")
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FLODER'],filename))
            predictions, label = Predict(filename)
            print(predictions)
            flash(label)
            full_filename = os.path.join(app.config['UPLOAD_FLODER'], filename)
            flash(full_filename)
            print(full_filename)
            return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)