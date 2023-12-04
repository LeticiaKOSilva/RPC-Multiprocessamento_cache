import time
from rpc.client import Client
import asyncio
import aiohttp
from bs4 import BeautifulSoup  # Adicionando a importação do BeautifulSoup
import tkinter as tk
from rpc.constantes import Constantes
from interface import Interface_RPC

START = 100
END = 1100

#Variáveis que serão utilizadas para receber os dados da interface
operation = ""
values = []

client = Client('127.0.0.1',5000)

root = tk.Tk()
interface_RPC = Interface_RPC(root)
root.resizable(False, False)
root.mainloop()
operation, values = interface_RPC.return_values()

if operation == Constantes.IS_PRIME:
    print("entrou")
    result = client.is_prime(values[0])
    interface_RPC.print_prime(result)
elif operation == Constantes.VALIDATE_CPF:
    result = client.valida_CPF(values[0])
    interface_RPC.print_validate_CPF(result)
elif operation == Constantes.LAST_NEWS_IF_BARBACENA:
    news_items = client.last_news_if_barbacena(values[0])
    for valor in news_items:
        value = valor.split(',')
        if int(value[1]) == 5:
            result += valor
else:
    if len(values) >= 2:  # Check if there are at least two values in the list
        if operation == Constantes.SIM_SUM:
            result = client.sumC(values[0], values[1])
        elif operation == Constantes.SIM_SUB:
            result = client.sub(values[0], values[1])
        elif operation == Constantes.SIM_MUL:
            result = client.mul(values[0], values[1])
        else:
            result = client.div(values[0], values[1])
        interface_RPC.print_result(result)
    else:
        print("Not enough values for the operation.")





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
