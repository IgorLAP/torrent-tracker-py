import requests
from bs4 import BeautifulSoup


def get_bs4(url: str):
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')