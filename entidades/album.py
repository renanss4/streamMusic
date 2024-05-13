from playlist import Playlist

class Album(Playlist):
    def __init__(self, nome: str, descricao=''):
        super().__init__(nome, descricao)