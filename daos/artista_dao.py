from daos.dao import DAO
from entidades.artista import Artista

class ArtistaDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, artista: Artista):
        if artista is not None and isinstance(artista, Artista) and isinstance(artista.nome, str):
            super().add(artista.nome, artista)

    def get(self, nome: str):
        if isinstance(nome, str):
            return super().get(nome)

    def update(self, artista: Artista):
        if artista is not None and isinstance(artista, Artista) and isinstance(artista.nome, str):
            super().update(artista.nome, artista)

    def remove(self, nome: str):
        if isinstance(nome, str):
            super().remove(nome)
