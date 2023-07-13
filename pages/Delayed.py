import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from Main import excel, read_style, read_style2


if excel:
    x = pd.ExcelFile(excel)
    delayed_sheet = x.parse('المتأخر')
    st.dataframe(delayed_sheet)


read_style2()