from datetime import date


class Gravadora:
    def __init__(self, nome: str, data_fundacao: date, email: str, senha: str, telefone: str):
        self.__nome = nome
        self.__data_fundacao = data_fundacao
        self.__email = email
        self.__senha = senha
        self.__telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_fundacao(self):
        return self.__data_fundacao

    @data_fundacao.setter
    def data_fundacao(self, data_fundacao):
        self.__data_fundacao = data_fundacao

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
