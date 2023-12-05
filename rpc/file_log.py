import time
class File_log:
    def __init__(self, host: str, port: int):

        #Cria um arquivo de log
        self.arq_log_fileName = f"logServer_{host}_{port}.txt"

        # Cria ou resgata o arquivo log do servidor de operações.
        self.log_file = ""

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

    @staticmethod
    def add_Text(host, port, data):
        timestampI = time.strftime("%Y-%m-%d %H:%M:%S")
        log_information = f"{timestampI} - {host} - {data} - "

        value = f"{host}_{port}"
        log_file = File_log().arq_log(value)  # Criando uma instância para chamar arq_log
        log_file.write(log_information + "\n")
        log_file.flush()
        File_log().to_close_log(log_file)


    @staticmethod
    def finaly_log(host, port):
        value = f"{host}_{port}"
        log_file = File_log().arq_log(value)  # Criando uma instância para chamar arq_log
        timestampF = time.strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(timestampF + "\n")
        log_file.flush()
        File_log().to_close_log(log_file)
