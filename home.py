import streamlit as st 


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://images.pexels.com/photos/4386466/pexels-photo-4386466.jpeg?cs=srgb&dl=pexels-karolina-grabowska-4386466.jpg&fm=jpg");
            filter: blur(-1px);
            background-size: cover
             
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def main():     
    set_bg_hack_url()
    
    #st.title("Heart Disease Prediction with Medbot")
    txt = "<p style='font-size: 40px;color:darkslategray;'>Cardiovascular diseases</p>"
    st.write(txt, unsafe_allow_html=True)
    text = "<p style='font-family:Garamond ; color:maroon;font-weight: bold; font-size: 32px;'>Cardiovascular disease (CVD) remains the world’s number one killer, resulting in 18.6 million deaths a year. It has many causes: from smoking, diabetes, high blood pressure and obesity, to air pollution. For the 520 million people living with CVD, COVID-19 has been heartbreaking. They have been more at risk of developing severe forms of the virus. And many have been afraid to attend routine and emergency appointments, and have become isolated from friends and family.</p>"
    st.write(text, unsafe_allow_html=True)

