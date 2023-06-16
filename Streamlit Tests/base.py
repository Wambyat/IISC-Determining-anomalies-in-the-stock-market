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
from results import results_page
from home import home_page

# !TODO Add more states if required.
# These are the various states in the app. All initialized to here. More to be added
# @params
#  model_run: The state of the model: str
#       "No attempt": The model has not been run
#       "Done": The model ran successfully
#       "Error": The model ran into an unknown error
#       "Invalid": The model ran into an invalid input
if "model_run" not in st.session_state:
    st.session_state["model_run"] = "No attempt"

# This is the menu bar
# @params: (title, options, icons, orientation)
#   title: The title of the menu bar
#   options: The options in the menu bar
#   icons: The icons for the menu bar
#   key: The key for the menu bar
#   orientation: The orientation of the menu bar
# @returns: The selected option from the menu bar: str

menu_bar = option_menu("Stock market manipulation 101", ["Home", "Run Model", "View stocks", 'Profile'], icons=['house', 'cpu', "graph-up-arrow", 'person'], orientation="horizontal")

# !TODO: Finish pages: home,model,stocks,results
# This renders based on the selection from the menu bar. Since there is no switch case in python, we use if else statements.
if menu_bar=="Home":
    home_page()
elif menu_bar == "Run Model":
    model_page()
elif menu_bar == "View stocks":
    stocks_page()
elif menu_bar == "Results":
    results_page()