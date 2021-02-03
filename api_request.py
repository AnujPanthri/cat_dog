import requests
import base64
from numpy import array
import numpy as np
from PIL import Image
import json
from io import BytesIO
import matplotlib.pyplot as plt

url="https://ai-cat-dog-classifier.herokuapp.com/api/"
stri=['ap1.jpg','new.jpg']
# img=Image.open( stri[0],mode="r" )
# img1=Image.open(r"ankur panthri.jpg")
image=[]
img64=[]
payload={}


# im_file = BytesIO()
# sun.save(im_file, format="JPEG")
# im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
# im_b4 = base64.b64encode(im_bytes)

for i in range(len(stri)):
    tempimg=Image.open(stri[i])
    image.append(tempimg.resize([150,150]))
    im_file = BytesIO()
    image[i].save(im_file,format="JPEG")
    im_bytes = im_file.getvalue()
    #arr[i]=arr[i]/255
    img64.append(base64.b64encode(im_bytes))
    #payload = {'image': img64[0], 'image1': img64[1]}
    payload[i]=img64[i].decode("ascii")
    print(i)
# print(len(img64[0]))
print(type(payload))
#print(payload)
r=requests.post(url,json=payload)
print(r.json())
