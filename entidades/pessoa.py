from abc import abstractmethod, ABC
from entidades.playlist import Playlist
from datetime import date

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, email: str, telefone: int, data_nascimento: date):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__data_nascimento = data_nascimento
        self.__playlists = [Playlist('Músicas Favoritas', 'Lista de músicas favoritas')]
        self.__artistas_seguidos = []

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def playlists(self):
        return self.__playlists

    @property
    def perfil(self):
        return self.__perfil

    @property
    def artistas_seguidos(self):
        return self.__artistas_seguidos
