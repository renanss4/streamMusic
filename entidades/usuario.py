from entidades.pessoa import Pessoa


class Usuario(Pessoa):
    def __init__(self, nome: str, identificador: str, email: str, senha: str, telefone: int):
        super().__init__(nome, identificador, email, senha, telefone)
