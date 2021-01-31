from flask import Flask,jsonify,request
from PIL import Image
from numpy import array
import numpy as np
import base64
import io
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


app=Flask(__name__)
model = tf.keras.models.load_model('imgmodel.h5') 
@app.route('/')
def home():
    return "<h2>hi dear</h2>"

@app.route('/c_d/',methods=['POST'])
def classifier():
    data=request.form.to_dict(flat=False)
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
    predictions=model.predict(allimg)
    result=[]
    i=0
    for i in range(len(predictions)):
        n=predictions[i]
        #print("see:",color_dict[n])
        result.append({'dog':n})
    return jsonify(result)
    #print("all",allimg.shape)
    # arr=array(img)
    #print('data',img)
    
    #img.show()
    
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
