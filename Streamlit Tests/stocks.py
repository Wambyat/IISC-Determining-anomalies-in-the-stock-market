import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import mpld3
import streamlit.components.v1 as components   
import matplotlib.pyplot as plt
import praw
import pandas as pd
import snscrape.modules.twitter as sntwitter
from streamlit_extras.mandatory_date_range import date_range_picker
import tweet_embed as te
import myStemmer as mS

# !TODO Move this to the secret vault
# This instanctiates the praw.Reddit object.
# @params (Store all these in the secret vault)
#   username: The username of the reddit account.
#   password: The password of the reddit account.
#   client_id: The client id of the reddit account. This is from the user account. Get it from somewhere I forgot.
#   client_secret: The client secret of the reddit account. This is from the user account. Get it from somewhere I forgot.
#   user_agent: The user agent of the reddit account. Esentially the name of the bot. We will use praw_scraper_1.0




def stocks_page():

    with st.sidebar:
            result = date_range_picker("Select a date range")
            startdate = result[0]
            enddate = result[1]
            com = st.text_input("Enter the ticker")
            passw = st.text_input(label= "Password",type = "password")
            a = st.button("Get details")

    if a == True:
        company = yf.Ticker(com)
        st.write(company.info['longName'])

        hist = company.history(period="1y")
    
        # hist.set_axis(["Time", "Open"], axis=1, inplace=True)
        index = hist.index
        index.name = "Time"
        hist = hist.reset_index()
        #drop all columns except time and open in hist dataframe
        hist = hist.drop(["High", "Low", "Close", "Volume", "Dividends", "Stock Splits"], axis=1)

        st.write(hist)

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

        user_agent = "praw_scraper_1.0"
        
        reddit = praw.Reddit(username="Wambyat", password=passw,client_id="vKxcl2gZOIFpwXw52cJr-A", client_secret="iOAq0BDKtBapF5Lf-S_z4_Ckj_tDvQ", user_agent=user_agent)
        subreddit_name = "all"
        subreddit = reddit.subreddit(subreddit_name)
        inp = company
        

        # company_name =  yf.Ticker(inp).info['longName']
        # inp = mS.remove_special_characters(company_name)
        # st.write(inp)
        mS.remove_special_characters("Hello i am under the water")
        # !TODO Add the filter for dates.
        results=subreddit.search(inp, limit=10)

        df = pd.DataFrame()
        titles=[]
        scores=[]
        ids=[]

        # Looping thru the result to get the title, score and id of the post
        # subreddit can have a few different params: top, new, hot etc.
        for res in results:    
            titles.append(res.title)
            scores.append(res.score) #upvotes
            ids.append(res.id)
            
        df['Title'] = titles
        df['Id'] = ids
        df['Upvotes'] = scores #upvotes

        #title
        st.title("Reddit Scraper")

        st.table(df)
        df.head(10)

        st.write("Hello world")

        df1 = pd.DataFrame()
        df1['Tweet'] = []
        df1['Date'] = []
        df1['URL'] = []

        st.title("Twitter Scraper")

        

        twitter_input = inp+" since:"+startdate.strftime("%Y-%m-%d")+" until:"+enddate.strftime("%Y-%m-%d")
        st.write(twitter_input)
        extra = 0
        #this uses snscraper to get latest tweets about apple
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(twitter_input).get_items()):
            if i>20:
                break
            if i>10+extra:
                break
            #append to df1
            if tweet.lang != 'en':
                extra += 1
                continue
            df2 = pd.DataFrame({'Tweet': [tweet.content], 'Date': [tweet.date], 'URL': [tweet.url]})
            df1 = pd.concat([df1, df2], ignore_index=True)

            #append to container
            tweet_url = te.embed_tweet(tweet.url)

            components.html(tweet_url, height=400, scrolling=True)

            # print(tweet.content)
            # print(tweet.date)
            print(tweet.url)
            # print(tweet.id)
            # print(tweet.user.username)
            # print(tweet.user.id)
            # print(tweet.user.followersCount)
            # print(tweet.user.friendsCount)
            # print(tweet.user.location)
            # print(tweet.user.verified)
            # print(tweet.user.description)
            # print(tweet.user.created)
            # print(tweet.user.url)
            # print(tweet.user.profileImageUrl)
            # print(tweet.likeCount)
            # print(tweet.retweetCount)
            # print(tweet.replyCount)
            # print(tweet.quoteCount)
            # print(tweet.lang)
            