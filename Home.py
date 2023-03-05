import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from PIL import Image


st.set_page_config(page_title="Cyber Assist", page_icon="🖥️", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---ASSETS---
lottie_ebooks = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_frJ5A7.json")
img_lottie_animation = Image.open("images/ncrm.jpg")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---SIDEBAR---
with st.sidebar:
    st.subheader("Stats of Malware and Phishing sites:")
    st.image("images/st.jpg")
    st.write("This chart - pulled from Google Safe Browsing - shows the steep increase in the number of websites deemed unsafe between January 2016 and January 2021.")

# ---CONTENT---
with st.container():
    st.subheader("Hi, I am Lucifer :smiling_imp:")
    st.title("A Student From India")
    st.write(
        "I am passionate about learning the ways to break and secure the Cyber Firewall."
    )
    st.write('###')

    left_column, right_column = st.columns(2)
    with right_column:
        st.header('Why you should learn Cybersecurity?')
        st.subheader("- Retain Customer Trust:")
        st.write(
            '''
            Learning cybersecurity will strengthen business security and protect customers’ data. A strong cybersecurity system will promote trust and retain customers.
            ''')
        st.subheader("- Staying Updated with New Threats:")
        st.write(
            '''
            As cyberattacks are growing more and more sophisticated, constantly learning and sharpening your skills in the field has become paramount.
            ''')
    with left_column:
        st_lottie(lottie_ebooks, height=300, key="computer") #---ANIMATION---

st.write('---')

# ---IN THIS SITE---
with st.container():
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.subheader('What will you find in this site?')
        st.write(
            '''
            You will find in this site:
            - eBooks related to Cybersecurity
            - A roadmap video (by "networkchuck")
            '''
        )
    with right_column:
        st.image("images/cs.jpg")


# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("The Hacker's Roadmap")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("The Hacker’s Roadmap (by networkchuck)")
        st.write(
            """
            - Do you want to become a Hacker? A Network Engineer? Cloud Engineer? System Administrator?
            - In this video, NetworkChuck will show you the path to getting started in IT and Cybersecurity that will help you reach these goals. 

            """
        )
        button = st.button('*Generate link*', key = "1")
        link = 'https://www.youtube.com/watch?v=uTAaFExLgwQ'
        if link:
            st.write(f'<a href="{link}" target="_blank">Click here...</a>', unsafe_allow_html=True)

# ---FORM---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/ed71b19657fbd311d7901ea9536cadfc" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


st.write("###")
st.write("###")
st.write("###")
st.write("*Note:- The Study Material Provided Is Not Ours And Belongs To Respective Owners.*")