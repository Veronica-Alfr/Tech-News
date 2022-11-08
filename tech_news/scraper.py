import requests
import time


# Requisito 1
def fetch(url, wait: int = 3):
    # "https://blog.betrybe.com"
    try:
        response = requests.get(url, timeout=wait)
        response.raise_for_status()
        print("RESPONSE => ", response.text)
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
