import praw, pandas as pd
user_agent = "praw_scraper_1.0"
reddit = praw.Reddit(
                     username="Wambyat",
                     password="47acadaniaaa",
                     client_id="vKxcl2gZOIFpwXw52cJr-A",
                     client_secret="iOAq0BDKtBapF5Lf-S_z4_Ckj_tDvQ",
                     user_agent=user_agent
)
subreddit_name = "all"
subreddit = reddit.subreddit(subreddit_name)
inp = 'Apple Inc.'
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
df['Upvotes'] = scores

print(df)