import streamlit as st
import numpy as np
import cv2

st.write("""
# Video Display 
""")

switch = st.select_slider("Video",options=["OFF","ON"],value="OFF")
position = st.empty()
if switch=="ON":
    vid = cv2.VideoCapture(0)
    while(True):
        _, frame = vid.read()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        position.image(frame)