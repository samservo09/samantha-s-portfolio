import streamlit as st 
from pathlib import Path

st.title("Welcome to my projects!")

st.markdown("*Note: Everything here is still a placeholder. I will soon add my personal projects!*")

#define image path
cwd = Path.cwd()
img_dir = cwd / 'img'
image_path2 = img_dir / 'project1.jpg'

col1, col2 = st.columns(2, gap="small")
with col1:
    #insert project picture
    if image_path2.exists() and image_path2.is_file():
        st.image(str(image_path2), width=230)  # Convert Path object to string

with col2:
    st.subheader("Project 1")
    st.write("Project description here.")
    st.markdown("[Visit Github Repo](https://github.com/samservo09/samantha-s-portfolio.git)")