from daos.dao import DAO
from entidades.gravadora import Gravadora

class GravadoraDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, gravadora: Gravadora):
        if gravadora is not None and isinstance(gravadora, Gravadora) and isinstance(gravadora.nome, str):
            super().add(gravadora.nome, gravadora)

    def get(self, nome: str):
        if isinstance(nome, str):
            return super().get(nome)

    def update(self, gravadora: Gravadora):
        if gravadora is not None and isinstance(gravadora, Gravadora) and isinstance(gravadora.nome, str):
            super().update(gravadora.nome, gravadora)

    def remove(self, nome: str):
        if isinstance(nome, str):
            super().remove(nome)
