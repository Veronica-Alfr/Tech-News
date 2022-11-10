from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    title_and_url = [(news["title"], news["url"]) for news in news_list]
    return title_and_url


# Requisito 7
def search_by_date(date):
    try:
        # formatted_date = datetime(date).strftime("%m/%d/%Y")
        formatted_date = datetime.strptime(date, "%Y-%m-%d").strftime(
            "%d/%m/%Y"
        )
        news_list = search_news({"timestamp": formatted_date})
        title_and_url = [(news["title"], news["url"]) for news in news_list]
        return title_and_url
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    news_list = search_news(
        {"tags": {"$elemMatch": {"$regex": tag, "$options": "i"}}}
        )
    title_and_url = [(news["title"], news["url"]) for news in news_list]
    return title_and_url


# Requisito 9
def search_by_category(category):
    news_list = search_news(
        {"category": {"$regex": category, "$options": "i"}}
        )
    title_and_url = [(news["title"], news["url"]) for news in news_list]
    return title_and_url
