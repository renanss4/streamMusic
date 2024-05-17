from entidades.pessoa import Pessoa
from entidades.musica import Musica
from entidades.album import Album


class Artista(Pessoa):
    def __init__(self, nome: str, username: str, email: str, telefone: int):
        super().__init__(nome, username, email, telefone)
        self.__albuns = [Album(f'Mix do {nome}', f'Um mix do artista {nome}')]
        self.__musicas = [Musica()]

    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas
