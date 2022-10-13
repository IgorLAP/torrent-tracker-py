import requests


def format_bytes(size):
    power = 2**10
    n = 0
    power_labels = {0 : '', 1: 'KB', 2: 'MB', 3: 'GB', 4: 'TB'}
    while size > power:
        size /= power
        n += 1
    full, rest = str(size).split('.')
    return f"{full}.{rest[:1]} {power_labels[n]}"


def torrentcsv(query: str):
    magnet_base = 'magnet:?xt=urn:btih:'
    url = f'https://torrents-csv.ml/service/search?q={query}&page=1&size=10&type_=torrent'
    torrents = []
    for item in requests.get(url).json():
        torrents.append({
            'link': f'{magnet_base}{item["infohash"]}&dn={item["name"]}',
            'name': item['name'],
            'seed': item['seeders'],
            'size': format_bytes(item['size_bytes'])
        })
    return torrents
