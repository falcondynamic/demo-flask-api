import streamlit as st

from helpers import load_lottieurl, local_css

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
local_css(st, "style/styles.css")

with st.container():
    st.header("My Resume")
    st.subheader("Hi I am a Data Scientist :wave:")
    st.write("I am a Data Scientist with 2 years of experience in the field. I have worked on several projects and have experience in Python, SQL, and Machine Learning.")  
    st.write("[Learn more >](https://www.linkedin.com/in/your-linkedin-profile/)")
