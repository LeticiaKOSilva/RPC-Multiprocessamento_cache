
class Constantes:
    #Nome do arquivo responsável por guardar os dados em cache
    CACHE_FILE_NAME = 'cache.txt'


    CACHE_SYNC_TIME = 3  # Tempo mínimo para sincronização em segundos
    MAX_CACHE_SIZE = 5  # Número máximo de registros no cache em disco

    #Operações
    SUM = "soma"
    SUB = "subtracao"
    MUL = "multiplicacao"
    DIV = "divisao"
    IS_PRIME = "is_prime"
    IS_PRIMES = "is_primes"
    FIND_PRIMES = "find_primes"
    MULTI_PROCESSAMENTO_PRIMES = "multi_processamento_primes"
    LAST_NEWS_IF_BARBACENA = "last_news_if_barbacena"
    VALIDATE_CPF = "valida_CPF"

    YES_NOTICIAS ="Pode procurar"
    NO_NOTICIAS = "Nao pode procurar"
    
    #Referente aos símbolos das operações matemáticas
    SIM_SUM = "+"
    SIM_SUB ="-"
    SIM_MUL = "*"
    SIM_DIV = "/"

    #Referente ao tempo de sincronização
    TIME_SINCRONIZED = 4

    #Número total de requisições aceitas no cache
    NUMBER_CACHE = 6

    KEY = b'Sixteen byte key'

    URL_SITE = "https://www.ifsudestemg.edu.br/noticias/barbacena/?b_start:int="
