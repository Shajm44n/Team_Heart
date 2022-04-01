import numpy as np
#from skimage.io import imread
import cv2
from keras.preprocessing import image
from skimage.transform import resize
from tensorflow import keras
import streamlit as st
from PIL import Image


#test_img=image.load_img("D:\\ECG Images dataset of Cardiac Patients\\Train\\normal\\normal(1).jpg",target_size=(64,64))
def main():
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file is not None:
        image=Image.open(uploaded_file)
        st.text("Uploaded Image")
        st.image(image)
        test_image = np.array(image, dtype='float32')
        test_image = cv2.resize(test_image, (64, 64), interpolation=cv2.INTER_CUBIC)

        test_image = np.expand_dims(test_image, axis=0)
        model = keras.models.load_model('ecg_model_binary.h5')
        result=model.predict(test_image)
        print(result)
        if result[0][0]==0:
            prediction='<p style="font-family:Courier; color:Red; font-size: 42px;font-weight: bold;">heart blockage detected</p>'
            print(prediction)
            st.write(prediction, unsafe_allow_html=True)
            doc = '<p style="font-family:Courier; color:White; font-size: 24px;font-weight: bold;">Book an appointment with our doctor immediately</p>'
            st.write(doc, unsafe_allow_html=True)

        else:
            prediction='<p style="font-family:Courier; color:White; font-size: 42px;font-weight: bold;">healthy heart</p>'
            print(prediction)
            st.write(prediction, unsafe_allow_html=True)
    







