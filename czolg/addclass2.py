
# Importing modules 
import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as plt
import cv2
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import to_categorical
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.models import Sequential

from sklearn.model_selection import train_test_split


from keras.models import model_from_json

img_width, img_height = 224, 224

train_data_dir = 'data/train'
validation_data_dir = 'data/validation'
nb_train_samples = 100
nb_validation_samples = 3
epochs = 25
batch_size = 16

# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("first_try.h5")
print("Loaded model from disk")

model = loaded_model

model_2 = Sequential()

# getting all the layers except the output one
for layer in model.layers[:-1]: # just exclude last layer from copying
    model_2.add(layer)

# prevent the already trained layers from being trained again 
# (you can use layers[:-n] to only freeze the model layers until the nth layer)
for layer in model_2.layers:
    layer.trainable = False

# adding the new output layer, the name parameter is important 
# otherwise, you will add a Dense_1 named layer, that normally already exists, leading to an error
model_2.add(Dense(4, name='new_Dense', activation='softmax'))


weights_bak = model.layers[-1].get_weights()
weights_new = model_2.layers[-1].get_weights()

weights_new[0][:, :-1] = weights_bak[0]
weights_new[1][:-1] = weights_bak[1]

weights_new[0][:, -1] = np.mean(weights_bak[0], axis=1)
weights_new[1][-1] = np.mean(weights_bak[1])

model_2.layers[-1].set_weights(weights_new)





model_2.summary()


model_2.compile(
              loss='categorical_crossentropy', 
              metrics=['acc'],
              optimizer='adam'
             )

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

# this is the augmentation configuration we will use for testing:
# only rescaling
test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

validation_generator = test_datagen.flow_from_directory(
    validation_data_dir,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    class_mode='categorical')

history = model_2.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

# serialize weights to HDF5
model_2.save_weights('first_tryAfterAdding.h5')

# serialize model to JSON
model_json = model_2.to_json()
with open("modelafterAdding.json", "w") as json_file:
    json_file.write(model_json)



plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()












