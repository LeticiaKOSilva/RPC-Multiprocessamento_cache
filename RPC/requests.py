import asyncio
import aiohttp
from bs4 import BeautifulSoup

URL_SITE = "https://www.ifsudestemg.edu.br/noticias/barbacena/?b_start:int={}"

# Função assíncrona para buscar títulos de notícias
async def fetch_news_titles(session, page_url, qtd_noticias):
    async with session.get(page_url) as response:
        if response.status != 200:
            print(f"Falha ao obter a página {page_url}")
            return []  # Retorna uma lista vazia em caso de falha na obtenção

        page_content = await response.text()
        soup = BeautifulSoup(page_content, "html.parser")
        news_items = []
        h2_elements = soup.find_all("h2", class_="tileHeadline")
        for h2_element in h2_elements:
            a_element = h2_element.find("a")
            if a_element:
                title = a_element.text.strip()
                url = a_element["href"]
                news_items.append({"title": title, "url": url})
                if len(news_items) == qtd_noticias:
                    break  # Para quando a quantidade desejada de notícias é alcançada
        return news_items

# Função assíncrona para coletar títulos de notícias
async def collect_news_titles(qtd_noticias):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for page_num in range(0, qtd_noticias, 20):  # Supondo 20 notícias por página
            page_url = URL_SITE.format(page_num)
            task = fetch_news_titles(session, page_url, qtd_noticias)
            tasks.append(task)
        
        # Reúne os resultados de todas as tarefas de forma concorrente
        results = await asyncio.gather(*tasks)
        return [item for sublist in results for item in sublist]

# Função para obter os títulos das notícias
def get_titles(qtd_noticias: int):
    # Executa a função assíncrona para coletar os títulos das notícias
    news_items = asyncio.run(collect_news_titles(qtd_noticias))
    values = []
    for idx, item in enumerate(news_items, start=1):
        values.append(f"{idx}. Título: {item['title']}, URL: {item['url']}")
    return values
