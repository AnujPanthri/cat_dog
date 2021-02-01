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
    data=request.get_json(force=True)
    length=len(data)
    print("len",length)
    allimg=[]
    for i in range(length):
        s=str(i)
        im_b64 = data[s][0] 
        im_b64=bytes(im_b64,'ascii')
        de=base64.b64decode(im_b64)
        buf=io.BytesIO(de)
        img=Image.open(buf)
        temparr=array(img)
        temparr=temparr.reshape([-1,150,150,3])
        print("len:",temparr.shape)
        if i==0:
            allimg=temparr
        else:
            allimg=np.concatenate((allimg,temparr))
    print("all",allimg.shape)
    allimg = allimg.astype('float32')
    allimg = allimg/255
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
    return jsonify(data)

if __name__ == '__main__' :
    app.run(debug=True)
