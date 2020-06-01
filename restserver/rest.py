#!flask/bin/python
from flask import Flask
from flask import jsonify
from flask import request
import json
import tensorflow as tf
from keras.optimizers import SGD

#from keras.models import load_model
from keras.preprocessing import image
import numpy as np
from PIL import Image
import os, os.path
import requests
from string import digits
from io import BytesIO
from keras.models import model_from_json
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

import keras.backend.tensorflow_backend as tb
tb._SYMBOLIC_SCOPE.value = True

def loadModel(model, modelWeights):
    json_file = open(model, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights(modelWeights)
    return loaded_model



def trainFromNew():
	pass


def downloadImage(url):
	response = requests.get(url,verify=False)
	img = Image.open(BytesIO(response.content))	
	img = img.resize((224,224))
	img = img.convert('RGB')
	return img#img.save("img/" + sys.argv[1] + "_" + str(i)+".jpg", "JPEG")

	
def countFilesInDirectory(path):
	ls = os.listdir(path) # dir is your directory path
	return len(ls)#includes directory, w/o . and ..



def gatherInfoImpl(json):
	for j in json['data']:
		print("adding: " + j['label'])
		if j['label'].lower() not in classLabels:# we dont have that label
			howmanylabels = len(classLabels)
			os.mkdir('data/' + str(howmanylabels+1) + j['label'].lower())
			classLabels.append(j['label'].lower())
		indexOfFolder = classLabels.index(j['label'].lower()) + 1
		folderName = str(indexOfFolder) + j['label'].lower()
		fileCounter = countFilesInDirectory('data/'+folderName)
		for url in j['urls']:
			img = downloadImage(url)
			img.save("data/" + folderName + "/" + str(fileCounter)+".jpg", "JPEG")
			fileCounter = fileCounter + 1
def loadClassLabels():
	ls = os.listdir("data")
	ls.sort()
	for i in range(len(ls)): 
		remove_digits = ls[i].maketrans('', '', digits)
		ls[i] = ls[i].translate(remove_digits)
	print(ls)
	return ls
	
def isImplementedImpl(label):
	nb_classes = model.layers[-1].output_shape[-1]
	if label not in classLabels:
		return False
	if classLabels.index(label) >= nb_classes:
		return False
	return True
def relearnImpl():
	img_width, img_height = 224, 224

	train_data_dir = 'data/'
	nb_train_samples = 50
	#nb_validation_samples = 3
	epochs = 50#50
	batch_size = 16

	if K.image_data_format() == 'channels_first':
	    input_shape = (3, img_width, img_height)
	else:
	    input_shape = (img_width, img_height, 3)

	#dmodel = Sequential()
	#dmodel.add(Conv2D(32, (3, 3), input_shape=input_shape))
	#dmodel.add(Activation('relu'))
	#dmodel.add(MaxPooling2D(pool_size=(2, 2)))

	#dmodel.add(Conv2D(32, (3, 3)))
	#dmodel.add(Activation('relu'))
	#dmodel.add(MaxPooling2D(pool_size=(2, 2)))

	#dmodel.add(Conv2D(64, (3, 3)))
	#dmodel.add(Activation('relu'))
	#dmodel.add(MaxPooling2D(pool_size=(2, 2)))

	#dmodel.add(Flatten())
	#dmodel.add(Dense(64))
	#dmodel.add(Activation('relu'))
	#dmodel.add(Dropout(0.5))
	#dmodel.add(Dense(len(classLabels),activation = 'sigmoid'))

	dmodel = Sequential()
	dmodel.add(Conv2D(32, kernel_size=(3, 3),padding='same',input_shape=input_shape))
	dmodel.add(Activation('relu'))
	dmodel.add(Conv2D(64, (3, 3)))
	dmodel.add(Activation('relu'))
	dmodel.add(MaxPooling2D(pool_size=(2, 2)))
	dmodel.add(Dropout(0.25))

	dmodel.add(Conv2D(64,(3, 3), padding='same'))
	dmodel.add(Activation('relu'))
	dmodel.add(Conv2D(64, 3, 3))
	dmodel.add(Activation('relu'))
	dmodel.add(MaxPooling2D(pool_size=(2, 2)))
	dmodel.add(Dropout(0.25))

	dmodel.add(Flatten())
	dmodel.add(Dense(512))
	dmodel.add(Activation('relu'))
	dmodel.add(Dropout(0.5))
	dmodel.add(Dense(len(classLabels),activation = 'sigmoid'))





	dmodel.compile(
	              #loss='categorical_crossentropy', 
	              loss='binary_crossentropy',
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


	dmodel.summary()

	history = dmodel.fit_generator(
	    train_generator,
	    steps_per_epoch=10,#nb_train_samples // batch_size,
	    epochs=epochs
	   )# validation_data=validation_generator,
	    #validation_steps=nb_validation_samples // batch_size)

	# serialize weights to HDF5
	dmodel.save_weights('first_try.h5')

	# serialize model to JSON
	model_json = dmodel.to_json()
	with open("model.json", "w") as json_file:
	    json_file.write(model_json)
	model = dmodel

def checkNImpls(json):#softmax
	ret = []
	for j in json['data']:
		label = j['label'].lower()
		url = j['url']
		print("for url: " + url)
		img = downloadImage(url)
		img_width, img_height = 224, 224
		x = image.img_to_array(img)
		x = np.expand_dims(x, axis=0)
		#images = np.vstack([x])
		classes = model.predict(x)
		print("Predicted :- ",classLabels[np.argmax(classes)-1])
		ret.append(str(classLabels[np.argmax(classes)-1] == label))
	return ret

def checkNImpl(json):#sigmoid
	ret = []
	print("#########################################[]####################################")
	for j in json['data']:
		label = j['label'].lower()
		url = j['url']
		print("for url: " + url)
		img = downloadImage(url)
		img_width, img_height = 224, 224
		x = image.img_to_array(img)
		x = np.expand_dims(x, axis=0)
		#images = np.vstack([x])
		classes = model.predict(x)
		print("klasy: ")
		print(classes[0])
		#print("Predicted :- ",classLabels[np.argmax(classes)-1])
		#ret.append(str(classLabels[np.argmax(classes)-1] == label))
		labelid = classLabels.index(j['label'].lower())
		print("eldo")
		ret.append(classes[labelid] >=0.5)
	return ret
	
	
	
#nb_classes = model.layers[-1].output_shape[-1]
classLabels = loadClassLabels()
model = loadModel("model.json","first_try.h5")


app = Flask(__name__)

@app.route('/relearn', methods=['POST'])
def relearn():
	relearnImpl()
	return "ok"
	
@app.route('/gatherInfo', methods=['POST'])
def gatherInfo():
	print("elo")
	jdata = request.get_json(force=True)
	gatherInfoImpl(jdata)
	return "ok"
	
@app.route('/checkN', methods=['GET'])
def checkN():
	jdata = request.get_json(force=True)
	print(jdata)
	r = checkNImpl(jdata)
	return json.dumps(r)
	
@app.route('/isImplemented', methods=['GET'])
def isImplemented():
	jdata = request.get_json(force=True)
	ret = str(isImplementedImpl(jdata['label']))
	return json.dumps({"value":ret})



if __name__ == '__main__':
    app.run(threaded=False)
    



