from keras.saving.save import load_model
import librosa
from scipy.io import wavfile
import train_model as tm
from keras.models import load_model
import numpy as np
import math

SAMPLE_RATE = 22050
TRACK_DURATION = 30 # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION

WAV_PATH = "test_music/pachelbel.wav"
MODEL_PATH = "saved_models/model-512-256-64-e200b32ln3t25.0"

model = load_model(MODEL_PATH)

samples_per_segment = int(SAMPLES_PER_TRACK / 10)
num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / 512)

def predict(file):
    """Predicts the genres of the song at the file path
    
    :file (str): path to .wav file to predict
    :return topThree []: top three predictions guessed
    :return topThreePercentage []: top three percentages that the algorithm guessed for each prediction
    """

    snippet_predictions = [0 for i in range(10)]
        #Trims track to 30 seconds.
    if (math.floor(librosa.get_duration(filename=file)) > 30):
        sampleRate, waveData = wavfile.read(file)
        startSample = 0
        endSample = int(30 * sampleRate)
        wavfile.write(file, sampleRate, waveData[startSample:endSample])

    for i in range(10):
        #Grabs a 3 second sample from the 30 second sample
        sampleRate, waveData = wavfile.read(file)
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
    topThree = [0 for i in range(3)]
    topThreePercent = [0 for i in range(3)]

    for i in range(3):
        max_value = max(snippet_predictions)
        topThreePercent[i] = max_value * 10
        for j in range(10):
            if (snippet_predictions[j] == max_value):
                if (j == 0):
                    topThree[i] = "Blues"
                elif (j == 1):
                    topThree[i] = "Classical"
                elif (j == 2):
                    topThree[i] = "Country"
                elif (j == 3):
                    topThree[i] = "Disco"
                elif (j == 4):
                    topThree[i] = "Hip Hop"
                elif (j == 5):
                    topThree[i] = "Jazz"
                elif (j == 6):
                    topThree[i] = "Metal"
                elif (j == 7):
                    topThree[i] = "Pop"
                elif (j == 8):
                    topThree[i] = "Reggae"
                elif (j == 9):
                    topThree[i] = "Rock"
                snippet_predictions[j] = -1
                break

    print(topThree)
    print(topThreePercent)


    return topThree, topThreePercent

################################################
# IF RUNNING WITHOUT UI, UNCOMMENT BELOW TO RUN
################################################
#predict(WAV_PATH)


