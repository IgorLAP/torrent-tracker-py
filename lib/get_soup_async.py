import aiohttp
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}


async def get_soup_async(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, verify_ssl=False) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            return soup

