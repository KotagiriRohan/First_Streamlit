import streamlit as st
import numpy as np
import cv2
import urllib
st.write("""
# Basic HSV Editing
""")
userinput = st.text_input("Enter the url of the Image")

if userinput:
    req = urllib.request.urlopen(userinput)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, 1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
default = [0,255]
Hue = st.slider('Hue',0,155,default)
Sat = st.slider('Saturation',0,155,default)
val = st.slider('Value',0,155,default)

l_b = np.array([Hue[0],Sat[0],val[0]])
u_b = np.array([Hue[1],Sat[1],val[1]])
if userinput:
    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(img,img,mask=mask)
    st.image(res)