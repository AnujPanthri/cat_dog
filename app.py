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
model = tf.keras.models.load_model('imgmodel.h5') 

"""## Initializing Color Classes for Prediction"""

app=flask.Flask(__name__)
#app.config["DEBUG"]=True
#predicting from loaded trained_model


@app.route('/')
def home():
    return "<h1>working</h1>"


@app.route('/api/',methods=['POST'])
def predict_color():
    print("wo")
    return jsonify("re")

if __name__ == '__main__' :
    app.run(debug=True)
