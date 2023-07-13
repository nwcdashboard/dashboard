import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from Main import excel, read_style, read_style2

def read(file):
    x = pd.ExcelFile(file)
    sheetnames = x.sheet_names
    selected = st.selectbox(
        "Select a sheet",
        sheetnames
    )
    df = x.parse(selected)
    return df,selected


def read(file):
    x = pd.ExcelFile(file)
    sheetnames = x.sheet_names
    selected = st.selectbox(
        "Select a sheet",
        sheetnames
    )
    df = x.parse(selected)
    return df,selected


if excel:
    df,sheet = read(excel)
    st.dataframe(df)


# overall=st.sidebar.button("Overall")
#
# if overall:
#     del excel

read_style2()
