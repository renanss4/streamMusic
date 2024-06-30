from daos.dao import DAO
from entidades.artista import Artista
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class ArtistaDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, artista: Artista):
        try:
            if artista is None or not isinstance(artista, Artista) or not isinstance(artista.nome, str):
                raise InvalidEntityError("Artista inválido ou nome não é uma string.")
            super().add(artista.nome, artista)
        except InvalidEntityError as e:
            print(f"Erro ao adicionar artista: {e}")

    def get(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome deve ser uma string.")
            artista = super().get(nome)
            if artista is None:
                raise EntityNotFoundError("Artista não encontrado.")
            return artista
        except (InvalidEntityError, EntityNotFoundError) as e:
            print(f"Erro ao obter artista: {e}")

    def update(self, artista: Artista):
        try:
            if artista is None or not isinstance(artista, Artista) or not isinstance(artista.nome, str):
                raise InvalidEntityError("Artista inválido ou nome não é uma string.")
            super().update(artista.nome, artista)
        except InvalidEntityError as e:
            print(f"Erro ao atualizar artista: {e}")

    def remove(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome deve ser uma string.")
            super().remove(nome)
        except InvalidEntityError as e:
            print(f"Erro ao remover artista: {e}")
