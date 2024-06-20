import time
import asyncio
import aiohttp
import tkinter as tk
from bs4 import BeautifulSoup  # Adicionando a importação do BeautifulSoup
from interface import Interface_RPC
from rpc.constantes import Constantes
from rpc.client import Client

START = 100
END = 1100

client = Client('127.0.0.1', 5000)

root = tk.Tk()
interface_RPC = Interface_RPC(root)
root.resizable(False, False)


#Verifica a operação escolhida e exibe seu resultado final
def perform_operation(operation, values):
    if operation == Constantes.IS_PRIME:
        result = client.is_prime(values[0])
        interface_RPC.print_prime(result)
    elif operation == Constantes.VALIDATE_CPF:
        result = client.valida_CPF(values[0])
        interface_RPC.print_validate_CPF(result)
    elif operation == Constantes.LAST_NEWS_IF_BARBACENA:
        news_items = client.last_news_if_barbacena(values[0])
        interface_RPC.print_noticias(news_items)
    else:
        if len(values) >= 2:
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

def on_operation_selected(operation, values):
    perform_operation(operation, values)

interface_RPC.set_operation_callback(on_operation_selected)

root.mainloop()
