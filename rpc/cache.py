import pickle
import os
import re
from datetime import datetime, timedelta
from rpc.request import Request
from rpc.constantes import Constantes

class Cache:
    def __init__(self):
        self.cache = self.import_cache()

    def import_cache(self):
        if not os.path.exists(Constantes.CACHE_FILE_NAME):
            return {}

        try:
            with open(Constantes.CACHE_FILE_NAME, 'rb') as file:
                cache = pickle.load(file)
                return cache
        except Exception as e:
            print("Erro ao importar o cache:", e)
            return {}

    def export_cache(self):
        try:
            with open(Constantes.CACHE_FILE_NAME, 'wb') as file:
                pickle.dump(self.cache, file)
                print("Cache exportado com sucesso.")
        except Exception as e:
            print("Erro ao exportar o cache:", e)

    def get(self, key):
        return self.cache.get(key)

    def is_cache_outdated(self, data_str):
        if data_str in self.cache:
            last_update_time = self.cache[data_str].get('last_updated')
            if last_update_time:
                current_time = datetime.now()
                return (current_time - last_update_time) > timedelta(minutes=5)
        return True

    def update_last_updated_time(self):
        self.cache['last_updated'] = datetime.now()
        self.export_cache()

    def get_or_fetch_news(self, data_str, qtd_noticias):
        if self.is_cache_outdated(data_str):
            new_news = self.fetch_and_update_cache(data_str, qtd_noticias)
            return new_news
        else:
            return self.get_v(data_str, qtd_noticias)

    def fetch_and_update_cache(self, data_str, qtd_noticias):
        request_object = Request()  # Instancie um objeto Request
        new_news = request_object.fetch_news_from_website(qtd_noticias)
        self.cache[data_str] = {
            'last_updated': datetime.now(),
            data_str: new_news
        }
        self.export_cache()
        return new_news

    def get_v(self, data_str, quantidade):
        cached_news = self.cache.get(data_str, {}).get('conteudo', [])
        if cached_news and len(cached_news) >= quantidade:
            return cached_news[:quantidade]
        else:
            return []

    def set(self, key, value):
        if len(self.cache) >= 5:
            self.update_first_line(key,value)
            self.update_last_updated_time()
        else:
            self.cache[key] = value
            self.update_last_updated_time()
            self.export_cache()

    def remove(self, key):
        if key in self.cache:
            del self.cache[key]
            self.export_cache()
    
    def update_first_line(self, new_key, new_value):
        if self.cache:
            keys = list(self.cache.keys())
            if keys:
                # Obtém a chave na primeira posição
                first_key = keys[0]
                # Obtém o valor da chave na primeira posição
                first_value = self.cache[first_key]

                # Remove a entrada com a chave na primeira posição
                del self.cache[first_key]

                # Cria um novo dicionário com a nova chave e valor
                updated_cache = {new_key: new_value}
                
                # Adiciona as chaves e valores originais de volta no dicionário
                for key in keys:
                    if key != first_key:
                        updated_cache[key] = self.cache[key]

                # Atualiza o cache com as alterações
                self.cache = updated_cache
