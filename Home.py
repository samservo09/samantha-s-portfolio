import streamlit as st  

st.set_page_config(
    page_title="Samantha Servo's Portfolio",
    page_icon="👾",
)

st.sidebar.success("Select a page above.")

#division of two different contents
col1, col2 = st.columns(2, gap="small")
with col1:
    st.title("Beyond the Vernaculum")
    st.write("SAMANTHA SERVO")

with col2:
    #insert my profile picture
    st.image("img\profile-pic.JPG", caption="My profile picture", width=230)

#short description about me and my site
st.write("I am an aspiring Data Scientist.")