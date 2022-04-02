import streamlit as st
import pandas as pd
import appv6
import streamlit as st
import ecg_predict_streamlit
import home


# Security
#passlib,hashlib,bcrypt,scrypt



def add_userdata(new_user,email_id,mob_no,new_password,confirm_password):
    if new_user == "" or email_id == "" or mob_no == "" or new_password == "" or confirm_password == "":
        st.warning("All Fields Are Required")
    elif new_password != confirm_password:
        st.warning("Password and Confirm Password Should Be Same")
    else:

        with open('LoginSystemData_st.json', 'a') as f:
            f.write(new_user + "," + email_id + "," + mob_no + "," + new_password + "," + confirm_password + "\n")
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")

def login_user(username,password):
    if username == "" or password == "":
        st.warning("All Fields Are Required")
    else:
        with open('LoginSystemData_st.json', 'r') as f:
            readable = f.read()  # --> you need to readable:str your file
            lines = readable.splitlines()  # --> ['name,pw','name,pw','name,pw']
            user = list(filter(lambda l: l.split(',')[0] == username and l.split(',')[3] == password,lines))
            if user:
                return user
            else:
                st.warning('Invalid Username And Password')
            f.close()




def main():
    st.title("Heart Health Assistance")
    menu = ["Login","SignUp"]
    choice = st.sidebar.selectbox("SignUp/Login",menu)
    # if choice == "Home":
    #     st.subheader("Home")
    if choice == "Login":
        text = '<p style="font-family:Courier; color:White; font-size: 20px;font-weight: Italic;">Remove All Your Doubts in Matters of Heart</p>'
        st.write(text, unsafe_allow_html=True)
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            result = login_user(username,password)
            if result:

                PAGES = {


                    "Home" :home,
                    "Chat": appv6,
                    "Upload": ecg_predict_streamlit

                }
                st.subheader("Hi {}".format(username) +".....!")
                
                st.sidebar.title('Navigation')
                selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
                page = PAGES[selection]
                page.main()
            else:
                st.warning("Incorrect Username or Password")
    elif choice == "SignUp":
        st.subheader("Create New Account")
        new_user = st.text_input("Username")
        email_id = st.text_input("Email Id")
        mob_no = st.text_input("Mobile Number")
        new_password = st.text_input("Password", type='password')
        confirm_password = st.text_input("Confirm Password", type='password')
        if st.button("Signup"):
            add_userdata(new_user,email_id,mob_no,new_password,confirm_password)


if __name__ == '__main__':
	main()