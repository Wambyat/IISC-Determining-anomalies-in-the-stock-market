import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import mpld3
import streamlit.components.v1 as components    
def stocks_page():
    st.write("This is stocks page")
    com = st.text_input("Enter the ticker")
    st.button("Get graph")
    company = yf.Ticker(com)

    hist = company.history(period="1y")
    
    # hist.set_axis(["Time", "Open"], axis=1, inplace=True)
    index = hist.index
    index.name = "Time"
    hist = hist.reset_index()
    #drop all columns except time and open in hist dataframe
    hist = hist.drop(["High", "Low", "Close", "Volume", "Dividends", "Stock Splits"], axis=1)

    st.write(hist)

    import matplotlib.pyplot as plt

    fig,ax = plt.subplots()

    ax.plot(hist['Time'], hist['Open'])
    ax.set_xlabel('Time')
    ax.set_ylabel('Open')
    ax.set_title('Sales Trend')
    fig_html = mpld3.fig_to_html(fig)
    components.html(fig_html, height=600)
    
    # plt.plot(hist['Time'], hist['Open'])
    # plt.xlabel('Time')
    # plt.ylabel('Open')
    # plt.title('Sales Trend')
    # plt.show()
    # plt.savefig('output.png')
    # st.pyplot(plt.show())
