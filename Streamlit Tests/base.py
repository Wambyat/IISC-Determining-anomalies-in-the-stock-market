import praw
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import snscrape.modules.twitter as sntwitter
from streamlit_extras.mandatory_date_range import date_range_picker
import tweet_embed as te
from streamlit_option_menu import option_menu
from model import model_page
from stocks import stocks_page
from profile import profile_page
from home import home_page

# Set streamlit to wide mode

def on_change(a):
    b = 1

menu_bar = option_menu("Stock market manipulation 101", ["Home", "Run Model", "View stocks", 'Profile'], icons=['house', 'cpu', "graph-up-arrow", 'person'], on_change=on_change,key='aa', orientation="horizontal")

#switch case in python
if menu_bar=="Home":
    home_page()
elif menu_bar == "Run Model":
    model_page()
elif menu_bar == "View stocks":
    stocks_page()
elif menu_bar == "Profile":
    profile_page()
