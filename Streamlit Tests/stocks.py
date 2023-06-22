import streamlit as st
import yfinance as yf
import plotly.express as px
import streamlit_plotly_events as plty_events
def stocks_page():
    st.write("This is stocks page")
    com = st.text_input("Enter the ticker")
    st.button("Get graph")
    company = yf.Ticker(com)
    hist = company.history(period="1y")
    st.write(hist['Open'])
    # st.line_chart(hist['Open'])
    fig = px.line(hist['Open'])
    selected_points = plty_events(fig, click_event=False, hover_event=True)
    #GOnna put the graphs n shit here.