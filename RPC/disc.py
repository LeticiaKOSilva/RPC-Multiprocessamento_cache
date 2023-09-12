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
        self.cache[key] = value
        self.export_cache()

    def remove(self, key):
        if key in self.cache:
            del self.cache[key]
            self.export_cache()
