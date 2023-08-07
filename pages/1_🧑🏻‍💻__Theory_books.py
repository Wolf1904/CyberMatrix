import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
import time

st.set_page_config(page_title="Theory Books", page_icon="🧑🏻‍💻", layout="wide")

def local_CSS(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_CSS("style/style1.css")


st.header("Theory Books")
st.write("These ebooks contains theoritical knowledge and provides analysis of Hacking.")
st.write('---')


st.subheader("eBooks:")

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/cpcs.jpg")
    with text_column:
        st.subheader("Computer Programming And Cyber Security for Beginners")
        st.text("Author: Zach Codings")
        st.write(
            """
            Do you feel that informatics is indispensable in today's increasingly digital world? Do you want to introduce yourself to the world of programming or cyber security but don't know where to get started? ...
            """
            )
        button = st.button('*Generate link*', key = "1")
        if button:
            link = 'https://drive.google.com/file/d/1u3Un6CSCHWIMxc3YeuwJS2AMP8RjK3ji/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)
            
with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/tbp.jpg")
    with text_column:
        st.subheader("The Pentester BluePrint")
        st.text("Author: Phillip L. Wylie, Kim Crawley")
        st.write(
            """
            JUMPSTART YOUR NEW AND EXCITING CAREER AS A PENETRATION TESTER The Pentester BluePrint: Your Guide to Being a Pentester offers readers a chance to delve deeply into the world of the ethical, or "white-hat" hacker. ...
            """
            )
        button = st.button('*Generate link*', key = "2")
        if button:
            link = 'https://drive.google.com/file/d/1HvM3BUBHfEOes10JIEPzdRBoffIkjaWI/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/se.jpg")
    with text_column:
        st.subheader("Social Engineering: The Art of Human Hacking")
        st.text("Author: Christopher Hadnagy")
        st.write(
            """
            The first book to reveal and dissect the technical aspect of many social engineering maneuvers From elicitation, pretexting, influence and manipulation all aspects of social engineering are picked apart, ...
            """
            )
        button = st.button('*Generate link*', key = "3")
        if button:
            link = 'https://drive.google.com/file/d/11tqC4nT5N9mt0ZaKGNnrAF2Fl9bMnJqt/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/bst.jpg")
    with text_column:
        st.subheader("Basic Security Testing with Kali Linux 2")
        st.text("Author: Daniel W. Dieterle")
        st.write(
            """
            Basic Security Testing with Kali Linux 2 Kali Linux 2 (2016) is an Ethical Hacking platform that allows good guys to use the same tools and techniques that a hacker would use, so they can find security issues before the bad guys do. ...
            """
            )
        button = st.button('*Generate link*', key = "4")
        if button:
            link = 'https://drive.google.com/file/d/1ExTmqgkNQiSWpst2tUyvI0dE-17ymex3/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/mpt.jpg")
    with text_column:
        st.subheader("Metasploit Penetration Testing Cookbook")
        st.text("Authors: Abhinav Singh · Monika Agarwal")
        st.write(
            """
            This is a Cookbook which follows a practical task-based style. There are plenty of code and commands used for illustration which make your learning curve easy and quick.This book targets both professional penetration testers as well as new users of Metasploit who wish to gain expertise over the framework. ...
            """
            )
        button = st.button('*Generate link*', key = "5")
        if button:
            link = 'https://drive.google.com/file/d/1ZjLuWM32BRiWIie6LxD9ssBk8msgbJyP/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/thp.jpg")
    with text_column:
        st.subheader("The Hacker Playbook 3")
        st.text("Author: Peter Kim")
        st.write(
            """
            Back for the third season, The Hacker Playbook 3 (THP3) takes your offensive game to the pro tier. With a combination of new strategies, attacks, exploits, tips and tricks, you will be able to put yourself in the center of the action toward victory. ...
            """
            )
        button = st.button('*Generate link*', key = "6")
        if button:
            link = 'https://drive.google.com/file/d/1dTEbQgmvOp2qyK1s3QokvIbSsUgbHPjG/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/nse.jpg")
    with text_column:
        st.subheader("Network Security Essentials")
        st.text("Author: William Stallings")
        st.write(
            """
            Network Securities Essentials: Applications and Standards introduces students to the critical importance of Internet security in our age of universal electronic connectivity. Amidst viruses, hackers and electronic fraud, organizations and individuals are constantly at risk of having their private information compromised...
            """
            )
        button = st.button('*Generate link*', key = "12")
        if button:
            link = 'https://drive.google.com/file/d/1BqpJFS_L_ZAiX9GPR31cfmtSjNPlS2-2/view?usp=drive_link'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

st.write("---")
st.write("###")
st.subheader("Bonus Book")

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/tcb.jpg")
    with text_column:
        st.subheader("The Code Book")
        st.text("Author: Simon Singh")
        st.write(
            """
            The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography is a book by Simon Singh, published in 1999 by Fourth Estate and Doubleday. The Code Book describes some illustrative highlights in the history of cryptography, drawn from both of its principal branches, codes and ciphers.
            """
            )
        button = st.button('*Generate link*', key = "9")
        if button:
            link = 'https://drive.google.com/file/d/1Evgfe9Os6F-ZHTzc_N8q8j3-qSWjBCTC/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(2)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)
