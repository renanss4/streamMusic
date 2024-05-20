from entidades.pessoa import Pessoa
from datetime import date


class Usuario(Pessoa):
    def __init__(self, nome: str, email: str, telefone: int, data_nascimento: date):
        super().__init__(nome, email, telefone, data_nascimento)