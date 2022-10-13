from helpers.get_bs4 import get_bs4


def lime(query: str):
    base_url = 'https://www.limetorrents.lol'
    url = f'{base_url}/search/all/{query}/seeds/1/'
    site = get_bs4(url)
    not_null = site.select('table.table2 tr td')
    if len(not_null) == 0:
        return []
    torrents = []
    table_columns = site.select('table.table2 tr')[1:11]
    for item in table_columns:
        torrents.append({
            'name': item.select('td.tdleft .tt-name a:last-child')[0].text,
            'link': f"{base_url}{item.select('td.tdleft .tt-name a:last-child')[0].get('href')}",
            'seed': int(item.select('td.tdseed')[0].text.replace(',', '')),
            'size': item.select('td.tdnormal:nth-child(3)')[0].text,
        })
    return torrents