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
st.write(f"Image path: {image_path}")

# Check if the file exists
if image_path.exists() and image_path.is_file():
    st.write("Image file found.")
else:
    st.error(f"Image file not found: {image_path}")

#division of two different contents
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title("BEYOND THE VERNACULUM")
    st.write("Samantha Servo")

with col2:
    #insert my profile picture
    if image_path.exists() and image_path.is_file():
        st.image(str(image_path), width=230)  # Convert Path object to string

#short description about me and my site
st.write("I am an aspiring Data Scientist.")
