#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import request



import tensorflow as tf

from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image

import requests

from io import BytesIO




# dimensions of our images
img_width, img_height = 224,224

#'binary_accuracy', 'categorical_accuracy'
# load the model we saved
model = tf.keras.models.load_model('final_model.h5')
model.summary()
# predicting images


def retClass(url):
    response = requests.get(url)

    img = Image.open(BytesIO(response.content))	
    img = img.resize((img_width, img_height))
    #img = image.load_img(plik, target_size=(img_width, img_height))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    batchkkk = 64

    images = np.vstack([x])
    a = model.predict(images, batch_size=batchkkk)
    return (a[0][0])
    




app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    d = request.args.get("url")

    print(d)
    acc = retClass(d)
    if acc == 0.0:
        ret = 'kot'
    elif acc <0.0001:
        ret = 'moze-kot'
    else:
        ret = 'nie-kot'
    return jsonify(wynik=ret)


if __name__ == '__main__':
    app.run(debug=True)


