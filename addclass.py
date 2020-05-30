
# Importing modules 
import numpy as np 
import pandas as pd 
import os
import matplotlib.pyplot as plt
import cv2
from tensorflow import keras

from keras.utils import to_categorical
from keras.layers import Dense,Conv2D,Flatten,MaxPool2D,Dropout
from keras.models import Sequential

from sklearn.model_selection import train_test_split


np.random.seed(1)






def createmodel(path):
    model = Sequential()
    model.add(Conv2D(kernel_size=(3,3), filters=32, activation='tanh', input_shape=(224,224,3,)))
    model.add(Conv2D(filters=30,kernel_size = (3,3),activation='tanh'))
    model.add(MaxPool2D(2,2))
    model.add(Conv2D(filters=30,kernel_size = (3,3),activation='tanh'))
    model.add(MaxPool2D(2,2))
    model.add(Conv2D(filters=30,kernel_size = (3,3),activation='tanh'))
    model.add(Flatten())
    model.add(Dense(20,activation='relu'))
    model.add(Dense(15,activation='relu'))
    model.add(Dense(2,activation = 'softmax'))
    model.load_weights(path)
    return model






base_model = createmodel('dn.h5')
base_model.pop() #remove the last layer - 'Dense' layer with 10 units
for layer in base_model.layers:
    layer.trainable = False
base_model.add(Dense(3, activation = 'softmax'))
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
train_images = []       
train_labels = []
shape = (224,224)  
train_path = './data/train'

for filename in os.listdir(train_path):
    if filename.split('.')[1] == 'jpg':
        img = cv2.imread(os.path.join(train_path,filename))
        
        # Spliting file names and storing the labels for image in list
        train_labels.append(filename.split('_')[0])
        
        # Resize all images to a specific shape
        img = cv2.resize(img,shape)
        
        train_images.append(img)

# Converting labels into One Hot encoded sparse matrix
train_labels = pd.get_dummies(train_labels).values

# Converting train_images to array
train_images = np.array(train_images)

# Splitting Training data into train and validation dataset
x_train,x_val,y_train,y_val = train_test_split(train_images,train_labels,random_state=1)

             
history = model.fit(x_train,y_train,epochs=50,batch_size=50,validation_data=(x_val,y_val))
model.save('afterdn.h5')





