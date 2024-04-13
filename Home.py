import streamlit as st  

st.set_page_config(
    page_title="Samantha Servo's Portfolio",
    page_icon="👾",
)

st.sidebar.success("Select a page above.")

container = st.beta_container()

with container:
    st.title("Beyond the Vernaculum")
    st.write("SAMANTHA SERVO")

with container:
    st.image("img\profile-pic.JPG", caption="My profile picture", use_column_width=True)
