import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    return soup.get_text(
        separator=" ",
        strip=True
    )