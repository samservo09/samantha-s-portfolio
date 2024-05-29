import streamlit as st 
from PIL import Image
from pathlib import Path

resume = "resume.pdf"

with open(resume, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

#define image path
cwd = Path.cwd()
img_dir = cwd / 'img'
image_path = img_dir / 'profile-pic.png'

#hero section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(image_path, width=230)

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

#skills section
st.write("#")
st.subheader("Skills")
st.write(
    """
    Technical skills:
    
    Python | Jupyter Notebook | Google Colaboratory | SQL | Microsoft Office (Word, Excel, and Powerpoint) | Dialogflow | Git | HTML | CSS
    
    Business skills:
    
    Intelligence | Detail-oriented | Project Management Skills | Growth mindset | Good communication skills
    """
)

#experience section
st.write("#")
st.subheader("Experience")
st.write(
    """
    > 2022 - Present
    
    Data Committee | Google Developer Students Clubs | Pamantasan ng Lungsod ng Maynila 
    
    • Appointed as a committee manager
    • Assisted with Data Camp incoming scholars' application
    
    > 2021 - 2022
    
    AI/ML Committee | Google Developer Students Clubs | Pamantasan ng Lungsod ng Maynila 
    
    • Participated in study jams about Artificial Intelligence and Machine Learning.
    • Participated in PLM-Google Developer Students Clubs events.
    
    > November 2022 - December 2022
    
    Virtual Apprentice | Iceberg Insulated
    
    • Learned to apply sales forecasting to the given historical data of the company.
    • Application of data visualization and data cleaning through Python and spreadsheets (mainly Google Sheets).
    • Built a dashboard page for Iceberg employees to track sales and inventory using Google Sheets.

    > May 2022 - June 2022
    
    Virtual Apprentice | Dashlabs.ai
    
    • Exposed to new technologies such as Dialogflow, node.js, and socket.io by creating a chatbot. 
    • Improved understanding of Dashlabs.ai as a company and its customers.
    • Learned the importance of interaction flow for understanding consumers/costumers when creating a chatbot.
    """
)

#education
st.write("#")
st.subheader("Education")
st.write(
    """
    > September 2021 - June 2025
    Bachelor of Science in Computer Science | Pamantasan ng Lungsod ng Maynila | Intramuros, Manila
    """
)

#licenses and certifications
st.write("#")
st.subheader("Licenses and Certifications")
st.write(
    """
    > Certified in Cybersecurity
    
    International Information System Security Certification Consortium (ISC)² (Issued: 04/2023 - Expires: 04/26)
    
    > Completed DOST SPARTA’s Data Science Pathway
    
    Smarter Philippines through Data Analytics, R&D, Training, and Adoption This initiative is the result of a collaborative effort among the Department of Science and Technology (DOST), Development Academy of the Philippines (DAP), Analytics Association of the Philippines (AAP), and Coursebank, supervised by the DOST-Philippine Council for Industry, Energy, and Emerging Technology Research and Development (DOST-PCIEERD).
    
    """
)

#others
st.write("#")
st.subheader("Others")
st.write(
    """
    > Second Placer Hack-Attack: Won 2nd prize with my group, Econnovators through the development of EnableU for the PLM-GDSC ideathon (02/2023)
    
    > DOST-SEI S&T RA 7687: Qualified for DOST (Department of Science and Technology) 2021 Scholarship Program
    
    > DataCamp Scholar: Awarded with one year of free access to 350+ courses and tracks in the DataCamp Platform.
    """
)
