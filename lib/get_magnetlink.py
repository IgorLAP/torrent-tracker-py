import requests
from bs4 import BeautifulSoup


def get_magnetlink(link: str):
    response = requests.get(link)
    site = BeautifulSoup(response.content, 'html.parser')
    if link.__contains__('torrentgalaxy.to'):
        return site.select('a.btn.btn-danger')[0].get('href')

    if link.__contains__('limetorrents'):
        torrent_title = site.select('#content h1')[0].text
        return site.find('a', text='Magnet Download').get('href')

    if link.__contains__('1337xx.to'):
        return site.select('a[href^="magnet"]')[0].get('href')
