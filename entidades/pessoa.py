from abc import abstractclassmethod, ABC
from datetime import date
from playlist import Playlist

class Pessoa(ABC):
    @abstractclassmethod
    def __init__(self, nome: str, email: str, senha: str, telefone: int,
                 nome_playlist='Músicas Favoritas', descricao='Lista de músicas favoritas'):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__telefone = telefone    
        self.__playlists = [Playlist(nome_playlist, descricao)]

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def playlists(self):
        return self.__playlists
