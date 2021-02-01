# -*- coding: utf-8 -*-
## Importing Libraries
import numpy as np
from numpy import array
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

app=flask.Flask(__name__)
app.config["DEBUG"]=True
#predicting from loaded trained_model


@app.route('/')
def home():
    return "<h1>working</h1>"


@app.route('/api/',methods=['POST'])
def classifier():
    data=request.get_json(force=True)
    length=len(data)
    print("len",length)
    allimg=[]
    for i in range(length):
        s=str(i)
        im_b64 = data[s]
        im_b64=im_b64.encode('ascii')
        de=base64.b64decode(im_b64)
        buf=io.BytesIO(de)
        img=Image.open(buf)
        print(img)
        #img.show()
        temparr=array(img)
        temparr=temparr.reshape([-1,150,150,3])
        print("len:",temparr.shape)
        if i==0:
            allimg=temparr
        else:
            allimg=np.concatenate((allimg,temparr))
    print("all",allimg.shape)
    #allimg = allimg.astype('float32')
    allimg = allimg/255
    print("all image array",allimg)
    predictions=model.predict(allimg)
    result=[]
    predictions=np.ndarray.flatten(predictions)
    print(predictions.shape)
    i=0
    
    for i in range(len(predictions)):
        n=predictions[i]
        n=str(n)
        print("value:",n)

        #print("see:",color_dict[n])
        result.append({'dog':n})
    print(result)
    return jsonify(result)

if __name__ == '__main__' :
    app.run(debug=True)
