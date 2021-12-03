import json
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow.keras as keras
from tensorflow.keras import layers
from tensorflow.python.keras.backend import dropout


# https://github.com/musikalkemist/DeepLearningForAudioWithPython/blob/master/14-%20Solving%20overfitting%20in%20neural%20networks/code/solving_overfitting.py
# used to help fix overfitting problems and general model structure

data = {}

#train_model.py
def load_data(data_path):
    """
    Loads the JSON data into a dictionary
    
    :data_path (str): string location to the JSON containing the data
    
    returns
        :inputs (nparray): array of mfcc data
        :targets (nparray): array of labels associated with the mfccs
    """
    
    print("Loading data...")
    #loads the data from JSON back into dictionary
    
    with open(data_path) as f:
        data = json.load(f)

    #convert lsits to numpy arr
    inputs = np.array(data["mfcc"])
    targets = np.array(data["labels"])

    return inputs, targets

def prep_data(test_size, data_path):
    """
    Prepares the data for training
    :test_size (float): percentage of data to use as test sample
    :data_path (str): path to test data
    """
    
    print("Prepping...")
    x, y = load_data(data_path)

    # create train/validation/test data split
    print("Splitting test data")
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=test_size)
    return X_train, X_test, Y_train, Y_test

def train_model(input_shape, trainX, trainY, testX, testY, epochs=100, batch_size=32, layer_sizes=[512, 256, 64], dropout_rate=0.3):
    """
    Trains the model using the data and parameters provided
    """

    # Defines the model.
    model = keras.Sequential()

    # add hidden layers
    model.add(keras.layers.Flatten(input_shape=input_shape))
    for i in range(len(layer_sizes)):
        model.add(keras.layers.Dense(layer_sizes[i], activation='relu', kernel_regularizer=keras.regularizers.l2(0.001)))
        model.add(keras.layers.Dropout(dropout_rate))

    # out layer
    model.add(keras.layers.Dense(10, activation='softmax'))

    # Defines Optimizer
    opt = keras.optimizers.Adam(learning_rate=0.0001)

    # Compiles the model
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

    MODEL_SAVE_PATH = "saved_models/"

    test_size = 0.25

    # get train, validation, test splits
    X_train, X_test, y_train, y_test = prep_data(test_size, D_PATH)

    # create network
    input_shape = (X_train.shape[1], X_train.shape[2])

    # parameters to tweak for model
    epochs = 200
    batch_size = 32
    layer_sizes = [512, 256, 64]
    dropout_rate = 0.3

    model = train_model(input_shape, X_train, y_train, X_test, y_test, epochs=epochs, batch_size=batch_size, layer_sizes=layer_sizes, dropout_rate=dropout_rate)

    layer_sizes_string = ""
    for i in range(len(layer_sizes)):
        layer_sizes_string += str(layer_sizes[i])
    model.save(MODEL_SAVE_PATH + "model-" + layer_sizes_string + "-e" + str(epochs) + "-b" + str(batch_size) + "-ln" + str(len(layer_sizes)) + "-t" + str(test_size * 100))