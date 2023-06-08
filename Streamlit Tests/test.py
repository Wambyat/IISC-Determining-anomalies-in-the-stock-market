import praw
import pandas as pd
import streamlit as st
import snscrape.modules.twitter as sntwitter

# Define user agent
user_agent = "praw_scraper_1.0"

# Create an instance of reddit class
reddit = praw.Reddit(
                     username="Wambyat",
                     password="47acadaniaaa",
                     client_id="vKxcl2gZOIFpwXw52cJr-A",
                     client_secret="iOAq0BDKtBapF5Lf-S_z4_Ckj_tDvQ",
                     user_agent=user_agent
)


#Put the name of the subreddit here. Should be changed to a search instead.
subreddit_name = "all"
subreddit = reddit.subreddit(subreddit_name)

results=subreddit.search('apple', limit=10)

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

#this uses snscraper to get latest tweets about apple
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('apple since:2023-06-01 until:2023-06-07').get_items()):
    if i>10:
        break
    #append to df1
    df1 = df1.append({'Tweet':tweet.content, 'Date':tweet.date}, ignore_index=True)
    print(tweet.content)
    print(tweet.date)
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

st.title("Twitter Scraper")
st.table(df1)