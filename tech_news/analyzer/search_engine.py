from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    search_in_db = search_news({"title": {"$regex": title, "$options": "i"}})
    news_found = []
    for each in search_in_db:
        news_found.append((each["title"], each["url"]))
    return news_found


# Requisito 7
def search_by_date(date):
    try:
        search_in_db = search_news(
            {
                "timestamp": datetime.date.fromisoformat(date).strftime(
                    "%d/%m/%Y"
                )
            }
        )
        news_found = []
        for each in search_in_db:
            news_found.append((each["title"], each["url"]))
        return news_found
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    search_in_db = search_news({"tags": {"$regex": tag, "$options": "i"}})
    news_found = []
    for each in search_in_db:
        news_found.append((each["title"], each["url"]))
    return news_found


# Requisito 9
def search_by_category(category):
    search_in_db = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    news_found = []
    for each in search_in_db:
        news_found.append((each["title"], each["url"]))
    return news_found
