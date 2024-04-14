import streamlit as st 

st.title("Welcome to my projects!")

st.markdown("*Note: Everything here is still a placeholder. I will soon add my personal projects!*")

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image("img\project1.jpg", width=230)

with col2:
    st.subheader("Project 1")
    st.write("Project description here.")
    st.markdown("[Visit Github Repo](https://github.com/samservo09/samantha-s-portfolio.git)")