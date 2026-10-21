
# from git import fetch_repos

# repositories = fetch_repos()

# for repo in repositories:
#     print(f"\n{repo['name']} | Stars: {repo['stars']}")
#     print(f"Language: {repo['language']}")
#     print(repo["description"])
#     print(repo["url"])

# print(f"\nTotal repositories: {len(repositories)}")

# ======================================================================
# ======================================================================

# from news import fetch_news as fn

# latest_news = fn()

# for article in latest_news:
#     print(f"\n [{article["source"]}] {article["title"]}")
#     print(article["url"])

# ======================================================================
# ======================================================================

from weather import fetch_weather as fw

city= input("Enter city name:")
weather = fw(city)

print(weather)