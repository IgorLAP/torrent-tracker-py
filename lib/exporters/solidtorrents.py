from helpers.get_bs4 import get_bs4
from helpers.seed_formatter import seed_formatter


def solidtorrents(query: str):
    base_url = 'https://solidtorrents.to'
    url = f'{base_url}/search?q={query}'
    site = get_bs4(url)
    table_columns = site.select('.card.search-result.my-2')
    if len(table_columns) == 0:
        return []
    torrents = []
    columns = table_columns[0:10] \
        if table_columns[0].select('div.links a:last-child') is None \
        else table_columns[3:13]
    for item in columns:
        torrents.append({
            'name': item.select('h5.title')[0].text,
            'link': item.select('div.links a:last-child')[0].get('href'),
            'size': item.select('div.stats div:nth-child(2)')[0].text,
            'seed': seed_formatter(item.select('div.stats div:nth-child(3)')[0].text),
        })
    return torrents
