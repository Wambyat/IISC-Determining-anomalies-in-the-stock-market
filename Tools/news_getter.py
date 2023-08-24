from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key="d76c6f83b5e04d968b1a7c0ec785623e")

# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(
#     q="bitcoin",
#     sources="bbc-news,the-verge",
#     category="business",
#     language="en",
#     country="us",
# )

# /v2/everything
all_articles = newsapi.get_everything(
    q="bitcoin",
    from_param="2017-12-01",
    to="2017-12-12",
    language="en",
)

print(all_articles)

# /v2/top-headlines/sources
# sources = newsapi.get_sources()
