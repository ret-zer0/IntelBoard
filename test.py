from news import fetch_news

articles = fetch_news()

for article in articles:
    print(f"{article["source"]}")
    print(f"{article["title"]}")
    print(f"{article["url"]}")