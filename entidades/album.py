from playlist import Playlist


class Album(Playlist):
    def __init__(self, musicas, nome: str, descricao: str, capa):
        super().__init__(nome, descricao, musicas)
        self.__capa = capa

    @property
    def capa(self):
        return self.__capa

    @capa.setter
    def capa(self, capa):
        self.__capa = capa
