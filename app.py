import numpy as np
import flask
from flask import request, jsonify
# Importing Tensorflow
import tensorflow as tf
import base64
import io
from PIL import Image

#print(tf.__version__)

"""## Loading Trained Model"""
# Recreate the exact same model, including its weights and the optimizer
model = tf.keras.models.load_model('imgmodel.h5') 

"""## Initializing Color Classes for Prediction"""

# Mapping the Color Index with the respective 11 Classes (More Explained in RGB Color Classifier: Part 1)

app=flask.Flask(__name__)
#app.config["DEBUG"]=True
#predicting from loaded trained_model


@app.route('/')
def home():
    return "<h2>hi dear</h2>"


@app.route('/api/',methods=['POST'])
def classifier():
    return jsonify("resultfromdog")


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
