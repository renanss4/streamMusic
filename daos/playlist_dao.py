from daos.dao import DAO
from entidades.playlist import Playlist
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class PlaylistDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, playlist: Playlist):
        try:
            if playlist is None or not isinstance(playlist, Playlist) or not isinstance(playlist.nome, str):
                raise InvalidEntityError("Playlist inválida ou nome não é uma string.")
            super().add(playlist.nome, playlist)
        except InvalidEntityError as e:
            print(f"Erro ao adicionar playlist: {e}")

    def get(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome deve ser uma string.")
            playlist = super().get(nome)
            if playlist is None:
                raise EntityNotFoundError("Playlist não encontrada.")
            return playlist
        except (InvalidEntityError, EntityNotFoundError) as e:
            print(f"Erro ao obter playlist: {e}")
            return None

    def update(self, playlist: Playlist):
        try:
            if playlist is None or not isinstance(playlist, Playlist) or not isinstance(playlist.nome, str):
                raise InvalidEntityError("Playlist inválida ou nome não é uma string.")
            super().update(playlist.nome, playlist)
        except InvalidEntityError as e:
            print(f"Erro ao atualizar playlist: {e}")

    def remove(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome deve ser uma string.")
            super().remove(nome)
        except InvalidEntityError as e:
            print(f"Erro ao remover playlist: {e}")
