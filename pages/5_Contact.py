import streamlit as st 

st.header(":mailbox: Get In Touch With Me!")

#link for connecting my form to formsubmit's endpoint
contact_form = """
<form action="https://formsubmit.co/samanthaservo09@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit">Send</button>
</form>
"""

#inject the HTML code into my website
st.markdown(contact_form, unsafe_allow_html=True)

#use local css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style.css")

