import streamlit as st  
from pathlib import Path

st.set_page_config(
    page_title="Samantha Servo's Portfolio",
    page_icon="👾",
)

st.sidebar.success("Select a page above.")

#define image path
cwd = Path.cwd()
img_dir = cwd / 'img'
image_path = img_dir / 'profile-pic.png'

#division of two different contents
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title("BEYOND THE VERNACULUM")
    st.write("What is this place?")

with col2:
    #insert my profile picture
    if image_path.exists() and image_path.is_file():
        st.image(str(image_path), width=230)  # Convert Path object to string

#short description about me and my site
st.write("Welcome to my portfolio website! This is a website I have created to compile and showcase all information about me. That includes my projects so you can see how we can work together in the future!")