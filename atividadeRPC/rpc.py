import socket
import threading
import math
import multiprocessing
import time
from utils import check_prime  # Importe a função check_prime

# Define operation constants
SUM = "soma"
SUB = "subtracao"
MUL = "multiplicacao"
DIV = "divisao"
IS_PRIME = "is_prime"
IS_PRIMES = "is_primes"
FIND_PRIMES = "find_primes"

class Client:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client.connect((self.host, self.port))

    def send_request(self, operation, *args):
        data = [operation, *args]
        data_str = ",".join(map(str, data))
        self.socket_client.send(data_str.encode())
        result = self.socket_client.recv(1024).decode()
        return result

    def sumC(self, number1: float, number2: float) -> float:
        return float(self.send_request(SUM, number1, number2))

    def sub(self, number1: float, number2: float) -> float:
        return float(self.send_request(SUB, number1, number2))

    def mul(self, number1: float, number2: float) -> float:
        return float(self.send_request(MUL, number1, number2))

    def div(self, number1: float, number2: float) -> float:
        return float(self.send_request(DIV, number1, number2))

    def is_prime(self, number: int) -> bool:
        result = self.send_request(IS_PRIME, number)
        return result == "True"  # Converte a string para um valor booleano
    
    def is_primes(self, numbers:list)-> list: 
        result = self.send_request(IS_PRIMES,*numbers)
        return result.split(",")
    
    def find_primes(self, start: int, end : int):
        result = self.send_request(FIND_PRIMES, start, end)
        return result

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()

    def createThread(self):
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
                w = 6 - w  # Alternar entre 2 e 4
            return True

    def is_primes(self, numbers):
        results = []

        # Filtrar strings vazias da lista
        numbers = [num for num in numbers if num.strip() != '']

        # Converter os números para inteiros antes de chamar a função check_prime
        numbers = [int(num) for num in numbers]

        start_time = time.time()  # Registra o tempo de início

        # Use multiprocessing para verificar os números em paralelo
        with multiprocessing.Pool() as pool:
            results = pool.map(check_prime, numbers)  # Use a função check_prime importada

        end_time = time.time()  # Registra o tempo de término

        execution_time = end_time - start_time  # Calcula o tempo de execução

        return results, execution_time  # Retorna os resultados e o tempo de execução




    def find_primes(self, start, end):
        primes = []

        for num in range(int(start), int(end) + 1):
            if num > 1:
                is_prime = True
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    primes.append(num)

        return primes

    def handle_client(self, socket_client):
        while True:
            data = socket_client.recv(1024).decode()
            if not data:
                break

            operation, *args = data.split(",")

            result = None

            if operation == SUM and len(args) == 2:
                args = list(map(float, args))
                result = sum(args)
            elif operation == SUB and len(args) == 2:
                args = list(map(float, args))
                result = args[0] - args[1]
            elif operation == MUL and len(args) == 2:
                args = list(map(float, args))
                result = args[0] * args[1]
            elif operation == DIV and len(args) == 2:
                args = list(map(float, args))
                if args[1] != 0:
                    result = args[0] / args[1]
                else:
                    result = 0.0
            elif operation == IS_PRIME and len(args) == 1:
                result = self.is_prime(int(args[0]))
            elif operation == IS_PRIMES and len(args) >= 1:
                numbers = args
                results, execution_time = self.is_primes(numbers)
                result = results, execution_time
            elif operation == FIND_PRIMES and len(args) == 2:
                start, end = args
                result = self.find_primes(start, end)
            else:
                result = 0.0

            # Envie o resultado diretamente como um valor booleano
            socket_client.send(str(result).encode())

        # Mova esta linha para dentro do loop while
        socket_client.close()

