from flask import Flask,request
import flask
from flask import Flask,request
import flask
import numpy as np
from scipy import sparse
from skimage.io import imsave
from keras.preprocessing import image
import os
from keras import backend as K
from skimage.color import rgb2lab, lab2rgb, rgb2gray, xyz2lab
from keras.preprocessing.image import load_img, img_to_array, ImageDataGenerator
from keras.applications.vgg16 import preprocess_input
from keras.models import model_from_json
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/images/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello_world():
    return "hello world"


@app.route('/home')
def index():
    return flask.render_template('home.html')


@app.route('/home', methods=['POST'])
def uploading_file():
    print("working")
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
# load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    # Get images
    image = img_to_array(load_img('static/images/'+filename))
    image = np.array(image, dtype=float)
    X = rgb2lab(1.0/255*image)[:,:,0]
    Y = rgb2lab(1.0/255*image)[:,:,1:]
    Y /= 128
    X = X.reshape(1, 400, 400, 1)
    Y = Y.reshape(1, 400, 400, 2)
    output = loaded_model.predict(X)
    output *= 128
# Output colorizations
    cur = np.zeros((400, 400, 3))
    cur[:,:,0] = X[0][:,:,0]
    cur[:,:,1:] = output[0]
    imsave("static/images/img_result_"+filename, lab2rgb(cur))
    imsave("static/images/img_gray_version_"+filename, rgb2gray(lab2rgb(cur)))
    resul=['static/images/'+filename,'static/images/img_result_'+filename,'static/images/img_gray_version_'+filename]
    print(resul)
    return flask.render_template('result.html',result=resul)


if __name__ == '__main__':
    app.run(debug=False)
