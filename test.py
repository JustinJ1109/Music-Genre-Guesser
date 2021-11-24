import json
import numpy as np
import os

DATA_PATH = "preProcessedData/"

predictions = {}

for x in os.listdir(DATA_PATH):
    predictions.update({x[:-5] : 0})
    
print(predictions.keys())


