from helpers.get_bs4 import get_bs4


def seven(query: str):
    base_url = 'https://www.1337xx.to'
    url = f'{base_url}/search/${query}/1/'
    site = get_bs4(url)
    table_columns = site.select('tbody tr')
    if len(table_columns) == 0:
        return []
    torrents = []
    for item in table_columns:
        torrents.append({
            'name': item.select('td:nth-child(1) a:last-child')[0].text,
            'link': f"{base_url}{item.select('td:nth-child(1) a:last-child')[0].get('href')}",
            'seed': int(item.select('td:nth-child(2)')[0].text),
            'size': item.select('td:nth-child(5)')[0].text,
        })
    return torrents[0:10]