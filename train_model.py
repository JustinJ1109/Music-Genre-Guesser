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
    
    with open(data_path) as f:
        data = json.load(f)

    #convert lsits to numpy arr
    inputs = np.array(data["mfcc"])
    targets = np.array(data["labels"])

    return inputs, targets


###
def prep_data(test_size, data_path):
    print("Prepping...")
    x, y = load_data(data_path)

    # create train/validation/test data split
    print("Splitting test data")
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=test_size)
    

    return X_train, X_test, Y_train, Y_test

###
def train_model(input_shape):
    print("Training...")
    
    #Defines the model.
    model = keras.Sequential()

    model.add(keras.layers.Flatten(input_shape=input_shape))

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