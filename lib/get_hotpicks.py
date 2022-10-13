import requests
from bs4 import BeautifulSoup


def get_hotpicks(url: str):
    response = requests.get(url)
    site = BeautifulSoup(response.content, 'html.parser')
    hot_picks = site.findAll('div', attrs={'class': 'hotpicks'})
    movies = []
    for item in hot_picks:
        link = f"https://torrentgalaxy.to/{item.find('a').get('href')}"
        poster = item.find('img').get('data-src')
        name = item.find('img').get('alt')
        movies.append({"link": link, "poster": poster, "name": name})
    return movies
