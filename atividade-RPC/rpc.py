import socket
import threading
import math
import multiprocessing
import time

# Define operation constants
SUM = "soma"
SUB = "subtracao"
MUL = "multiplicacao"
DIV = "divisao"
IS_PRIME = "is_prime"
IS_PRIMES = "is_primes"
FIND_PRIMES = "find_primes"
MULTI_PROCESSAMENTO_PRIMES = "multi_processamento_primes"

class Client:
    '''Construtor da classe Client que recebe em seu parâmetro o 
       host(Ip do dispositivo)
       e a port(porta de acesso)
    '''
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client.connect((self.host, self.port))
        self.cache = {}  # Dicionário para armazenar resultados em cache

    def send_request(self, operation, *args):
        data = [operation, *args]
        data_str = ",".join(map(str, data))

        # Verifique se o resultado está em cache
        if data_str in self.cache:
            result = self.cache[data_str]
        else:
            self.socket_client.send(data_str.encode())
            result = self.socket_client.recv(4096).decode()
            self.cache[data_str] = result  # Armazene o resultado em cache

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
    
    def is_primes(self, numbers: list) -> list:
        result_str = self.send_request(IS_PRIMES, *numbers)
        results = [val == "True" for val in result_str.split(",")]
        return results

    def multiprocessamento(self, numbers: list) -> list:
        result_str = self.send_request(MULTI_PROCESSAMENTO_PRIMES, *numbers)
        results = [bool(float(val)) for val in result_str.split(",") if val]  # Filtra valores vazios
        return results
    
    def find_primes(self, start: int, end : int):
        result = self.send_request(FIND_PRIMES, start, end)
        return result

class Server:
    '''Construtor da classe Server que recebe em seu parâmetro o 
       host(Ip do dispositivo)
       e a port(porta de acesso)
    '''
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.host, self.port))
        self.socket_server.listen()

    #Cria uma thread para cada client conectado a este servidor
    def createThread(self):
        client, addr = self.socket_server.accept()
        client_thread = threading.Thread(target=self.handle_client, args=(client,))
        client_thread.start()

    #Verifica se um número é primo, se sim retorna True senão retorna False.
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

    '''Verifica se os números da lista são primos ou não, retornando uma lista de booleanos no final
       onde True-> número primo
        False -> número não primo 
    '''
    def is_primes(self, numbers : list) -> str:
        vetor = []

        for number in numbers:
            if self.is_prime(int(number)):
                vetor.append("True")
            else:
                vetor.append("False")
    
        return ",".join(vetor)  # Envia uma única string com os resultados separados por vírgula

    #Passa é divide de forma paralela o processos que verificam se os números da lista são primos ou não
    #Retornando ao fim uma lista de booleanos
    def check_primes_parallel(self, numbers: list) -> list:
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
        results = pool.map(self.is_prime, numbers)
        pool.close()
        pool.join()
        result_str = ",".join([str (float(result)) for result in results])  # Converte resultados em uma string
        return result_str

    #Verifica os números primos dentro do intervalo passado por parâmetro, retornando uma lista com esses números
    def find_primes(self, start, end):
        primes = []

        # Inicialize um array para rastrear os números primos até end
        is_prime = [True] * (end + 1)
        is_prime[0] = is_prime[1] = False  # 0 e 1 não são primos

        for p in range(2, int(end**0.5) + 1):
            if is_prime[p]:
                for multiple in range(p * p, end + 1, p):
                    is_prime[multiple] = False

        for num in range(max(2, int(start)), end + 1):
            if is_prime[num]:
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
                args = list(map(int, args))  # Convertemos todos os argumentos para inteiros
                result = self.is_primes(args)
            elif operation == FIND_PRIMES and len(args) == 2:
                start, end = args
                result = self.find_primes(int(start), int(end))
            elif operation == MULTI_PROCESSAMENTO_PRIMES and len(args) >= 1:
                args = list(map(int, args))
                result = self.check_primes_parallel(args)
            else:
                result = 0.0

            # Envia o resultado diretamente como um valor booleano
            socket_client.send(str(result).encode())

        socket_client.close()

