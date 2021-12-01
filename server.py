from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

import os

app = Flask(__name__)
CORS(app)

genre1 = "Country"
genre2 = "Pop"
genre3 = "Rock"
percentage1 = 50
percentage2 = 30
percentage3 = 20

UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



weather = {
    "data": [
    {
        "genre1": genre1,
        "percentage1": percentage1  
    },
    {
        "genre2": genre2,
        "percentage2": percentage2
    },
    {
        "genre3": genre3,
        "percentage3": percentage3
    }
    ]
}


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return "File upload successful! Please go back and refresh."

    else :
        return weather


if __name__ == '__main__':
   app.run(debug=True)