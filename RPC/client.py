import time
from rpc import Client
import asyncio
import aiohttp
from bs4 import BeautifulSoup  # Adicionando a importação do BeautifulSoup

START = 100
END = 1100

client = Client('127.0.0.1',14001)

news_items = client.last_news_if_barbacena(8)

for valor in news_items:
    print(valor)


