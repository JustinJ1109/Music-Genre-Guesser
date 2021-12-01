import librosa
from scipy.io import wavfile
import train_model as tm
import tensorflow.keras as keras
import numpy as np
import math

SAMPLE_RATE = 22050
TRACK_DURATION = 30 # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION

#Grabs the model.
D_PATH = 'preProcessedData/mfcc_data.json'
X_train, X_test, y_train, y_test = tm.prep_data(0.25, D_PATH)
input_shape = (X_train.shape[1], X_train.shape[2])

model = tm.train_model(input_shape)

model.load_weights("models/model25612864epoch5000batch100")

snippet_predictions = [0 for i in range(10)]

samples_per_segment = int(SAMPLES_PER_TRACK / 10)
num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / 512)

#Trims track to 30 seconds.
if (math.floor(librosa.get_duration(filename='test.wav')) > 30):
    sampleRate, waveData = wavfile.read("test.wav")
    startSample = 0
    endSample = int(30 * sampleRate)
    wavfile.write("test.wav", sampleRate, waveData[startSample:endSample])

topThree = [0 for i in range(3)]

for i in range(10):
    #Grabs a 3 second sample from the 30 second sample
    sampleRate, waveData = wavfile.read("test.wav")
    startSample = int(3 * i * sampleRate)
    endSample = int(3 * (i+1) * sampleRate)
    wavfile.write("snippet.wav", sampleRate, waveData[startSample:endSample])
    
    #Converts data to mfcc
    signal, sample_rate = librosa.load("snippet.wav")
    mfcc = librosa.feature.mfcc(signal, sample_rate, n_mfcc=13, n_fft=2048, hop_length=512)
    mfcc = mfcc.T

    prediction = tm.predict(model, mfcc)
    snippet_predictions[np.argmax(prediction, axis=1)[0]] += 1

print(snippet_predictions)
