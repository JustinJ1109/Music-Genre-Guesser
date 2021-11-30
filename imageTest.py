from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
CORS(app)


weather = {
    "data": [
    {
        "genre1": "Country",
        "percentage1": "50"  
    },
    {
        "genre2": "Pop",
        "percentage2": "30"
    },
    {
        "genre3": "Rock",
        "percentage3": "20"
    }
    ]
}


@app.route("/", methods=['GET'])
def index():
    return weather

@app.route("/", methods=['GET'])
def WeatherReport():
    global weather
    return jsonify([weather])

if __name__ == '__main__':
   app.run(debug=True)