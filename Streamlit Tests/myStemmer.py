import re
import requests
import yfinance as yf
import streamlit as st

def remove_special_characters(string):
    special_characters = ['.com','.org','.net','.edu','.gov','Inc','Corp',',','.','!']
    df_yahoo = yf.download('FB', start='2020-09-15',end='2020-11-15',progress=False)
    st.write(df_yahoo)
    st.write("SAD???")
    for i in special_characters:
        string = string.replace(i,'')
    return string
