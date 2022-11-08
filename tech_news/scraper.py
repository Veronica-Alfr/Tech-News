import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url, wait: int = 3):
    headers = {
            "user-agent": "Fake user-agent"
        }

    try:
        response = requests.get(url, timeout=wait, headers=headers)
        response.raise_for_status()
        print("RESPONSE => ", response.text)
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content: str) -> list:
    selector = Selector(html_content)
    return selector.css(".cs-overlay-link::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content: str) -> list:
    selector = Selector(html_content)
    return selector.css("a.next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content: str):
    selector = Selector(html_content)

    comments = selector.css("div.post-comments h5::text").get()
    if comments is not None:
        commentsReturn = int(comments.strip().split()[0])

    print(selector.css("div.entry-content > p:first-of-type *").get())

    return {
        "url": selector.css("link[rel=canonical]::attr(href)").get(),
        "title": selector.css("h1.entry-title::text").get().strip(),
        "timestamp": selector.css("li.meta-date::text").get(),
        "writer": selector.css("a.url.fn.n::text").get(),
        "comments_count": commentsReturn if comments else 0,
        "summary": "".join(selector.css(
            "div.entry-content > p:first-of-type *::text").getall()).strip(),
        "tags": selector.css("li > a[rel=tag]::text").getall(),
        "category": selector.css("div.meta-category span.label::text").get()
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
