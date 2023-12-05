# Multiprocessamento & cache
### ->Realizando operações e verificando através da medida de tempo se o multiprocessamento é mais rápido ou não, além da utilização de um cache para facilitar a rapidez do acesso a um método já chamado anteriormente.

## Proposta de atividade
  - Atividade proposta na matéria de Sistemas Distribuídos lecionada pelo professor Rafael.
  - A idéia é durante as semanas realizar novas entregas de novas funcionalidades do RPC(Remote Procedure Call) que é a comunicação que permite que um programa em um computador solicite a execução de um procedimento (função, método) em um espaço de endereço diferente, geralmente em outro processo ou em um sistema distribuído. 
  - Na tabela a seguir temos a definiçaõ das tarefas entregadas a cada semana.
    
    | | SEMANA | FUNCIONALIDADES | |
    | --- | --- | --- | --- |
    || Semana 1 | - Criação dos sockets do cliente e servidor em TCP ; <br> - Elaboração dos métodos soma, subtração, divisão e multiplicação do lado do cliente e do servidor.||
    || Semana 2 | - Adicionar a operação <strong>is_prime(number: int) -> bool no RPC</strong> ;<br> - Faça um método <strong> is_primes(numbres:list) -> list </strong>com a utilização de multiprocessos;<br> - Exibir números primos de 10 a 10000;<br> - Utilizar a biblioteca time para contabilizar o tempo entre a procura de números primos com e sem a utilização da biblioteca multiprocessing. ||
    || Semana 3 | Implementação de um cache em memória no cliente para todas as operações do RPC. ||
    || Semana 4 | - Aprimoramento do cache, agora ele deve ser persistido em disco;<br> - Criação de uma constante que verifica um tempo mínimo para a sincronização;<br> - Constante com o número máximo de registros do cache em disco;<br> - Quando o número de registros for ultrapassado substituir o registro mais velho pelo novo.||
    || Semana 5 | - Adicionar a operação <strong> last_news_if_barbacena(qtd_noticias : int) -> []</strong>;<br> - A operação receberá como parâmetro o número de notícias que deseja pesquisar e deve retornar um lista com o título e link das notícias;<br> - A operação utiliza o cache criado na semana 4; <br> - As notícias devem ser coletadas com paralelismo;<br> - link do site das notícias: (https://www.ifsudestemg.edu.br/noticias/barbacena/?b_start:int={}) ||
    || Semana 6 | - O cache deve considerar que quando o método <strong>last_news_if_barbacena</strong> for chamado que haja a verificação no cache, onde se houver respostas com número de notícias menores qou iguais que elas sejam aproveitadas;<br> - O cache deve ser consistente com as atualizações do site do ifet que deve realizar a sincronização de 5 em 5 minutos. ||
    || Semana 7 | - Elaboração de um servidor de nomes que irá estabelecer/gerenciar a conexão entre o cliente e o servidor; <br> - O cliente RPC agora será instanciado recebendo a porta desse servidor de nomes; <br> - A conexão entre cliente e servidor de nomes será UDP onde o cliente passara a operação que deseja solicitar ao servidor;<br> - O servidor de nomes deve retornar uma lista com o ip dos servidores que implementam a operação solicitada pelo cliente;<br> - O cliente irá escolher um desses servidores de forma aleatória. ||
    || Semana 8, 9 e 10 | - Criação do método <strong> valida_CPF(str:cpf) -> bool</strong>;<br> - Sistema de log onde um único arquivo texto (por servidor) deve armazenar para cada requisição recebida: <strong>timestamp, IP do cliente, nome da operação, tempo de resposta</strong>;<br> - Criação de um arquivo Shell Script que leia esses arquivos log e retorne o(s) ip(s) das requisições feitas;<br> - Criar um notebook no Kaggle ou Google Colab, fazer o upload de um arquivo de log, transformar seus dados em um dataframe Pandas. A partir dele, gerar:<br> a) Um gráfico de pizza com a porcentagem de chamadas por operação.<br> b) Um gráfico de barras (horizontal) com a quantidade de requisições por endereço IP.<br> c)Um gráfico de barras (vertical) com a quantidade de requisições por horário do dia.<br> d) Um gráfico de dispersão onde cada ponto é uma requisição, o eixo x é a operação chamada e o eixo y é o tempo de resposta.<br> - Implementação de criptografia nos envios e recebimentos das chamadas, podendo utiliar criptografia nas mensagens ou sockets seguros (SSL). ||
    || Semana 11 | - Criação de uma GUI para que o usuário possa interagir com as operações implementadas pelo servidor; <br> - A GUI pode ser desktop ou web, em linguagem/toolkit livre. ||
    
    
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
