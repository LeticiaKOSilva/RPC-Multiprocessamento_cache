# Multiprocessamento & cache
### ->Realizando operações e verificando através da medida de tempo se o multiprocessamento é mais rápido ou não, além da utilização de um cache para facilitar a rapidez do acesso a um método já chamado anteriormente.

- O programa foi feito utilizando a linguagem Python;
- Foram utiliadas diversas biliotecas:
  
      | | NOME | LINK | USABILIDADE | |
      | --- | --- | --- | --- | --- |
  
- As bibliotecas usadas nesse código foram: socket, threading, time, math e multiprocessing, asyncio, aiohttp, bs4, os, pickle;
- Foram criadas 3 classes sendo:
   - Uma classe Client que fornece métodos para a manipualação de dados do cliente e comunicação com o servidor;
   - Uma classe serverNames que possuí o ip e a porta dos servidores que realizam cada uma das operações propostas no RPC, retornado uma lista com todos os ips/portas que realizam tal operação;
   - Uma classe Server que fornece métodos para manipular os dados vindos do cliente, processá-las e devolve-las ao cliente;
- Os arquivos client.py, server.py e serverName só instanciam,inicializam suas classes e chamam os métodos;
- Os arquivos acima se conectam a esse arquivo rpc.py pela importação:
    - client.py: import rpc from Client;
    - serverName: import rpc from ServerNames;
    - server.py: import rpc from Server;
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
