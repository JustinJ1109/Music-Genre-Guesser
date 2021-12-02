from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
from h5py._hl.files import File
import test as t
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", methods=['GET', 'POST'])
def index():
    file: File = None
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File upload successful! Please go back and refresh."

    else :
        print("reaching else")
        if(os.listdir(UPLOAD_FOLDER)) != 0:
            print(file)   
            genre, percentage = t.predict(file)
            print("ran python script")
            predictions = {
            "data": [
            {
                "genre1": genre[0],
                "percentage1": percentage[0]  
            },
            {
                "genre2": genre[1],
                "percentage2": percentage[1] 
            },
            {
                "genre3": genre[2],
                "percentage3": percentage[2]
            }
            ]
        }
            return predictions
        return ""
       
        



if __name__ == '__main__':
   app.run(debug=True)