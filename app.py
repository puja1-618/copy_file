import os
import shutil
from flask import Flask, request, render_template, url_for, redirect



app = Flask(__name__)


@app.route("/")
def fileFrontPage():
    return render_template('submit.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            photo.save(os.path.join(r"C:\Users\Public\Pictures", photo.filename))
    return redirect(url_for('fileFrontPage'))
def destination():
    dst=data["destination"]
    shutil.copy(r"C:\Users\Public\Pictures",dst)



if __name__ == '__main__':
    app.run(debug=True)