from daos.dao import DAO
from entidades.musica import Musica

class MusicaDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, musica: Musica):
        if musica is not None and isinstance(musica, Musica) and isinstance(musica.nome, str):
            super().add(musica.nome, musica)

    def get(self, nome: str):
        if isinstance(nome, str):
            return super().get(nome)

    def update(self, musica: Musica):
        if musica is not None and isinstance(musica, Musica) and isinstance(musica.nome, str):
            super().update(musica.nome, musica)

    def remove(self, nome: str):
        if isinstance(nome, str):
            super().remove(nome)
