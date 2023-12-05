import socket
import json
import inspect
import random
import time
import multiprocessing
from rpc.cache import Cache
from rpc.constantes import Constantes
from rpc.request import Request
from rpc.cryptograph import CryptoHandler

class Client:

    def __init__(self, host,port):
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.cache = Cache()
        self.tempo = 0
        self.BUFFER = 8192

    def send_request(self, operation, *args):
        data = [operation, *args]
        data_str = ",".join(map(str, data))
            
        start_time = time.time()

        result = self.cache.get(data_str)
        if result is not None:
            return result
        else:
            print('entrou aqui nesse trem muito doido')
            ips = self.resolve_operation_server_ips(operation)
            if ips:
                print('entrou no if ips')
                serverH, serverP = random.choice(ips)
                socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                try:
                    socket_server.connect((serverH, serverP))
                    print('conectou nesse trem')
                    print(data_str)
                    message = CryptoHandler.encrypt_message(data_str,Constantes.KEY)
                    socket_server.send(message.encode('utf-8'))
                    print('enviou')
                    result = socket_server.recv(4096).decode('utf-8')
                    print('recebeu o resultado')
                    result = CryptoHandler.decrypt_message(result,Constantes.KEY)
                    if result == 'Operação inexistente!':
                        print("Inexistente" + str(result))
                        return 0.0
                except ConnectionResetError:
                    print("A conexão foi interrompida!")
                    # Adicione lógica de reconexão aqui se necessário

                socket_server.close()

            else:
                return 0.0

            self.cache.set(data_str, result)
            if self.check_time(time.time() - start_time):
                print("Entrou no time")
                self.cache.export_cache()
        print("Passou do send")
        return result
    
    def check_time(self, elapsed_time):
        
        if elapsed_time >= Constantes.TIME_SINCRONIZED:
            return True
        return False 

    def resolve_operation_server_ips(self, operation):
        message = CryptoHandler.encrypt_message(operation,Constantes.KEY)
        self.socket_client.sendto(message.encode('utf-8'), (self.host, self.port))
        ips = self.socket_client.recvfrom(self.BUFFER)
        ips_data = ips[0]
        ips = CryptoHandler.decrypt_message(ips_data.decode('utf-8'), Constantes.KEY)
        ips = json.loads(ips)['resp']
        return ips

    def sumC(self, number1: float, number2: float) -> float:
        return float(self.send_request(Constantes.SUM, number1, number2))

    def sub(self, number1: float, number2: float) -> float:
        return float(self.send_request(Constantes.SUB, number1, number2))

    def mul(self, number1: float, number2: float) -> float:
        return float(self.send_request(Constantes.MUL, number1, number2))

    def div(self, number1: float, number2: float) -> float:
        return float(self.send_request(Constantes.DIV, number1, number2))

    def is_prime(self, number: int) -> bool:
        result = self.send_request(Constantes.IS_PRIME, number)
        return result == "True"  # Converte a string para um valor booleano
    
    def is_primes(self, numbers: list) -> list:
        result_str = self.send_request(Constantes.IS_PRIMES, *numbers)
        results = [val == "True" for val in result_str.split(",")]
        return results

    def multiprocessamento(self, numbers: list) -> list:
        result_str = self.send_request(Constantes.MULTI_PROCESSAMENTO_PRIMES, *numbers)
        results = [bool(float(val)) for val in result_str.split(",") if val]  # Filtra valores vazios
        return results
    
    def find_primes(self, start: int, end : int):
        result = self.send_request(Constantes.FIND_PRIMES, start, end)
        return result

    def last_news_if_barbacena(self, qtd_noticias: int):
        data_str = f"{Constantes.LAST_NEWS_IF_BARBACENA},{qtd_noticias}"
        news_items = self.send_request(Constantes.LAST_NEWS_IF_BARBACENA, qtd_noticias)

        if news_items == Constantes.NO_NOTICIAS:
            news_items = "Número inválido de notícias"
        else:
            news_items = Request.get_titles(qtd_noticias)
            self.cache.set(data_str, news_items)  # Atualiza o cache
        #news_items = self.cache.get(data_str)

        # if self.cache.is_cache_outdated(data_str):
        #     # Se a quantidade desejada é maior que a do cache, buscar no site
        #     #news_items = Request.get_titles(qtd_noticias)
        #     news_items = self.send_request(Constantes.LAST_NEWS_IF_BARBACENA, qtd_noticias)
        #     self.cache.set(data_str, news_items)  # Atualiza o cache
        # elif news_items is not None:
        #     news_items = self.cache.get_v(data_str,qtd_noticias)
        #     if len(news_items) > 0 :
        #     else:
        #         # Se a quantidade desejada é maior que a do cache, buscar no site
        #         #news_items = Request.get_titles(qtd_noticias)
        #         news_items = self.send_request(Constantes.LAST_NEWS_IF_BARBACENA, qtd_noticias)
        #         self.cache.set(data_str, news_items)  # Atualiza o cache
        # else:
        #     # Se a quantidade desejada é maior que a do cache, buscar no site
        #         #news_items = Request.get_titles(qtd_noticias)
        #         news_items = self.send_request(Constantes.LAST_NEWS_IF_BARBACENA, qtd_noticias)
        #         self.cache.set(data_str, news_items)  # Atualiza o cache
        return news_items
    
    def valida_CPF(self,cpf:str) -> bool:
        result = self.send_request(Constantes.VALIDATE_CPF, cpf)
        return result == "True" # Converte a string para um valor booleano