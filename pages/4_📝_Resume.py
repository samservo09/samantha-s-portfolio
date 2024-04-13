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
    
#social links
st.write("#")
social_media = {
    "LinkedIn": "https://www.linkedin.com/in/samantha-servo-43625b18a",
    "Github": "https://github.com/samservo09",
    "Facebook": "https://www.facebook.com/profile.php?viewas=100000686899395&id=100002915061794"
}
cols = st.columns(len(social_media))
for index, (platform, link) in enumerate(social_media.items()):
    cols[index].write(f"[{platform}]({link})")

