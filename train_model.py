import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
import os

from tensorflow.keras import layers
from tensorflow.python.keras.backend import dropout

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
def train_model(input_shape, trainX, trainY, testX, testY, epochs=100, batch_size=32, layer_sizes=[512, 256, 64], dropout_rate=0.3):
    print("Training...")
    

    #Defines the model.
    model = keras.Sequential()

    model.add(keras.layers.Flatten(input_shape=input_shape))

    for i in range(layer_sizes):
        model.add(keras.layers.Dense(layer_sizes[i], activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)))
        model.add(keras.layers.Dropout(dropout_rate))

    # out layer
    model.add(keras.layers.Dense(10, activation='softmax'))
    print("Output layer added!")

    #Defines Optimizer
    opt = keras.optimizers.Adam(learning_rate=0.0001)

    #Compiles the model
    model.compile(optimizer=opt, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

    model.fit(trainX, trainY, epochs=epochs, batch_size=batch_size, validation_data=(testX, testY))

    return model



def predict(model, x_data, y_data=None):
    print("Predicting...")
    # requires 4d array (1, 130, 13, 1)
    x_data = x_data[np.newaxis, ...]
    prediction = model.predict(x_data)
    pred_index = np.argmax(prediction, axis=1)

    print("Target: {}, Predicted Label: {}".format(y_data, pred_index))
    return prediction

D_PATH = 'preProcessedData/mfcc_data.json'
if __name__ == "__main__":

    # get train, validation, test splits
    X_train, X_test, y_train, y_test = prep_data(0.3, D_PATH)

    # create network
    input_shape = (X_train.shape[1], X_train.shape[2])

    epochs = 100
    batch_size = 40
    layer_sizes = [512, 256, 128]

    model = train_model(input_shape, X_train, y_train, X_test, y_test, epochs=epochs, batch_size=batch_size, layer_sizes=layer_sizes)

    model.save_weights("models/model" + str(layer_sizes[0]) + str(layer_sizes[1]) + str(layer_sizes[2]) + "epoch" + str(epochs) + "batch" + str(batch_size))

