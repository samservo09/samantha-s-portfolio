import streamlit as st 
from pathlib import Path

st.title("Welcome to my projects!")

st.markdown("*Note: Everything here is still in progress. I will soon add my other future personal projects!*")

st.subheader("Excel Projects")

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
    st.markdown("[Visit Google Sheet](https://docs.google.com/spreadsheets/d/1CMnNx5sVJJMRzZz5heCcvJBlZb9HO1w7LXwPK87dOEI/edit?usp=sharing)")
    

st.subheader("Python Projects")
st.markdown("soon to be added")

st.subheader("SQL Projects")
st.markdown("soon to be added")

st.subheader("PowerBI Projects")
st.markdown("soon to be added")

st.subheader("End-to-end Data Science Project")
st.markdown("soon to be added")