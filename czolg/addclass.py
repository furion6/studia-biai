
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
epochs = 50
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

base_model = model

base_model.pop() #remove the last layer - 'Dense' layer with 10 units
base_model.pop()
for layer in base_model.layers:
    layer.trainable = False
#base_model.add(Dense(4, activation = 'softmax',name='dense_headphones'))
base_model.add(Dense(4,name="xd"))
base_model.add(Activation('softmax',name = "act"))
#model.add(Dense(2,activation = 'softmax'))
base_model.summary() #Check architecture before starting the fine-tuning




# Processing training data
# -> appending images in a list 'train_images'
# -> appending labels in a list 'train_labels'
model = base_model


model.compile(
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

history = model.fit_generator(
    train_generator,
    steps_per_epoch=nb_train_samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=nb_validation_samples // batch_size)

# serialize weights to HDF5
model.save_weights('first_tryAfterAdding.h5')

# serialize model to JSON
model_json = model.to_json()
with open("modelafterAdding.json", "w") as json_file:
    json_file.write(model_json)



plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()












