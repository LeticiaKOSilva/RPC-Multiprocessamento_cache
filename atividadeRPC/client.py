import time
from rpc import Client

START = 10
END = 1000

client = Client('127.0.0.1',14000)

print(client.sumC(10,20))
print(client.sub(10,15))
print(client.mul(5,5))
print(client.div(10,2))
print(client.is_prime(21))

primes_10_10000 = client.find_primes(START,END)

#Exibindo todos os números primos encontrados entre o intervalo de 10 a 10000
print(primes_10_10000)

numbers = list(range(START, END + 1))

# Medir o tempo de execução com multiprocessamento no cliente
start_time_client = time.time()
results = client.is_primes(numbers)
end_time_client = time.time()
execution_time_with_multiprocessing = end_time_client - start_time_client

print("Resultados com multiprocessamento:")

print(f"Tempo de execução com multiprocessamento no cliente: {execution_time_with_multiprocessing:.4f} segundos")