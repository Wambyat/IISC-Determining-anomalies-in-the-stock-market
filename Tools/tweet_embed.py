import requests
import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime

def embed_tweet(tweet_url):
    api = "https://publish.twitter.com/oembed?url={}".format(tweet_url)
    response = requests.get(api)
    res = response.json()["html"]
    return res

def twitter_call(inp, startdate, enddate):
    twitter_input = inp+" since:"+startdate.strftime("%Y-%m-%d")+" until:"+enddate.strftime("%Y-%m-%d")
    # st.write(twitter_input)
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
        # tweet_url = embed_tweet(tweet.url)

        # components.html(tweet_url, height=400, scrolling=True)

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
        

if __name__ == '__main__':
    twitter_call("apple", datetime.datetime(2021, 1, 1), datetime.datetime(2021, 1, 2))