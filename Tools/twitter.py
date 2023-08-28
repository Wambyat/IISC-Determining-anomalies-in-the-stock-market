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
    twitter_input = (
        inp
        + " since:"
        + startdate.strftime("%Y-%m-%d")
        + " until:"
        + enddate.strftime("%Y-%m-%d")
    )
    extra = 0
    for i, tweet in enumerate(
        sntwitter.TwitterSearchScraper(twitter_input).get_items()
    ):
        if i > 20:
            break
        if i > 10 + extra:
            break
        # append to df1
        if tweet.lang != "en":
            extra += 1
            continue
        df2 = pd.DataFrame(
            {"Tweet": [tweet.content], "Date": [tweet.date], "URL": [tweet.url]}
        )
        df1 = pd.concat([df1, df2], ignore_index=True)

        print(tweet.url)


if __name__ == "__main__":
    twitter_call("apple", datetime.datetime(2023, 8, 1), datetime.datetime(2023, 8, 2))
