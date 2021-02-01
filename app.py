# -*- coding: utf-8 -*-
## Importing Libraries
import numpy as np
import flask
from flask import request, jsonify
# Importing Tensorflow
import tensorflow as tf

#print(tf.__version__)

"""## Loading Trained Model"""
# Recreate the exact same model, including its weights and the optimizer
model = tf.keras.models.load_model('imgmoel.h5') 

"""## Initializing Color Classes for Prediction"""

app=flask.Flask(__name__)
#app.config["DEBUG"]=True
#predicting from loaded trained_model


@app.route('/')
def home():
    return "<h1>working</h1>"


@app.route('/api/',methods=['POST'])
def predict_color():
    data=request.get_json(force=True)
    print("wo")
    return jsonify(data)

if __name__ == '__main__' :
    app.run(debug=True)
