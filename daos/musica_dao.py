from daos.dao import DAO
from entidades.musica import Musica
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class MusicaDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, musica: Musica):
        try:
            if musica is None or not isinstance(musica, Musica) or not isinstance(musica.nome, str):
                raise InvalidEntityError("Música inválida ou nome não é uma string.")
            super().add(musica.nome, musica)
        except InvalidEntityError as e:
            print(f"Erro ao adicionar música: {e}")

    def get(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome deve ser uma string.")
            musica = super().get(nome)
            if musica is None:
                raise EntityNotFoundError("Música não encontrada.")
            return musica
        except (InvalidEntityError, EntityNotFoundError) as e:
            print(f"Erro ao obter música: {e}")
            return None

    def update(self, musica: Musica):
        try:
            if musica is None or not isinstance(musica, Musica) or not isinstance(musica.nome, str):
                raise InvalidEntityError("Música inválida ou nome não é uma string.")
            super().update(musica.nome, musica)
        except InvalidEntityError as e:
            print(f"Erro ao atualizar música: {e}")

    def remove(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome deve ser uma string.")
            super().remove(nome)
        except InvalidEntityError as e:
            print(f"Erro ao remover música: {e}")
