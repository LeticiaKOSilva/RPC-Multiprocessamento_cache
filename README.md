# Multiprocessamento & cache
### ->Realizando operações e verificando através da medida de tempo se o multiprocessamento é mais rápido ou não, além da utilização de um cache para facilitar a rapidez do acesso a um método já chamado anteriormente.

## Proposta de atividade
  - Atividade proposta na matéria de Sistemas Distribuídos lecionada pelo professor Rafael.
  - A idéia é durante as semanas realizar novas entregas de novas funcionalidades do RPC(Remote Procedure Call) que é a comunicação que permite que um programa em um computador solicite a execução de um procedimento (função, método) em um espaço de endereço diferente, geralmente em outro processo ou em um sistema distribuído. 
  - Na tabela a seguir temos a definiçaõ das tarefas entregadas a cada semana.
    
    | | SEMANA | FUNCIONALIDADES | |
    | --- | --- | --- | --- |
    || Semana 1 | Criação dos sockets do cliente e servidor; <br> Elaboração dos métodos soma, subtração, divisão e multiplicação do lado do cliente e do servidor.||
    
## Resultado da atividade
  - O programa foi feito utilizando a linguagem Python;
  - A seguir temos a imagem da primeira interface gráfica que aparece para o cliente:
    
    <img src="https://github.com/LeticiaKOSilva/RPC-Multiprocessamento_cache/blob/main/Imagens_rpc/interface_rpc.jpg" width="400px"/>
    
- Depois ao escolher uma das opções acima e precionar o seu botão correspondente, neste exemplo escolhemos o botão operações matemáticas.

    <img src="https://github.com/LeticiaKOSilva/RPC-Multiprocessamento_cache/blob/main/Imagens_rpc/calculadora_rpc.jpg" width="300px"/>
    
- A escolha da operação matemática foi a subtração, onde fizemos 78 - 58 e agora temos o resultado desta operação.
    <img src="https://github.com/LeticiaKOSilva/RPC-Multiprocessamento_cache/blob/main/Imagens_rpc/resultado_operacao_rpc.jpg" width="400px"/>
    
## Bibliotecas utilizadas na elaboração dessa atividade

- A seguir apresentamos tabela com as bibliotecas.

    | | BIBLIOTECA | MÉTODO ESPECÍFICO | DESCRIÇÃO DE USO | |
    | --- | --- | --- | --- | --- |
    || socket | | Criação e comunicação entre meus sockets: cliente, servidor de nome e servidor. ||
    || threading | | Para a criação de threads caso haja mais de um cliente acessando ao mesmo tempo. ||
    || multiprocessing | | Para aumentar a rapides do processo. ||
    || tkinter | messagebox, simpledialog, scrolledtext | Métodos utilizados para auxiliar na criação da interface gráfica. ||
    || sys | | Operações com o sistema operacional. ||
    || asyncio | | Para a busca de notícias do ifet ocorrer de forma assíncrona. ||
    || aiohttp | | Para junto a biblioteca asyncio fazer a busca do título e link das notícias. ||
    || bs4 | BeautifulSoup | Método que auxlia na manipulação de texto de marcação do html. ||
    || time | | Manipulação do tempo no arquivo de log. ||
    || validate_docbr | CPF | Utilizado para a validação de cpfs. ||
    || json | | Manipulação de json. ||
    || datetime | datetime, timedelta | Manipulação de data e hora para o cache ||
    || Crypto.Cipher | AES | Padrão de criptografia simétrica amplamente utilizada. ||
    || Crypto.Util.Padding | pad, unpad | Utilização dos métodos para adicionar ou remover preenchimento em dados antes de criptografá-los ou após descriptografá-los. ||
    || base64 | | Usada para codificar e decodificar dados em formato base64. ||
  
  
  
  
  
  
  


- O código possui multiprocessos, o servidor pode atender a mais de um cliente por criar uma thread para cada um desses clientes;
- O cache é um dicionário que é criado logo no construtor do lado do cliente onde primeiro se verifica se o método existe no cache se não existir ele o salva se existir ele o chama;
- Pra verificar a eficiência do multiprocessamento é feito uma verificação numa lista de números que verifica se um valor é primo ou não e retorna uma lista de booleanos, essa verificação e feita com e sem multiprocessamento e através da biblioteca time conseguimos calcular o tempo de execução de ambas as formas.
- Agora com a ajuda da classe Cache disponível no arquivo disc.py foi feito um cache em disco, onde:
  - Uma variável verifica o tempo em que o cache em disco será atualizado;
  - É outra variável que delimita um tamanho de cache, onde quando este limite e ultrapassado o cache mais antigo é excluído.
- O novo método da classe Client last_news_if_barbacena tem como função retornar ao cliente uma lista com o número de notícias que deseja extrair do site (https://www.ifsudestemg.edu.br/noticias/barbacena/?b_start:int={}).
- O arquivo requests.py tem várias funções que tem como objetivos principais:
   - Fazer uma requisição uma requisição no site para extrair seu html;
   - Pegar do código html o título e o link de cada notícia;
   - Formata-las em título e link;
   - E retornar em forma de lista.
- O método def last_news_if_barbacena(self, qtd_noticias: int) -> [], deve além de adicionar ao cache as notícias solicitadas como:
     - Considerar que toda vez que for solicitado uma nova quantidade de notícias, verificar se no cache já existe uma solicitação igual ou maior a essa. Por isso se existir ele retorna os dados correspondentes ao número solicitado pelo usuário;
     - De 5 em 5 minutos ele deve ir ao site (https://www.ifsudestemg.edu.br/noticias/barbacena/?b_start:int={}) e atualizar o cache com as novas notícias.
