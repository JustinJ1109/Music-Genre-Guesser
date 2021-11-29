from flask.helpers import send_file
import librosa
from flask import Flask, render_template, request
from flask_restful import Resource, Api
import werkzeug
import train_model as tm
import matplotlib.pyplot as plt
import keras
import tensorflow
from scipy.io import wavfile
import numpy as np
import os

DATA_PATH = "preProcessedData/"
X_train, Y_train, X_test, Y_test, X_valid, Y_valid = tm.prep_data(.2, .2, DATA_PATH)
model = tm.train_model((X_train.shape[1], X_train.shape[2]))
print(str(model))

#app = Flask(__name__)
#api = Api(app)

#class Predictions(Resource):
    #def get(self):
        #return {'predictions': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]} 

#api.add_resource(Predictions, '/predictions')

#if __name__ == '__main__':
    #app.run(port=5002)

for i in range(1):
    #Gets file from angular front end.
    #app = Flask(__name__)
    #@app.route('/uploader', methods = ['GET', 'POST'])
    #def upload_file():
        #if request.method == 'POST':
            #f = request.files['file']
            #f.save(secure_filename(f.filename))
            #return f
    #f = upload_file()
    f = open("test.wav", "wr")
    
    #Trims the file down to 30 seconds.
    sampleRate, waveData = wavfile.read(f)
    startSample = int(0)
    endSample = int(30 * sampleRate)
    wavfile.write("out.wav", sampleRate, waveData[startSample:endSample])

    #Converts file to spectrogram.
    sampleRate, waveData = wavfile.read("out.wav")
    x, sr = librosa.load(snippet.path())
    X = librosa.stft(x)
    Xdb = librosa.amplitude_to_db(abs(X))
    fig = plt.figure(figsize=(14, 5), dpi=100) #FIXME: figsize and dpi is definitely wrong
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    fig.savefig("output.png")
    output = open("output.png", "r")

    #@app.route("/")
    #def predOut(output):
        #print (output)
        #return send_file("(Path_To_Angular)")
        
    for i in range(10):
        #Grabs a 3 second sample from the 30 second sample
        sampleRate, waveData = wavfile.read("output.png")
        startSample = int(3 * i * sampleRate)
        endSample = int(3 * (i+1) * sampleRate)
        wavfile.write("snippet.wav", sampleRate, waveData[startSample:endSample])
        
        snippet = open("snippet.wav", "wr")
    
        #Converts file to spectrogram.
        x, sr = librosa.load(snippet.path())
        X = librosa.stft(x)
        Xdb = librosa.amplitude_to_db(abs(X))
        fig = plt.figure(figsize=(14, 5), dpi=100) #FIXME: figsize and dpi is definitely wrong
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
        fig.savefig("snippet.png")
        
        #Converts spectrogram to mfcc
        snippetPic = open("snippet.png", "wr")
        
        signal, sample_rate = librosa.load(snippet, sr=sampleRate)
        
        mfcc = librosa.feature.mfcc(signal[startSample:endSample], sample_rate)
        mfcc = mfcc.T
        
        prediction = tm.predict(model, mfcc, "")
        print(prediction)

        #@app.route("/")
        #def predOut(prediction):
            #print (prediction)
            #return send_file("(Path_To_Angular)")