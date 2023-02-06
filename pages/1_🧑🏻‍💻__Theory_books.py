import streamlit as st
from PIL import Image
import webbrowser


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
        st.write(
            """
            Do you feel that informatics is indispensable in today's increasingly digital world? Do you want to introduce yourself to the world of programming or cyber security but don't know where to get started? ...
            """
            )
        link = st.button('*Click here...*', key = "1")
        if link:
            webbrowser.open('https://drive.google.com/file/d/1u3Un6CSCHWIMxc3YeuwJS2AMP8RjK3ji/view?usp=share_link')
            
with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/tbp.jpg")
    with text_column:
        st.subheader("The Pentester BluePrint")
        st.write(
            """
            JUMPSTART YOUR NEW AND EXCITING CAREER AS A PENETRATION TESTER The Pentester BluePrint: Your Guide to Being a Pentester offers readers a chance to delve deeply into the world of the ethical, or "white-hat" hacker. ...
            """
            )
        link = st.button('*Click here...*', key = "2")
        if link:
            webbrowser.open('https://drive.google.com/file/d/1HvM3BUBHfEOes10JIEPzdRBoffIkjaWI/view?usp=share_link')

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/se.jpg")
    with text_column:
        st.subheader("Social Engineering: The Art of Human Hacking")
        st.write(
            """
            The first book to reveal and dissect the technical aspect of many social engineering maneuvers From elicitation, pretexting, influence and manipulation all aspects of social engineering are picked apart, ...
            """
            )
        link = st.button('*Click here...*', key = "3")
        if link:
            webbrowser.open('https://drive.google.com/file/d/11tqC4nT5N9mt0ZaKGNnrAF2Fl9bMnJqt/view?usp=share_link')

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/bst.jpg")
    with text_column:
        st.subheader("Basic Security Testing with Kali Linux 2")
        st.write(
            """
            Basic Security Testing with Kali Linux 2 Kali Linux 2 (2016) is an Ethical Hacking platform that allows good guys to use the same tools and techniques that a hacker would use, so they can find security issues before the bad guys do. ...
            """
            )
        link = st.button('*Click here...*', key = "4")
        if link:
            webbrowser.open('https://drive.google.com/file/d/1ExTmqgkNQiSWpst2tUyvI0dE-17ymex3/view?usp=share_link')

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/mpt.jpg")
    with text_column:
        st.subheader("Metasploit Penetration Testing Cookbook")
        st.write(
            """
            This is a Cookbook which follows a practical task-based style. There are plenty of code and commands used for illustration which make your learning curve easy and quick.This book targets both professional penetration testers as well as new users of Metasploit who wish to gain expertise over the framework. ...
            """
            )
        link = st.button('*Click here...*', key = "5")
        if link:
            webbrowser.open('https://drive.google.com/file/d/1ZjLuWM32BRiWIie6LxD9ssBk8msgbJyP/view?usp=share_link')

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/thp.jpg")
    with text_column:
        st.subheader("The Hacker Playbook 3")
        st.write(
            """
            Back for the third season, The Hacker Playbook 3 (THP3) takes your offensive game to the pro tier. With a combination of new strategies, attacks, exploits, tips and tricks, you will be able to put yourself in the center of the action toward victory. ...
            """
            )
        link = st.button('*Click here...*', key = "6")
        if link:
            webbrowser.open('https://drive.google.com/file/d/1dTEbQgmvOp2qyK1s3QokvIbSsUgbHPjG/view?usp=share_link')

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
        st.write(
            """
            The Code Book: The Science of Secrecy from Ancient Egypt to Quantum Cryptography is a book by Simon Singh, published in 1999 by Fourth Estate and Doubleday. The Code Book describes some illustrative highlights in the history of cryptography, drawn from both of its principal branches, codes and ciphers.
            """
            )
        link = st.button('*Click here...*', key = "9")
        if link:
            webbrowser.open('https://drive.google.com/file/d/1Evgfe9Os6F-ZHTzc_N8q8j3-qSWjBCTC/view?usp=share_link')
