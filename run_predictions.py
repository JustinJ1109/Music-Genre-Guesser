
#Separate file (runPredictions.py) from here on out:
import librosa
from flask import Flask, render_template, request
from werkzeug import secure_filename
import train_model as tm
import matplotlib.pyplot as plt
import keras
from scipy.io import wavfile
import numpy as np
import os

DATA_PATH = "preProcessedData/"
model = tm.train_model(tm.load_data(DATA_PATH))

while (True):
    #Gets file from angular front end.
    app = Flask(__name__)
    @app.route('/uploader', methods = ['GET', 'POST'])
    def upload_file():
        if request.method == 'POST':
            f = request.files['file']
            f.save(secure_filename(f.filename))
            return f
    f = upload_file()
    
    #Trims the file down to 30 seconds.
    sampleRate, waveData = wavfile.read(f)
    startSample = int(0)
    endSample = int(30 * sampleRate)
    wavfile.write(".wav", sampleRate, waveData[startSample:endSample])
    
    predictions = {}
    for x in os.listdir(DATA_PATH):
        predictions.update({x[:-5] : 0})
        
    for i in range(10):
        #Grabs a 3 second sample from the 30 second sample
        sampleRate, waveData = wavfile.read(f)
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
        
        prediction = predict(model, )

        @app.route("/")
        def predOut(prediction):
            print (prediction)
            return send_file("(Path_To_Angular)")
                
        # add snippet to list of predictions
        predictions[prediction] += 1