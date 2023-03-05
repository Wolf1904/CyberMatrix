import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
import time

st.set_page_config(page_title="Cybersecurity Courses", page_icon="🧑🏻‍💻", layout="wide")

def local_CSS(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_CSS("style/style1.css")


st.header("Cybersecurity Courses")
st.write("These are some courses related to cybersecurity")
st.write('---')


st.subheader("Courses:")

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/a+.jpg")
    with text_column:
        st.subheader("A+ (Plus) Certification - CompTIA")
        st.text("Author: CompTIA")
        st.text("Provided by: Alison")
        st.write(
            """
            CompTIA A+ is the only industry recognized credential with performance testing to prove pros can think on their feet to perform critical IT support tasks.
            """
            )
        button = st.button('*Generate link*', key = "1")
        if button:
            link = 'https://alison.com/tag/comptia-a+?utm_source=google&utm_medium=cpc&utm_campaign=PPC_Tier-4_First-Click_Courses-_Broad_&utm_adgroup=Tag_Comptia-A+&gclid=CjwKCAiAh9qdBhAOEiwAvxIokyITkjo2gRXcMION5CPwjJtlRTZhuOg5ciVxfoTe0eeS3lBWY5wCXhoCNNoQAvD_BwE'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to open Course...</a>'
            html(hyperlink, height=30)
            
with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/n+.jpg")
    with text_column:
        st.subheader("Security+ (Plus) Certification - CompTIA")
        st.text("Author: CompTIA")
        st.text("Provided by: Alison")
        st.write(
            """
            CompTIA Security+ is the first security certification a candidate should earn. It establishes the core knowledge required of any cybersecurity role and ...
            """
            )
        button = st.button('*Generate link*', key = "2")
        if button:
            link = 'https://alison.com/course/comptia-security-exam-syo-501'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to open Course...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/s+.jpg")
    with text_column:
        st.subheader("CCNA - Training & Certifications - Cisco")
        st.text("Author: Cisco")
        st.text("Provided by: Alison")
        st.write(
            """
            CCNA exam covers networking fundamentals, IP services, security fundamentals, automation and programmability. Designed for agility and versatility, CCNA ...
            """
            )
        button = st.button('*Generate link*', key = "3")
        if button:
            link = 'https://alison.com/courses?query=ccna'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to open Course...</a>'
            html(hyperlink, height=30)

