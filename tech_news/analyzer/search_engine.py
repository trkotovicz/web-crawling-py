from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """for book in db.books.find({"title": {"$regex": "t"}}):
        print(book["title"])"""
    search_in_db = search_news({"title": {"$regex": title, "$options": "i"}})
    news_found = []
    for each in search_in_db:
        news_found.append((each["title"], each["url"]))
    # print((search_in_db[0]["title"], search_in_db[0]["url"]))
    print(news_found)
    return news_found


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
