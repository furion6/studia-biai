import tensorflow as tf
import numpy as np
from keras.preprocessing import image
import sys

IMAGE_SIZE = 224





model = tf.keras.models.load_model(sys.argv[1])

model.summary()



img_width, img_height = 224, 224



#nienoze
img = image.load_img(sys.argv[2], target_size=(img_width, img_height))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

#images = np.vstack([x])
classes = model.predict(x)
print(classes)
output = { 0:'dog',1:'car',2:'yellow'}
print("Predicted :- ",output[np.argmax(classes)])




