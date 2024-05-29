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
    st.title("BEYOND THE VINCULUM")
    st.write("What is this place?")

with col2:
    #insert my profile picture
    if image_path.exists() and image_path.is_file():
        st.image(str(image_path), width=230)  # Convert Path object to string

#short description about me and my site
st.write("Welcome to my portfolio website! This is a website I have created to compile and showcase all information about me. That includes my projects so you can see how we can work together in the future!")

st.subheader("Why Beyond The Vinculum?")
st.write("In a summarized form: My brand is all about being beyond the traditional limitations or what is known.")
st.write("I am an explorer given my thirst for knowledge. I utilize this in order to learn skills necessary in helping others. In this context, in Data Science.")

st.subheader("What is a vinculum?")
st.write("Short version: a horizontal line used in mathematics for grouping purposes.")
st.write("In the book of Michael Sullivan's College Algebra, I first encountered this term. It is a bar placed atop an expression to indicate what we would now indicate with parentheses. In modern Math, the last survivor of usage of vinculum is the bar on top of the present radical symbol.")
st.write("So when I say Beyond the Vinculum, it means I am the person who will move beyond the traditional boundaries and limitations. An outlier, who will willingly explore the least explored path.")

st.subheader("FUNFACT: I used to HATE Mathematics!")
st.write("How contrasting, right? I want to work in a numerical heavy career yet I hated Math? Yes, in fact, I took the ABM (Accountancy and Business Management) strand in Senior High School. I was scared of Math. But something happened when I was in college that made me go back to Math. The root of my problem: Not understanding how to study Math. After failing a course in my program which is Math-heavy, I bought myself a College Algebra book, and taught myself again about Math! I'm still doing it now as you are reading it. (I want to finish the book!)")