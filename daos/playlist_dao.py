from daos.dao import DAO
from entidades.playlist import Playlist

class PlaylistDAO(DAO):
    def __init__(self):
        super().__init__('playlists.pkl')

    def add(self, playlist: Playlist):
        if playlist is not None and isinstance(playlist, Playlist) and isinstance(playlist.nome, str):
            super().add(playlist.nome, playlist)

    def get(self, nome: str):
        if isinstance(nome, str):
            return super().get(nome)

    def update(self, playlist: Playlist):
        if playlist is not None and isinstance(playlist, Playlist) and isinstance(playlist.nome, str):
            super().update(playlist.nome, playlist)

    def remove(self, nome: str):
        if isinstance(nome, str):
            super().remove(nome)
