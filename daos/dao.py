import pickle
from abc import ABC
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class DAO(ABC):
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        try:
            with open(self.__datasource, 'wb') as f:
                pickle.dump(self.__cache, f)
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")

    def __load(self):
        try:
            with open(self.__datasource, 'rb') as f:
                self.__cache = pickle.load(f)
        except FileNotFoundError:
            print("Arquivo de dados não encontrado, criando um novo.")
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")

    def add(self, key, value):
        if key is None or value is None:
            raise InvalidEntityError("Chave ou valor não pode ser None.")
        self.__cache[key] = value
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            raise EntityNotFoundError(f"Chave '{key}' não encontrada.")

    def get_all(self):
        return list(self.__cache.values())

    def update(self, key, value):
        if key not in self.__cache:
            raise EntityNotFoundError(f"Chave '{key}' não encontrada para atualização.")
        self.__cache[key] = value
        self.__dump()

    def remove(self, key):
        try:
            del self.__cache[key]
            self.__dump()
        except KeyError:
            raise EntityNotFoundError(f"Chave '{key}' não encontrada para remoção.")
