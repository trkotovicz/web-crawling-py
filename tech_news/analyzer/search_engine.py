from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    search_in_db = search_news({"title": {"$regex": title, "$options": "i"}})
    news_found = []
    for each in search_in_db:
        news_found.append((each["title"], each["url"]))
    return news_found


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    search_in_db = search_news({"tags": {"$regex": tag, "$options": "i"}})
    news_found = []
    for each in search_in_db:
        news_found.append((each["title"], each["url"]))
    return news_found


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
