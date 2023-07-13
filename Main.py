import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from PIL import Image


img=Image.open('images/NWC.png')
st.set_page_config(page_title='NWC',page_icon=img)
st.title('Welcome to Dashboard')
st.subheader('import excel file: ')
excel = st.file_uploader('Chose your file:', type='xlsx')

def read_style():
    with open("design.html") as f:
        return f.read()
def read_style2():
    with open("style.css") as f:
        return st.markdown(f'<style> {f.read()} </style>',unsafe_allow_html=True)



read_style2()
