from daos.dao import DAO
from entidades.usuario import Usuario
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class UsuarioDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, usuario: Usuario):
        try:
            if not isinstance(usuario, Usuario) or not isinstance(usuario.nome, str):
                raise InvalidEntityError("Usuário inválido ou nome do usuário não é uma string.")
            super().add(usuario.nome, usuario)
        except InvalidEntityError as e:
            print(f"Erro ao adicionar usuário: {e}")

    def get(self, nome: str):
        try:
            result = super().get(nome)
            if result is None:
                raise EntityNotFoundError(f"Usuário '{nome}' não encontrado.")
            return result
        except EntityNotFoundError as e:
            print(f"Erro ao buscar usuário: {e}")

    def update(self, usuario: Usuario):
        try:
            if not isinstance(usuario, Usuario) or not isinstance(usuario.nome, str):
                raise InvalidEntityError("Usuário inválido ou nome do usuário não é uma string.")
            super().update(usuario.nome, usuario)
        except InvalidEntityError as e:
            print(f"Erro ao atualizar usuário: {e}")

    def remove(self, nome: str):
        try:
            result = super().remove(nome)
            if result is None:
                raise EntityNotFoundError(f"Usuário '{nome}' não encontrado para remoção.")
        except EntityNotFoundError as e:
            print(f"Erro ao remover usuário: {e}")
