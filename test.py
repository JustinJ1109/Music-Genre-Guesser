import imageio
import pathlib
import tensorflow as tf
import keras
from tensorflow._api.v2 import data
import numpy as np
import pandas as pd

# image shape - (288, 432, 4)

file_path = 'Data/images_original/'

def load_data(data_path):
    #https://stackoverflow.com/questions/60312574/how-to-read-multiple-directories-which-have-different-number-of-files-into-tenso
    base_dir = pathlib.Path(data_path)
    scenes = tf.data.Dataset.list_files(str(base_dir / '*'))

    for s in scenes:
        scene_dir = pathlib.Path(s.numpy().decode('utf-8'))
        images = scene_dir / '*.png'
        data = []
        for i in images:
            # features = [i['x1'], i['x2']] # ...
            # data.append(features)
            print(str(i))

load_data(file_path)