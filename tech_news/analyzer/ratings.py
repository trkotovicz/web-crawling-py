from tech_news.database import find_news


# Requisito 10
def top_5_news():
    news_from_db = find_news()
    sort_news = sorted(
        news_from_db, key=lambda row: row["comments_count"], reverse=True
    )

    sorted_news = [
        (each_new["title"], each_new["url"]) for each_new in sort_news
    ]
    print(sorted_news)
    return sorted_news[:5]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
