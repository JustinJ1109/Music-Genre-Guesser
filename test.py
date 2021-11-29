import librosa
from scipy.io import wavfile
import train_model as tm
import numpy


D_PATH = 'preProcessedData/'
if __name__ == "__main__":

    # get train, validation, test splits
    X_train, X_validation, X_test, y_train, y_validation, y_test = tm.prep_data(0.25, 0.2, D_PATH)

    # create network
    input_shape = (X_train.shape[1], X_train.shape[2], 1)
    model = tm.train_model(input_shape)


snippet_predictions = {
        "blues" : 0, "classical" : 0, "country" : 0, 
        "disco" : 0, "hiphop" : 0, "jazz" : 0, 
        "metal" : 0, "pop" : 0, "reggae" : 0, "rock" : 0}


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
    librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
    
    #Converts spectrogram to mfcc
    snippetPic = open("snippet.png", "wr")
    signal, sample_rate = librosa.load(snippet, sr=sampleRate)
    mfcc = librosa.feature.mfcc(signal[startSample:endSample], sample_rate)
    mfcc = mfcc.T

    snippet_predictions[tm.predict(tm.model, mfcc)] += 1

    curr_max_key = ""
    curr_max = 0
    for k, v in snippet_predictions.items():
        if v > curr_max:
            curr_max = v
            curr_max_key = k

    prediction = curr_max_key
