import streamlit as st
from util import intro_title, intro_text1



def run_intro():
    st.markdown(intro_title, unsafe_allow_html=True)
    st.markdown(intro_text1, unsafe_allow_html=True)







