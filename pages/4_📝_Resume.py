import streamlit as st 
from PIL import Image

resume = "resume.pdf"
profile = "img\profile-pic.png"

with open(resume, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile)

#hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile, width=230)

with col2:
    st.title("SAMANTHA VIVIEN L. SERVO")
    st.write("Aspiring Data Scientist, advocate of data-driven business decison-making.")
    st.download_button(
        label="🗎 Download Resume",
        file_name='samantha-servo-resume.pdf',
        data=PDFbyte,
        mime="application/octet-stream"
    )
    st.write("📧: samanthaservo09@gmail.com")
    
