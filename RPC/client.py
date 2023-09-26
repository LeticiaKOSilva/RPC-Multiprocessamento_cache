import time
from rpc import Client
import asyncio
import aiohttp
from bs4 import BeautifulSoup  # Adicionando a importação do BeautifulSoup

START = 100
END = 1100

client = Client('127.0.0.1',14001)

news_items = client.last_news_if_barbacena(100)
news_items = client.last_news_if_barbacena(1)
news_items = client.last_news_if_barbacena(3)
news_items = client.last_news_if_barbacena(20)
news_items = client.last_news_if_barbacena(10)
news_items = client.last_news_if_barbacena(5)
print(news_items)
#for valor in news_items:
#    value = valor.split(',')
#    if int(value[1]) == 5:
#        print(valor)


