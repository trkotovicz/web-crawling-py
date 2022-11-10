import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except (requests.ReadTimeout, requests.HTTPError):
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("li.meta-author > .author a::text").get()
    join = ""
    summary = join.join(
        selector.css(".entry-content > p:nth-of-type(1) *::text").getall()
    ).strip()
    category = selector.css(".entry-header-inner span.label::text").get()
    comments_count = len(selector.css(".comment").getall())
    tags = selector.css("a[rel=tag]::text").getall()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news_links = []
    news = []

    while len(news_links) <= amount:
        html_page = fetch(url)
        scrape_news_links = scrape_novidades(html_page)
        url = scrape_next_page_link(html_page)
        news_links.extend(scrape_news_links)

    for link in news_links[:amount]:
        fetch_new = fetch(link)
        scrape_new = scrape_noticia(fetch_new)
        news.append(scrape_new)

    create_news(news)
    return news
