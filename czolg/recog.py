import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import sys
from keras.models import model_from_json

IMAGE_SIZE = 224



# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("first_try.h5")
print("Loaded model from disk")

model = loaded_model



img_width, img_height = 224, 224



#nienoze
img = image.load_img(sys.argv[1], target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

#images = np.vstack([x])
classes = model.predict(x)
print(classes)
output = { 0:'car',1:'dogo',2:'lamp',3:'headphones'}
print("Predicted :- ",output[np.argmax(classes)])




