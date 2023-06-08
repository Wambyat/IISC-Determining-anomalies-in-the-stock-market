import tweepy

bearer_token = ""

client = tweepy.Client(bearer_token)

response = client.search_recent_tweets("Tweepy")


client_key = 'WlVyM010YWRIM2RmeWJvUWhCSlQ6MTpjaQ'
client_secret = 'TFtSvUgIu-8qUbupwJxvy4hVrlqwhOBUm2S9lpZ54gl8O4SMHq'

API_Key         = 'FW8lqHu7HwJ7o0SOi72CGsRVW'
API_Secret      = 'b87AciaIAvq1KjONMhesTesquJVQXQ0nmTSi2uqluGufDC5N2P'
Bearer_Token    = 'AAAAAAAAAAAAAAAAAAAAAMhbngEAAAAAdD1XVsly31n7%2FhnojROtaCXaL04%3DxjVFE3ZxHwydVxld1117L6nTOy96wa7bZwjvrzqOUbI9oQYiug'
Access_Token    = '1659227903324979201-7TYcJq0XO7QPuUIwo0gc77t3FWALro'
Access_Secret   = '6RJGgnKBDp7hjJ7G1Fnj84ScCXS6PWYhLn09i3Y1DiLDG'

# Authenticate with Twitter OAuth 2.0 Bearer Token (Application-only)
client = tweepy.Client(Bearer_Token)

# Pull tweets from twitter

query = '#chatgpt -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

# Get tweets that contain the hashtag #TypeKeywordHere
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english

for tweet in tweets.data:
    print('\n**Tweet Text**\n',tweet.text)

# The method returns a Response object, a named tuple with data, includes,
# errors, and meta fields
print(response.meta)

# In this case, the data field of the Response returned is a list of Tweet
# objects
tweets = response.data

# Each Tweet object has default ID and text fields
for tweet in tweets:
    print(tweet.id)
    print(tweet.text)

# By default, this endpoint/method returns 10 results
# You can retrieve up to 100 Tweets by specifying max_results
response = client.search_recent_tweets("Tweepy", max_results=100)