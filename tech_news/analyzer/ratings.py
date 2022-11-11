from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_news():
    news_from_db = find_news()
    sort_news = sorted(
        news_from_db, key=lambda row: row["comments_count"], reverse=True
    )

    sorted_news = [
        (each_new["title"], each_new["url"]) for each_new in sort_news
    ]
    return sorted_news[:5]


# Requisito 11
def top_5_categories():
    news_from_db = find_news()
    categories = [each_new["category"] for each_new in news_from_db]
    sorted_array = sorted(categories)
    count_categories = Counter(sorted_array).most_common(5)

    result = []
    for each in count_categories:
        category, times = each
        result.append(category)

    return result
