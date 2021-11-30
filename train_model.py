import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import os

#https://mybb.gvsu.edu/bbcswebdav/pid-9247138-dt-content-rid-78592561_1/courses/GVCIS365.01.202210/neuralNetworksPythonKeras.pdf and
#https://github.com/musikalkemist/DeepLearningForAudioWithPython/tree/master/16-%20How%20to%20implement%20a%20CNN%20for%20music%20genre%20classification/code and
#https://www.kaggle.com/msripooja/steps-to-convert-audio-clip-to-spectrogram and 
#https://pythonbasics.org/flask-upload-file/
#used as a basis for code.


data = {}

#train_model.py
def load_data(data_path):
    print("Loading data...")
#loads the data from JSON back into dictionary
    for f in os.listdir(data_path):
        print("loading {}".format(f))
        with open(data_path + f) as jFile:
            data.update(json.load(jFile))
    # FIXME: not structured properly
    print("Loaded!")
    
    x = []
    y = []
    for k, v in data.items():
        x.append(v)
        y.append(k)
    x = np.array(x)
    y = np.array(y)

    return x, y

###
def prep_data(test_size, validation_size, data_path):
    print("Prepping...")
    x, y = load_data(data_path)



    
    # create train/validation/test data split
    print("Splitting test data")
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=test_size)
    print("Split data successfully. Split again...")
    X_train, X_valid, Y_train, Y_valid = train_test_split(X_train, Y_train, test_size=validation_size)
    

    print("making new axes")
    X_train = X_train[..., np.newaxis]
    X_valid = X_valid[..., np.newaxis]
    X_test = X_test[..., np.newaxis]

    return X_train, X_valid, X_test, Y_train, Y_valid, Y_test

###
def train_model(input_shape):
    print("Training...")
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
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')) 
    model.add(keras.layers.BatchNormalization())
    print("Layer 1 added")
    
    # layer 2
    model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPooling2D((3, 3), strides=(2, 2), padding='same')) 
    model.add(keras.layers.BatchNormalization())
    print("Layer 2 added")

    # layer 3
    model.add(keras.layers.Conv2D(32, (2, 2), activation='relu', input_shape=input_shape))
    model.add(keras.layers.MaxPooling2D((2, 2), strides=(2, 2), padding='same'))
    model.add(keras.layers.BatchNormalization())
    print("Layer 3 added")

    # flatten out and feed to dense
    model.add(keras.layers.Flatten())
    model.add(keras.layers.Dense(64, activation='relu'))
    model.add(keras.layers.Dropout(0.3))
    print("Layers flattened")

    # out layer
    model.add(keras.layers.Dense(10, activation='softmax'))
    print("Output layer added!")


    return model

def predict(model, x_data, y_data=None):
    print("Predicting...")
    # requires 4d array (1, 130, 13, 1)
    x_data = x_data[np.newaxis, ...]
    prediction = model.predict(x_data)
    pred_index = np.argmax(prediction, axis=1)

    print("Target: {}, Predicted Label: {}".format(y_data, pred_index))
    return prediction