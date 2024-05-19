from entidades.pessoa import Pessoa
from entidades.musica import Musica
from entidades.album import Album
from datetime import date

class Artista(Pessoa):
    def __init__(self, nome: str, email: str, telefone: int, data_nascimento: date):
        super().__init__(nome, email, telefone, data_nascimento)
        self.__albuns = [Album(f'Mix do {nome}', f'Um mix do artista {nome}')]
        self.__musicas = []  # Inicializando a lista de músicas vazia

    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas
