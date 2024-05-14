from abc import abstractmethod, ABC
from datetime import date
from playlist import Playlist

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, email: str, senha: str, telefone: int, data_nascimento: date):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__telefone = telefone    
        self.__playlists = [Playlist('Músicas Favoritas', 'Lista de músicas favoritas')]
        self.__perfil = {"nome": nome, "email": email, "telefone": telefone}
        self.__artistas_seguidos = []

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

    def cadastrar_perfil(self, nome: str, email: str, telefone: int):
        self.__perfil = {"nome": nome, "email": email, "telefone": telefone}

    def mostrar_perfil(self):
        return self.__perfil

    def editar_perfil(self, nome: str, email: str, telefone: int):
        self.__perfil["nome"] = nome
        self.__perfil["email"] = email
        self.__perfil["telefone"] = telefone

    def remover_perfil(self):
        self.__perfil = {}

    def seguir_artista(self, artista: str):
        if artista not in self.artistas_seguidos:
            self.__artistas_seguidos.append(artista)

    def deixar_de_seguir(self, artista: str):
        if artista in self.artistas_seguidos:
            self.__artistas_seguidos.remove(artista)

    def mostrar_artistas_seguidos(self):
        return self.__artistas_seguidos