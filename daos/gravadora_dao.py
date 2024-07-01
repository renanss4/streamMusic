from daos.dao import DAO
from entidades.gravadora import Gravadora
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class GravadoraDAO(DAO):
    def __init__(self):
        super().__init__('gravadora.pkl')

    def add(self, gravadora: Gravadora):
        try:
            if gravadora is None or not isinstance(gravadora, Gravadora) or not isinstance(gravadora.nome, str):
                raise InvalidEntityError("Gravadora inválida ou nome não é uma string.")
            super().add(gravadora.nome, gravadora)
        except InvalidEntityError as e:
            print(f"Erro ao adicionar gravadora: {e}")

    def get(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome deve ser uma string.")
            gravadora = super().get(nome)
            if gravadora is None:
                raise EntityNotFoundError("Gravadora não encontrada.")
            return gravadora
        except (InvalidEntityError, EntityNotFoundError) as e:
            print(f"Erro ao obter gravadora: {e}")

    def update(self, gravadora: Gravadora):
        try:
            if gravadora is None or not isinstance(gravadora, Gravadora) or not isinstance(gravadora.nome, str):
                raise InvalidEntityError("Gravadora inválida ou nome não é uma string.")
            super().update(gravadora.nome, gravadora)
        except InvalidEntityError as e:
            print(f"Erro ao atualizar gravadora: {e}")

    def remove(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome deve ser uma string.")
            super().remove(nome)
        except InvalidEntityError as e:
            print(f"Erro ao remover gravadora: {e}")
