import time
from rpc.client import Client
import asyncio
import aiohttp
from bs4 import BeautifulSoup  # Adicionando a importação do BeautifulSoup
import tkinter as tk
from interface import Interface_RPC

START = 100
END = 1100

#client = Client('127.0.0.1',5000)

root = tk.Tk()
app = Interface_RPC(root)
root.resizable(False, False)
root.mainloop()
# Inicie o loop de eventos do Tkinter após ter interagido com a interface
#root.mainloop()
#app.return_values()
#print(operation)
#print(values)
#print(str(client.is_prime(2)))
#print(str(client.is_prime(3)))
#print(str(client.is_prime(1)))
#subtracao = client.sub(12,3)
#print(str(client.sub(6,2)))
#print(client.valida_CPF('137.819.696-14'))
#multiplicacao = client.mul(11,4)
#divisao = client.div(3,4)
#print(str(client.mul(5,5)))
#print(multiplicacao)
#print(str(client.sumC(2,6)))
#print(str(client.div(20,5)))
#news_items = client.last_news_if_barbacena(390)
#news_items = client.last_news_if_barbacena(400)
# news_items = client.last_news_if_barbacena(3)
# news_items = client.last_news_if_barbacena(20)
# news_items = client.last_news_if_barbacena(10)
# news_items = client.last_news_if_barbacena(5)
#print(news_items)
#for valor in news_items:
#    value = valor.split(',')
#    if int(value[1]) == 5:
#        print(valor)
