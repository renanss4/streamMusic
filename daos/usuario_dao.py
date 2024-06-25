from daos.dao import DAO
from entidades.usuario import Usuario

class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and isinstance(usuario.nome, str):
            super().add(usuario.nome, usuario)

    def get(self, nome: str):
        if isinstance(nome, str):
            return super().get(nome)

    def update(self, usuario: Usuario):
        if usuario is not None and isinstance(usuario, Usuario) and isinstance(usuario.nome, str):
            super().update(usuario.nome, usuario)

    def remove(self, nome: str):
        if isinstance(nome, str):
            super().remove(nome)
