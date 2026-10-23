import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from html import unescape

import feedparser

FEEDS = {
    "Al Jazeera": "https://www.aljazeera.com/xml/rss/all.xml",
    "The Guardian": "https://www.theguardian.com/world/rss",
    "BBC": "https://feeds.bbci.co.uk/news/rss.xml",
    "Dawn": "https://www.dawn.com/feeds/pakistan/"
}

def get_date(date):

    if not date:
        return datetime.min.replace(tzinfo=timezone.utc)  # noqa: UP017

    try:
        converted_date = parsedate_to_datetime(date)

        if converted_date.tzinfo is None:
            converted_date = converted_date.replace(tzinfo=timezone.utc)  # noqa: UP017

        return converted_date

    except (ValueError, TypeError, OverflowError):
        return datetime.min.replace(tzinfo=timezone.utc)  # noqa: UP017

def fetch_news(limit=15):
    articles = []

    for source, url in FEEDS.items():
        try:
            feed = feedparser.parse(url)

            if feed.bozo and not feed.entries:
                print(f"Could not read {source} feed.")
                continue

            for entry in feed.entries:
                summary = entry.get("summary", "")
                summary = re.sub(r"<[^>]+>", "",summary)
                summary = unescape(summary).strip()

                articles.append({
                    "source"   : source,
                    "title"    : entry.get("title", "No title"),
                    "summary"  : summary,
                    "url"      : entry.get("link", ""),
                    "published": entry.get("published", "")
                })


        except Exception as error:  # noqa: BLE001
            print(f"Error fetching {source}, {error}")

    articles.sort(
        key=lambda article: get_date(article["published"]),
        reverse=True
    )
    return articles[:limit]