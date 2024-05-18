from entidades.artista import Artista
from entidades.gravadora import Gravadora
from datetime import date


class Contrato:
    def __init__(self, numero: int, artista: Artista, gravadora: Gravadora):
        self.__numero = numero
        self.__artista = artista
        self.__gravadora = gravadora
        # self.__data_inicio = data_inicio
        # self.__data_fim = data_fim

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def artista(self):
        return self.__artista

    @artista.setter
    def artista(self, artista):
        self.__artista = artista

    @property
    def gravadora(self):
        return self.__gravadora

    @gravadora.setter
    def gravadora(self, gravadora):
        self.__gravadora = gravadora

    # @property
    # def data_inicio(self):
    #     return self.__data_inicio

    # @data_inicio.setter
    # def data_inicio(self, data_inicio):
    #     self.__data_inicio = data_inicio

    # @property
    # def data_fim(self):
    #     return self.__data_fim

    # @data_fim.setter
    # def data_fim(self, data_fim):
    #     self.__data_fim = data_fim
