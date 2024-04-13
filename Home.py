import streamlit as st  

st.set_page_config(
    page_title="Samantha Servo's Portfolio",
    page_icon="👾",
)

st.sidebar.success("Select a page above.")

st.title("Beyond the Vernaculum")
st.write("SAMANTHA SERVO")

#insert my profile picture
st.image("img\profile-pic.JPG", caption="My profile picture", width=230)
