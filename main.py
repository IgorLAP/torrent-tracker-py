from fastapi import FastAPI

import models
from lib.exporters.lime import lime
from lib.exporters.seven import seven
from lib.exporters.solidtorrents import solidtorrents
from lib.exporters.torrentcsv import torrentcsv
from lib.exporters.torrentgalaxy import torrentgalaxy
from lib.get_hotpicks import get_hotpicks
from lib.get_magnetlink import get_magnetlink
from helpers.query_formatter import query_formatter

app = FastAPI()


@app.get("/new-movies")
def new_movies(cat: int = None):
    if cat:
        movies = get_hotpicks(f'https://torrentgalaxy.to/torrents-hotpicks.php?cat={cat}')
        key = "movies" if cat == 1 else "fourKMovies"
        return {"refresh": True, key: movies}
    else:
        movies = get_hotpicks('https://torrentgalaxy.to/torrents-hotpicks.php?cat=1')
        four_k_movies = get_hotpicks('https://torrentgalaxy.to/torrents-hotpicks.php?cat=2')
        return {"movies": movies, "fourKMovies": four_k_movies}


@app.post('/get-link')
def get_link(request: models.GetLinkBody):
    link = request.link
    magnet_link = get_magnetlink(link)
    return {"magnetLink": magnet_link}


@app.post("/search-torrents")
async def search_torrents(request: models.SearchTorrentsBody):
    query = request.query
    providers = [
        {'pattern': 'seven', 'exporter': seven},
        {'pattern': 'limeTorrents', 'exporter': lime},
        {'pattern': 'torrentCsv', 'exporter': torrentcsv},
        {'pattern': 'torrentGalaxy', 'exporter': torrentgalaxy},
        {'pattern': 'solidTorrents', 'exporter': solidtorrents}
    ]
    torrents = []
    for item in range(len(providers)):
        exporter = providers[item]['exporter']
        pattern = providers[item]['pattern']
        formatted_query = query_formatter(query, pattern)
        torrents.extend(exporter(formatted_query))

    return {"torrents": torrents}
