from helpers.get_bs4 import get_bs4
from helpers.seed_formatter import seed_formatter


def torrentgalaxy(query: str):
    base_url = 'https://torrentgalaxy.to'
    url = f'{base_url}/torrents.php?search={query}&lang=0&nox=2&sort=seeders&order=desc'
    site = get_bs4(url)
    not_null = site.select('div.tgxtable')
    if len(not_null) == 0:
        return []
    table_columns = site.select('div.tgxtable div.tgxtablerow')[0:10]
    torrents = []
    for item in table_columns:
        torrents.append({
            'name': item.select('div.tgxtablecell.clickable-row a:nth-child(1)')[0].text.replace('<b>', ''),
            'link': f"{base_url}{item.select('div.tgxtablecell.clickable-row a:nth-child(1)')[0].get('href')}",
            'size': item.select('div.tgxtablecell.collapsehide span.badge.badge-secondary')[0].text,
            'seed':
                seed_formatter(
                    item.select('div.tgxtablecell.collapsehide span[title="Seeders/Leechers"] font[color="green"]')
                    [0].text
                )
        })
    return torrents
