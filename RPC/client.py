import time
from rpc import Client

START = 100
END = 1100

client = Client('127.0.0.1',14001)


print('Soma: ' + str(client.sumC(10,20)) + '\n')
print('Subtração: ' + str(client.sub(10,15)) + '\n')
print('Multiplicação: ' + str(client.mul(5,5)) + '\n')
print('Divisão: ' + str(client.div(10,2)) + '\n')
print('O número 21 é primo: ' + str(client.is_prime(21)) + '\n')


time_SI = time.time()
primes_10_10000 = client.find_primes(START,END)
time_SF = time.time()
print('Tempo sem cache\n' + str(time_SF - time_SI) + '\n')
#Exibindo todos os números primos encontrados entre o intervalo de 10 a 10000
print('Todos os Números primos de 10 a 1100:\n'+ str(primes_10_10000))

numbers = list(range(START, END + 1))

x = [1,2,3,4,5,6,7,8,9]
val = client.is_primes(x)
print(val)

vetor = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 
691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 
1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097]

# Medição de tempo sem multiprocessamento
start_time = time.time()
results = client.is_prime(vetor)
end_time = time.time()
print('\nTempo sem multiprocessamento:' +  str(end_time - start_time) + '\n')

# Medição de tempo com multiprocessamento
start_time = time.time()
results_parallel = client.multiprocessamento(vetor)
end_time = time.time()
print('Tempo com multiprocessamento:'+ str(end_time - start_time) + '\n')
#print('Resultado do multiprocessamento' + str(results_parallel) + '\n')  

time_SI = time.time()
primes_10_10000 = client.find_primes(START,END)
time_SF = time.time()
print('Tempo com cache\n' + str(time_SF - time_SI) + '\n')
#Exibindo todos os números primos encontrados entre o intervalo de 10 a 10000
print('Todos os Números primos de 10 a 1100:\n'+ str(primes_10_10000))

