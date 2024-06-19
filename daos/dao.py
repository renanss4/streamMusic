import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except:
            self.__dump()

    @abstractmethod
    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    @abstractmethod
    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, 'rb'))

    def add(self, key, value):
        self.__cache[key] = value
        self.__dump()

    def get(self, key):
        try:
            return self.__cache[key]
        except:
            return None
        
    def get_all(self):
        try:
            return self.__cache.values()
        except:
            return None
        
    def update(self, key, value):
        try:
            if(self.__cache[key] != None):
                self.__cache[key] = value #atualiza a entrada
                self.__dump()  #atualiza o arquivo
        except KeyError:
            pass  # implementar aqui o tratamento da exceção



    def remove(self, key):
        try:
            del self.__cache[key]
            self.__dump()
        except KeyError:
            pass