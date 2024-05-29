import streamlit as st  
from pathlib import Path

st.set_page_config(
    page_title="Samantha Servo's Portfolio",
    page_icon="👾",
)

st.sidebar.success("Select a page above.")

st.markdown("🚧 *Note: This website portfolio is under construction.* 🚧")

#define image path
cwd = Path.cwd()
img_dir = cwd / 'img'
image_path = img_dir / 'profile-pic.png'

#division of two different contents
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title("BEYOND THE VINCULUM")
    st.write("Samantha Servo")

with col2:
    #insert my profile picture
    if image_path.exists() and image_path.is_file():
        st.image(str(image_path), width=230)  # Convert Path object to string

#short description about me and my site
st.write("Hello! I am an aspiring Data Analyst/Scientist.")
st.write("I also consider myself as an autodidact and multipotentialite. An outlier, beyond the vinculum! Why those things? I love teaching myself (autodidact) about the different interests (multipotentialite) that I have.")
st.write("I taught myself both in creative and technical hobbies that I have. I won't enumerate them here because they're a lot! Just imagine how many I have that I have a Notion page just to manage them all. That's how I love learning. In this website portfolio, DATA SCIENCE/ANALYSIS is our star.")
st.write("I want to use my diverse knowledge and skills in helping businesses have a numerical vision of their current standing.")