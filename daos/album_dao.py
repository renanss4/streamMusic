from daos.dao import DAO
from entidades.album import Album

class AlbumDAO(DAO):
    def __init__(self):
        super().__init__('albuns.pkl')

    def add(self, album: Album):
        if album is not None and isinstance(album, Album) and isinstance(album.nome, str):
            super().add(album.nome, album)

    def get(self, nome: str):
        if isinstance(nome, str):
            return super().get(nome)

    def update(self, album: Album):
        if album is not None and isinstance(album, Album) and isinstance(album.nome, str):
            super().update(album.nome, album)

    def remove(self, nome: str):
        if isinstance(nome, str):
            super().remove(nome)
