from daos.dao import DAO
from entidades.contrato import Contrato
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class ContratoDAO(DAO):
    def __init__(self):
        super().__init__('data.pkl')

    def add(self, contrato: Contrato):
        try:
            if contrato is None or not isinstance(contrato, Contrato) or not isinstance(contrato.numero, int):
                raise InvalidEntityError("Contrato inválido ou número do contrato não é um inteiro.")
            super().add(contrato.numero, contrato)
        except InvalidEntityError as e:
            print(f"Erro ao adicionar contrato: {e}")

    def get(self, numero: int):
        try:
            contrato = super().get(numero)
            if contrato is None:
                raise EntityNotFoundError(f"Contrato com número {numero} não encontrado.")
            return contrato
        except EntityNotFoundError as e:
            print(f"Erro ao buscar contrato: {e}")

    def update(self, contrato: Contrato):
        try:
            if contrato is None or not isinstance(contrato, Contrato) or not isinstance(contrato.numero, int):
                raise InvalidEntityError("Contrato inválido ou número do contrato não é um inteiro.")
            super().update(contrato.numero, contrato)
        except InvalidEntityError as e:
            print(f"Erro ao atualizar contrato: {e}")

    def remove(self, numero: int):
        try:
            result = super().remove(numero)
            if result is None:
                raise EntityNotFoundError(f"Contrato com número {numero} não encontrado para remoção.")
        except EntityNotFoundError as e:
            print(f"Erro ao remover contrato: {e}")
