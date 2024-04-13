import streamlit as st  

st.set_page_config(
    page_title="Samantha Servo's Portfolio",
    page_icon="👾",
)

st.sidebar.success("Select a page above.")

#division of two different contents
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title("BEYOND THE VERNACULUM")
    st.write("What is this place?")

with col2:
    #insert my profile picture
    st.image("img\profile-pic.png", width=230)

#short description about me and my site
st.write("Welcome to my portfolio website! This is a website I have created to compile and showcase all information about me. That includes my projects so you can see how we can work together in the future!")