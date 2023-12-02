import socket
import threading
import json
from rpc.constantes import Constantes
import multiprocessing
import time
from validate_docbr import CPF #Biblioteca que valida CPFS desconsidernando a presença de "." e "-"
from rpc.cryptograph import CryptoHandler

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen(0)

    def createThread(self):
        while True:
            client, addr = self.socket_server.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client,))
            client_thread.start()

    def is_prime(self, number: int) -> bool:

        if number <= 1:
            return False
        elif number <= 3:
            return True
        elif number % 2 == 0 or number % 3 == 0:
            return False
        else:
            i = 5
            w = 2
            while i * i <= number:
                if number % i == 0:
                    return False
                i += w
                w = 6 - w
            return True

    def is_primes(self, numbers : list) -> str:
        vetor = []

        for number in numbers:
            if self.is_prime(int(number)):
                vetor.append("True")
            else:
                vetor.append("False")
    
        return ",".join(vetor)

    def check_primes_parallel(self, numbers: list) -> list:
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        results = pool.map(self.is_prime, numbers)
        pool.close()
        pool.join()
        result_str = ",".join([str (float(result)) for result in results])
        return result_str

    def find_primes(self, start, end):
        primes = []

        is_prime = [True] * (end + 1)
        is_prime[0] = is_prime[1] = False

        for p in range(2, int(end**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, end + 1, p):
                    is_prime[multiple] = False

        for num in range(max(2, int(start)), end + 1):
            if is_prime[num]:
                primes.append(num)

        return primes

    def valida_CPF(self,cpf:str):
        #Remove todos os caracteres não numéricos do CPF
        cpf_version_number = ''.join(filter(str.isdigit, cpf))

        #Verifica se o CPF tem 11 dígitos após a remoção dos não numéricos
        if len(cpf_version_number) == 11:
            cpf_validate = CPF()
            #Verifica se o CPF é válido
            print(cpf_version_number)
            return cpf_validate.validate(cpf_version_number)
        return False


    def handle_client(self, socket_client):
        while True:
            try:
                data = socket_client.recv(4096).decode('utf-8')
                data = CryptoHandler.decrypt_message(data,Constantes.KEY)
                
                if not data:
                    break
                print('pasou')
                time.sleep(3)
                operation, *args = data.split(",")

                result = None

                if operation == Constantes.SUM and len(args) == 2:
                    args = list(map(float, args))
                    result = sum(args)
                    print("Soma" + str(result))
                elif operation == Constantes.SUB and len(args) == 2:
                    args = list(map(float, args))
                    result = args[0] - args[1]
                    print("Subtracao" + str(result))
                elif operation == Constantes.MUL and len(args) == 2:
                    args = list(map(float, args))
                    result = args[0] * args[1]
                    print("Multiplicacao" + str(result))
                elif operation == Constantes.DIV and len(args) == 2:
                    args = list(map(float, args))
                    if args[1] != 0:
                        result = args[0] / args[1]
                        print("Divisao" + str(result))
                    else:
                        result = 0.0
                elif operation == Constantes.IS_PRIME and len(args) == 1:
                    result = self.is_prime(int(args[0]))
                elif operation == Constantes.IS_PRIMES and len(args) >= 1:
                    args = list(map(int, args))
                    result = self.is_primes(args)
                elif operation == Constantes.FIND_PRIMES and len(args) == 2:
                    start, end = args
                    result = self.find_primes(int(start), int(end))
                elif operation == Constantes.MULTI_PROCESSAMENTO_PRIMES and len(args) >= 1:
                    args = list(map(int, args))
                    result = self.check_primes_parallel(args)
                elif operation == Constantes.VALIDATE_CPF:
                    cpf = args[0]
                    print('CPF: ' + cpf)
                    result = self.valida_CPF(cpf)
                else:
                    result = 0.0
                print('chegou aqui')
                message = CryptoHandler.encrypt_message(str(result),Constantes.KEY)
                socket_client.send(message.encode('utf-8'))
            except ConnectionResetError:
                print("Conexão redefinida!")
                break
        # Remova a linha abaixo, pois o servidor não será encerrado quando a conexão com o cliente for fechada
        socket_client.close()
