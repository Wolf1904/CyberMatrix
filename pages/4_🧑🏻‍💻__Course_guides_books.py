import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
import time

st.set_page_config(page_title="Practical Books", page_icon="🧑🏻‍💻", layout="wide")

def local_CSS(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_CSS("style/style1.css")


st.header("Course Guides")
st.write("These guides helps you to gain the knowledge of the particular course.")
st.write('---')


st.subheader("Course Guide Books:")

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/compa+.jpeg")
    with text_column:
        st.subheader("The Official CompTIA A+ Core 1 and Core 2 Study Guide (Exams 220-1101 220-1102)")
        st.text("Author: James Pengelly")
        st.write(
            """
            Rigorously evaluated by third party subject matter experts to validate adequate coverage of the Core 1 exam objectives, the Official CompTIA A+ Core 1 & 2 Study Guide teaches the …
            """
            )
        button = st.button('*Generate link*', key = "1")
        if button:
            link = 'https://drive.google.com/file/d/1zvXL51wY3Vt8I8FIoApyLmZNq0yA4i4-/view?usp=drive_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/pwk.jpg")
    with text_column:
        st.subheader("PWK (PEN-200) - Official OffSec Course")
        st.text("Author: Offensive Security")
        st.write(
            """
            PWK (PEN-200) ethical hacking course overhaul: 33% more lab machines, double the content. PWK is a penetration testing certification designed by the minds behind Kali Linux. Real-world Benefits. Interactive Exercises. Active Student Forums. Industry-leading Training.
            """
            )
        button = st.button('*Generate link*', key = "2")
        if button:
            link = 'https://drive.google.com/file/d/1Xia2KtYrpyDqQ8jCJ73sW3pr9jYRoThS/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/ccna.jpg")
    with text_column:
        st.subheader("Cisco CCNA: Cisco Certified Network Associate (200-301)")
        st.text("Author: Cisco")
        st.write(
            """
            These courses cover network fundamentals, network access, IP connectivity, IP services, network security fundamentals, and laying the foundation for network automation and programmability.
            """
            )
        
    cloumn_1,column_2, column_3 = st.columns((1,2,2))
    with column_2:
        button = st.button('*Volume 1*', key = "3")
        if button:
            link = 'https://drive.google.com/file/d/1s2IlR0gVs4P4SRix0NUTbpJPGFTonQB2/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)
    with column_3:
        button = st.button('*Volume 2*', key = "4")
        if button:
            link = 'https://drive.google.com/file/d/1NsXfc4xY0MgdIaUFY-2qraeCorUvgEZJ/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)