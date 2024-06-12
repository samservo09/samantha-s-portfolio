import streamlit as st 
from pathlib import Path

st.title("Welcome to my projects!")

st.markdown("*Note: Everything here is still in progress. I will soon add my other future personal projects!*")

st.subheader("Spreadsheet Projects")

#define image path
cwd = Path.cwd()
img_dir = cwd / 'img'
image_path2 = img_dir / 'project1 .png'

col1, col2 = st.columns(2, gap="small")

with col1:
    #insert project picture
    if image_path2.exists() and image_path2.is_file():
        st.image(str(image_path2), width=350)  # Convert Path object to string

with col2:
    st.subheader("Financing a car purchase: Loan Amortization Schedule")
    st.write("Based from the book of Michael Sullivan, the College Algebra book, This spreadsheet will help you see a loan amortization schedule based on your inputs. You can make a copy of this google sheet and try it for yourself. I will add more features in the future.")
    st.markdown("[View my writeup about this project](https://docs.google.com/document/d/1552xpUEApxE5wLxYQyQ_nDUPJDdAffuXeackkw_0myM/edit?usp=sharing)")
    st.markdown("[Visit Project](https://docs.google.com/spreadsheets/d/1CMnNx5sVJJMRzZz5heCcvJBlZb9HO1w7LXwPK87dOEI/edit?usp=sharing)")
    

st.subheader("Python Projects")
#define image path
cwd = Path.cwd()
img_dir = cwd / 'img'
image_path2 = img_dir / 'project2.png'

col1, col2 = st.columns(2, gap="small")

with col1:
    #insert project picture
    if image_path2.exists() and image_path2.is_file():
        st.image(str(image_path2), width=350)  # Convert Path object to string

with col2:
    st.subheader("Stoicsim Quote Generator: Send a daily quote to your email!")
    st.write("I have used a stoic API to generate the random quotes. You can try and start receiving a random stoic quote!")
    st.markdown("[View my writeup about this project](https://docs.google.com/document/d/1qAS0TvFBrZcxB97Wa6A9cP0m5uilu7tOH7y8FE5d6og/edit?usp=sharing)")
    st.markdown("[Visit Project](https://github.com/samservo09/stoic-quote-generator.git)")

st.subheader("SQL Projects")
#define image path
cwd = Path.cwd()
img_dir = cwd / 'img'
image_path2 = img_dir / 'project2.png'

col1, col2 = st.columns(2, gap="small")

with col1:
    #insert project picture
    if image_path2.exists() and image_path2.is_file():
        st.image(str(image_path2), width=350)  # Convert Path object to string

with col2:
    st.subheader("Private Library Directory")
    st.write("I have created a private library directory using SQL. This will contain all the books that I have read and am currently reading! Note: This project is in progress!")
    st.markdown("[View my writeup about this project](https://docs.google.com/document/d/1XKPJXlA7XucW49Mdqz8XRTfev_7jqTMb1JhBah4JM9M/edit?usp=sharing)")
    st.markdown("[Visit Project] to be added!")

st.subheader("Data Visualization Projects")
st.markdown("soon to be added")

st.subheader("End-to-end Data Science Project")
st.markdown("soon to be added")