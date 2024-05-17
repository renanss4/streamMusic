from entidades.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome: str, username: str, email: str, telefone: int):
        super().__init__(nome, username, email, telefone)
