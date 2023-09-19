import pickle
import os

CACHE_FILE_NAME = 'cache.txt'

class Cache:
    def __init__(self):
        self.cache = self.import_cache()

    def import_cache(self):
        if not os.path.exists(CACHE_FILE_NAME):
            return {}

        try:
            with open(CACHE_FILE_NAME, 'rb') as file:
                cache = pickle.load(file)
                return cache
        except Exception as e:
            print("Erro ao importar o cache:", e)
            return {}

    def export_cache(self):
        try:
            with open(CACHE_FILE_NAME, 'wb') as file:
                pickle.dump(self.cache, file)
                print("Cache exportado com sucesso.")
        except Exception as e:
            print("Erro ao exportar o cache:", e)

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        if len(self.cache) >= 5:
            self.update_first_line(key,value)
        else :
            self.cache[key] = value
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

                self.export_cache()





