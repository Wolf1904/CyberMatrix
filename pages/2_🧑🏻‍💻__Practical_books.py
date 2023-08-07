import streamlit as st
from PIL import Image
from streamlit.components.v1 import html
import time

st.set_page_config(page_title="Practical Books", page_icon="🧑🏻‍💻", layout="wide")

def local_CSS(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_CSS("style/style1.css")


st.header("Practical Books")
st.write("These ebooks contains practical knowledge and provides hands-on experience on Hacking.")
st.write('---')


st.subheader("eBooks:")

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/pt.jpg")
    with text_column:
        st.subheader("Penetration testing : a hands-on introduction to hacking")
        st.text("Author: Georgia Weidman")
        st.write(
            """
            Penetration testers simulate cyber attacks to find security weaknesses in networks, operating systems, and applications. ...
            """
            )
        button = st.button('*Generate link*', key="1")
        if button:
            link = 'https://drive.google.com/file/d/1TSEsVeUGG8g9j5j3zqTjd3A1HJ4Qa_at/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/rtfm.png")
    with text_column:
        st.subheader("RTFM: Red Team Field Manual")
        st.text("Author: Ben Clark")
        st.write(
            """
            The Red Team Field Manual (RTFM) is a no fluff, but thorough reference guide for serious Red Team members who routinely find themselves on a mission without Google or the time to scan through a man page. ...
            """
            )
        button = st.button('*Generate link*', key = "3")
        if button:
            link = 'https://drive.google.com/file/d/1hGn4IqbKOVrcQc0DZXmrIpyGroUESCq7/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/ghp.jpg")
    with text_column:
        st.subheader("Gray hat Python : Python programming for hackers and reverse engineers")
        st.text("Author: Justin Seitz")
        st.write(
            """
            Python is fast becoming the programming language of choice for hackers, reverse engineers, and software testers because it's easy to write quickly, and it has the low-level support and libraries that make hackers happy. But until now, there has been no real manual on how to use Python for a variety of hacking tasks. ...
            """
            )
        button = st.button('*Generate link*', key = "4")
        if button:
            link = 'https://drive.google.com/file/d/1RZlrZCQkv3we7pREM7A0Yt1i2Gc06oPm/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/mac.jpg")
    with text_column:
        st.subheader("Malware Analyst's Cookbook and DVD: Tools and Techniques for Fighting Malicious Code")
        st.text("Authors: Steven Adair, Michael Hale Ligh")
        st.write(
            """
            A computer forensics "how-to" for fighting malicious code and analyzing incidents With our ever-increasing reliance on computers comes an ever-growing risk of malware. ... 
            """
            )
        button = st.button('*Generate link*', key = "5")
        if button:
            link = 'https://drive.google.com/file/d/17OlxUApWDR06hfuYRQP1fLzkcLuWBXl9/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/icw.jpg")
    with text_column:
        st.subheader("Inside cyber warfare: mapping the cyber underworld")
        st.text("Author: Jeffrey Carr")
        st.write(
            """
            Inside Cyber Warfare provides fascinating and disturbing details on how nations, groups, and individuals throughout the world use the Internet as an attack platform to gain military, political, and economic advantages over their adversaries. ... 
            """
            )
        button = st.button('*Generate link*', key = "6")
        if button:
            link = 'https://drive.google.com/file/d/195U-n0DJ_5FTUf8PhC2CDLoMWO-5kmXW/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/bth.jpg")
    with text_column:
        st.subheader("Blue Team Handbook: SOC, SIEM, and Threat Hunting")
        st.text("Author: Don Murdoch")
        st.write(
            """
            Blue Team Handbook: SOC, SIEM, and Threat Hunting Use Cases is having an amazing impact on Security Operations worldwide. BTHb:SOCTH is the go to guiding book for new staff at a top 10 MSSP, integrated into University curriculum, and cited in top ten courses from a major information security training company. ... 
            """
            )
        button = st.button('*Generate link*', key = "7")
        if button:
            link = 'https://drive.google.com/file/d/1J9xA_wSrlUKqpT-yrKSrL15TBodLxEGz/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)

with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/btfm.jpg")
    with text_column:
        st.subheader("Blue Team Field Manual (BTFM)")
        st.text("Author: Alan White, Ben Clark")
        st.write(
            """
            Blue Team Field Manual (BTFM) is a Cyber Security Incident Response Guide that aligns with the NIST Cybersecurity Framework consisting of the five core functions of Identify, Protect, Detect, Respond, ...
            """
            )
        button = st.button('*Generate link*', key = "8")
        if button:
            link = 'https://drive.google.com/file/d/1c3prEsOhwhT7N88Oz902-PvJbiqA0wpt/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)


st.write("---")
st.write("###")
st.subheader("Importance of DSA in Cyber Security")
st.write(
    """
    Data structures are important in cyber security for storing and organizing data. They provide a way to organize and store data so that it can be accessed efficiently. Data structures can also be used to protect data from unauthorized access.
    """)
st.write("###")
with st.container():
    st.write("###")
    image_column, text_column = st.columns((1, 4))
    with image_column:
        st.image("images/dsa.jpg")
    with text_column:
        st.subheader("Data Structures Using C")
        st.text("Author: Reema Thareja")
        st.write(
            """
            This second edition of Data Structures Using C has been developed to provide a comprehensive and consistent coverage of both the abstract concepts of data structures as well as the implementation of these concepts using C language. ...
            """
            )
        button = st.button('*Generate link*', key = "9")
        if button:
            link = 'https://drive.google.com/file/d/1l-UWJgo8T11xU-Nl_EAOpRvIx3v-SBoT/view?usp=share_link'
            st.write('*Generating link...*')
            time.sleep(1)  # Simulate some processing time
            hyperlink = f'<a href="{link}" target="_blank">Click here to read eBook...</a>'
            html(hyperlink, height=30)
