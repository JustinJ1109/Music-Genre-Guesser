import json
import os
import math
import librosa

DATASET_PATH = "Data/genres_original/"
JSON_PATH = "preProcessedData/"
SAMPLE_RATE = 22050
TRACK_DURATION = 30 # measured in seconds
SAMPLES_PER_TRACK = SAMPLE_RATE * TRACK_DURATION

#

# code sampled from https://github.com/musikalkemist/DeepLearningForAudioWithPython/blob/master/12-%20Music%20genre%20classification:%20Preparing%20the%20dataset/code/extract_data.py

def save_mfcc(dataset_path, json_path, num_mfcc=13, n_fft=2048, hop_length=512, num_segments=5):
    print([x[:-5] for x in os.listdir(json_path)])

    samples_per_segment = int(SAMPLES_PER_TRACK / num_segments)
    num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)

    # loop through all genre sub-folder
    for (dirpath, dirnames, filenames) in os.walk(dataset_path):
        data = []

        # ensure we're processing a genre sub-folder level
        if dirpath is not dataset_path:

            # save genre label
            semantic_label = dirpath.split("/")[-1]
            if semantic_label not in [x[:-5] for x in os.listdir(json_path)]:

                print("\nProcessing: {}".format(semantic_label))

                # process all audio files in genre sub-dir
                for f in filenames:

            # load audio file
                    file_path = os.path.join(dirpath, f)
                    signal, sample_rate = librosa.load(file_path, sr=SAMPLE_RATE)

                    # process all segments of audio file
                    for d in range(num_segments): # 10 segments

                        # calculate start and finish sample for current segment
                        start = samples_per_segment * d
                        finish = start + samples_per_segment

                        # extract mfcc
                        mfcc = librosa.feature.mfcc(signal[start:finish], sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length)
                        mfcc = mfcc.T

                        # store only mfcc feature with expected number of vectors
                        if len(mfcc) == num_mfcc_vectors_per_segment:
                            data.append(sum(mfcc.tolist(), []))
                            print("{}, segment:{}".format(file_path, d+1))
                
                json_dict_obj = {semantic_label : data}


        # save MFCCs to json file
                with open(json_path + semantic_label + ".json", "w") as fp:
                    json.dump(json_dict_obj, fp, indent=4)
        
def crop_spectros(data_path):
    return
    
if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, num_segments=10)

