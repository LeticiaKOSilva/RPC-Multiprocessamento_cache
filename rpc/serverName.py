import socket
import os
import time
import json
import threading  # Correção: importando a biblioteca correta
from rpc.constantes import Constantes

class server_name:

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server_names_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_names_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.BUFFER = 1024
        self.sockets = self.server_sockets()

        #Cria um arquivo de log
        self.arq_log_fileName = f"logServer_{host}_{port}.txt"

        # Cria ou resgata o arquivo log do servidor de operações.
        self.log_file = ""

    def server_sockets(self):
        sockets = {
            'soma': [('127.0.0.1', 6001)],
            'subtracao': [('127.0.0.1', 6001)],
            'multiplicacao': [('127.0.0.1', 6001)],
            'divisao': [('127.0.0.1', 6001)],
            'last_news_if_barbacena': [('127.0.0.1', 6001)],
            'is_prime': [('127.0.0.1', 6001)],
            'valida_CPF': [('127.0.0.1', 6001)],
        }

        return sockets
    
    def arq_log(self, nameArq):
        #Cria um nome para o arquivo log
        log = f"logServer_{nameArq}.txt"
        log_fileName = ""

        '''
            Verifica se o arquivo de log já existe.
            Se não existir ele cria um novo arquivo e adiciona nele o cabeçalho do arquivo
            Se existir abra ele em formato de anexação 
        '''
        if not os.path.exists(log):
            with open(log, "w") as log_fileName:
                log_fileName.write(" Timestamp - IP do Cliente - Nome da Operacao - Tempo de Resposta \n")
            
            #Abre o arquivo para anexação
        log_fileName = open(log, "a")

        return log_fileName

    #Fecha o arquivo passado por parâmetro
    def to_close_log(self, arq):
        self.log_file.close()

    def createThread(self):
        self.server_names_socket.bind((self.host, self.port))
        while True:
            operation, client_address = self.server_names_socket.recvfrom(self.BUFFER)
            print('Conexão de:', client_address, operation)

            datas = operation.decode()
            thread = threading.Thread(target=self.handle_client, args=(datas, client_address))
            thread.start()

    def verificad_operation(self, operation: str):
        if operation in self.sockets:
            return self.sockets[operation]

    def handle_client(self, data, client_address):

        #Adiciona a contagem de timestamp
        timestampI = time.strftime("%Y-%m-%d %H:%M:%S")

        response = self.verificad_operation(data)

        if data == Constantes.VALIDATE_CPF:
            time.sleep(4)
        elif data == Constantes.IS_PRIME:
            time.sleep(5)
        else:
            time.sleep(6)

        #Adiciona a contagem de timestamp
        timestampF = time.strftime("%Y-%m-%d %H:%M:%S")

         #Informação de log
        log_information = f"{timestampI} - {client_address} - {data} - {timestampF}"

        '''
            Escreve os dados no arquivo correspondente
            Com o método flush certifica se as informações realmente chegaram
            Depois fecha o arquivo.
        '''
        self.log_file = self.arq_log(response)
        self.log_file.write(log_information + "\n")
        self.log_file.flush()
        self.to_close_log(self.log_file)

        self.server_names_socket.sendto(json.dumps({'resp': response}).encode(), client_address)

# Exemplo de uso:
# server = server_name('127.0.0.1', 6000)
# server.createThread()