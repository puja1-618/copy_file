import os
import shutil
from flask import Flask, request, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def fileFrontPage():
    return render_template('submit.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    # get the destination path from the input text
    if 'destination' in request.form:
        des = request.form['destination']
    # get the photo
    if 'photo' in request.files:
        photo = request.files['photo']
        if photo.filename != '':
            # check the provided path exists or not
            if os.path.exists(des):
                # Save the photo to the destination folder and render the thankyou.html page
                photo.save(os.path.join(des, photo.filename))
                return render_template('thankyou.html')
    # If destination path is empty or photo not provided
    # It will render the same page
    return redirect(url_for('fileFrontPage'))

if __name__ == '__main__':
    app.run(debug=True)
#jenkins_testing
