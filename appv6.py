import streamlit as st 
from streamlit_chat import message
import time
import processor
import csvpred
import ecg_predict_streamlit
from PIL import Image
from skimage.io import imread
from keras.preprocessing import image
     





def main():
    #count = 0
    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    if 'past' not in st.session_state:
        st.session_state['past'] = []
    st.write(f"Initialize the Chat bot By Typing Hi ")
   # placeholder = st.empty()  # placeholder for latest message
    user_in = st.text_input("Start your chat here")
    bot_reply = processor.chatbot_response(user_in)

    st.session_state.past.append(user_in)
    st.session_state.generated.append(bot_reply)


    if st.session_state['generated']:

        for i in range(len(st.session_state['generated'])-1, -1, -1):
            message(st.session_state["generated"][i], key=str(i))
            #time.sleep(1)
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            if "heart disease" in (st.session_state['generated'][i]):
                user_csv()
                break
# def resume_chat():
#     resume_chat = st.radio('Do you want to continue with our medbot ', ('Yes', 'No'))
#     if resume_chat == 'Yes':
#         main()
#     else:
#         st.write('Thank you for your valuable time.........!')




def user_csv():
    count=0
    age = st.slider('How old are you?', 0, 130, 45, key=count)
    st.write('You selected:', age)
    height = st.slider('whats your height?', 0, 200, 150)
    st.write('You selected:', height)
    weight = st.slider('whats your weight?', 0, 200, 60)
    st.write('You selected:', weight)
    gender = st.radio('what is your Gender?',('Male', 'Female'))
    st.write('You selected:', gender)
    sys_bp = st.slider('whats your systolic bp?', 0, 200, 140)
    st.write('You selected:', sys_bp)
    dia_bp = st.slider('whats your diastolic bp?', 0, 200, 80)
    st.write('You selected:', dia_bp)
    cholestrol = st.selectbox('Your cholestrol level',('1: normal', '2: above normal', '3: well above normal'))
    st.write('You selected:', cholestrol)
    glucose =  st.selectbox('Your glucose level',('1: normal', '2: above normal', '3: well above normal'))
    st.write('You selected:', glucose)
    smoke = st.radio('do you smoke',('Yes', 'No'))
    st.write('You selected:', smoke)
    alcohol = st.radio('do you drink',('Yes', 'No'))
    st.write('You selected:', alcohol)
    physical_activity = st.selectbox('Physical Activity',('Yes', 'No'))
    st.write('You selected:', physical_activity)
    # option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
    # st.write('You selected:', option)
    submit = st.button('Predict')
    if submit:
        h_value = csvpred.preprocess([age,gender,height,weight,sys_bp,dia_bp,cholestrol,glucose,smoke,alcohol,physical_activity])
        if h_value == 1:
            text = '<p style="font-family:Courier; color:Red; font-size: 42px;font-weight: bold;">You are in danger!!</p>'
            st.write(text, unsafe_allow_html=True)
            text2 = '<p style="font-family:Courier; color:white; font-size: 24px;font-weight: bold;">Please Navigate to ECG upload section</p>'
            st.write(text2, unsafe_allow_html=True)

        elif h_value == 0:
            st.write('You are safe!!')



if __name__=="__main__":
    st.title("Rule based Chatbot")
    st.subheader("This is a Rule based Chatbot made using NlTK and Python by Team Heart ")
    main()




