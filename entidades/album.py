from entidades.musica import Musica
from entidades.playlist import Playlist

class Album(Playlist):
    def __init__(self, nome: str, descricao: str = '', musicas: list[Musica] = None):
        super().__init__(nome, descricao, musicas)
