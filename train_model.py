import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import matplotlib.pyplot as plt
import os

#https://mybb.gvsu.edu/bbcswebdav/pid-9247138-dt-content-rid-78592561_1/courses/GVCIS365.01.202210/neuralNetworksPythonKeras.pdf and
#https://github.com/musikalkemist/DeepLearningForAudioWithPython/tree/master/16-%20How%20to%20implement%20a%20CNN%20for%20music%20genre%20classification/code and
#https://www.kaggle.com/msripooja/steps-to-convert-audio-clip-to-spectrogram and 
#https://pythonbasics.org/flask-upload-file/
#used as a basis for code.


data = {}

#train_model.py
def load_data(data_path):
#loads the data from JSON back into dictionary
    for f in os.listdir(data_path):
        with open(data_path + f) as jFile:
            data.update(json.load(jFile))
    return data.values(), data.keys()

###
def prep_data(test_size, validation_size, data_path):
    x, y = load_data(data_path)
    
    # create train/validation/test data split
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=test_size)
    X_train, X_valid, Y_train, Y_valid = train_test_split(X_train, Y_train, test_size=validation_size)
    
    X_train = X_train[..., np.newaxis]
    X_valid = X_valid[..., np.newaxis]
    X_test = X_test[..., np.newaxis]

    return X_train, Y_train, X_test, Y_test, X_valid, Y_valid
    
def predict(model, x_data, y_data):
    # requires 4d array (1, 130, 13, 1)
    y_data = None
    x_data = x_data[np.newaxis, ...]
    prediction = model.predict(x_data)
    pred_index = np.argmax(prediction, axis=1)

    print("Target: {}, Predicted Label: {}".format(y_data, pred_index))
    return prediction
    
###
def train_model(input_shape):
    #Restructures trainX and trainY.
    # trainX = trainX.reshape((trainX.shape[0], 432, 288, 1)) #FIXME: Dimensions
    # testX = testX.reshape((testX.shape[0], 432, 288, 1)) #FIXME: Dimensions
    # trainY = keras.to_categorical(trainY)
    # testY= keras.to_categorical(testY)

    #Changes trainer from int to float within range 0-255.
    # train_norm = keras.train.astype('float32')
    # train_norm /= 255.0
    # test_norm = keras.train.astype('float32')
    # test_norm /= 255.0

    #Defines the model.
    model = keras.Sequential()

    # layer 1
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape)) #FIXME: Dimensions
    model.add(keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')) #FIXME: Dimensions
    model.add(keras.layers.BatchNormalization())

    # layer 2
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape)) #FIXME: Dimensions
    model.add(keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')) #FIXME: Dimensions
    model.add(keras.layers.BatchNormalization())

    # layer 3
    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu', input_shape=input_shape)) #FIXME: Dimensions
    model.add(keras.layers.MaxPooling2D((2, 2), strides=(2, 2), padding='same')) #FIXME: Dimensions
    model.add(keras.layers.BatchNormalization())

    # flatten out and feed to dense
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dropout(0.3))

    # out layer
    model.add(keras.layers.Dense(10, activation='softmax'))


    return model


