import socket
import os
import time
import json
import threading
from rpc.constantes import Constantes
from rpc.cryptograph import CryptoHandler

class server_name:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server_names_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_names_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.BUFFER = 1024
        self.data = ""
        self.ip_address = ""
        self.timestampI = ""
        self.server_port = ""
        self.server_host = ""
        self.sockets = self.server_sockets()
        self.log_files = {}

    #Dicionário de operações dos servidores
    def server_sockets(self):
        sockets = {
            'soma': [('127.0.0.1', 6002)],
            'subtracao': [('127.0.0.1', 6001)],
            'multiplicacao': [('127.0.0.1', 6001)],
            'divisao': [('127.0.0.1', 6001)],
            'last_news_if_barbacena': [('127.0.0.1', 6002)],
            'is_prime': [('127.0.0.1', 6001)],
            'valida_CPF': [('127.0.0.1', 6002)],
        }
        return sockets

    # Abre um arquivo para a escrita se ele existir e caso não exista cria um com o cabeçalho padrão
    def init_log_file(self, server_host, server_port):
        log_file_name = f"logServer_{server_host}_{server_port}.txt"
        if not os.path.exists(log_file_name):
            with open(log_file_name, "w") as log_file:
                log_file.write("Timestamp - IP do Cliente - Nome da Operacao - Tempo de Resposta\n")
        self.log_files[(server_host, server_port)] = log_file_name
        return log_file_name

    def log_operation(self, log_file, log_information):
        with open(log_file, "a") as log_file:
            log_file.write(log_information + "\n")
            log_file.flush()

    #Cria a thread responsável por passar as esolhas para o servidor
    def createThread(self):
        self.server_names_socket.bind((self.host, self.port))
        while True:
            operation, client_address = self.server_names_socket.recvfrom(self.BUFFER)
            operation = CryptoHandler.decrypt_message(operation.decode('utf-8'), Constantes.KEY)
            print('Conexão de:', client_address, operation)

            if operation == "FINALIZE_PROCESSING":
                self.finalize_processing()
            else:
                datas = operation
                thread = threading.Thread(target=self.handle_client, args=(datas, client_address))
                thread.start()

    def verificad_operation(self, operation: str):
        if operation in self.sockets:
            return self.sockets[operation]
        return None

    # Gerencia a comunicação com a parte do cliente
    def handle_client(self, data, client_address):
        # Grave a data/hora inicial
        self.timestampI = time.strftime("%Y-%m-%d %H:%M:%S")
        self.data = data
        self.ip_address = client_address
        response = self.verificad_operation(data)
        if response:
            server_host, server_port = response[0]
        else:
            server_host, server_port = ("unknown", "unknown")
        
        self.server_port = server_port
        self.server_host = server_host

        # Inicializa o arquivo de log correspondente
        if (server_host, server_port) not in self.log_files:
            self.init_log_file(server_host, server_port)

        # Criptografa a mensagem
        message = CryptoHandler.encrypt_message(json.dumps({'resp': response}), Constantes.KEY)
        self.server_names_socket.sendto(message.encode('utf-8'), client_address)

    def finalize_processing(self):
        # Grava o tempo final da operação
        timestampF = time.strftime("%Y-%m-%d %H:%M:%S")

        # Coloca os dados necessários de cada operação no arquivo de log
        log_information = f"{self.timestampI} - {self.ip_address} - {self.data} - {timestampF}"

        if (self.server_host, self.server_port) in self.log_files:
            log_file = self.log_files[(self.server_host, self.server_port)]
            self.log_operation(log_file, log_information)

# Exemplo de uso:
# server = server_name('127.0.0.1', 6000)
# server.createThread()
