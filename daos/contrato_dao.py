from daos.dao import DAO
from entidades.contrato import Contrato

class ContratoDAO(DAO):
    def __init__(self):
        super().__init__('contratos.pkl')

    def add(self, contrato: Contrato):
        if contrato is not None and isinstance(contrato, Contrato) and isinstance(contrato.numero, int):
            super().add(contrato.numero, contrato)

    def get(self, numero: int):
        if isinstance(numero, int):
            return super().get(numero)

    def update(self, contrato: Contrato):
        if contrato is not None and isinstance(contrato, Contrato) and isinstance(contrato.numero, int):
            super().update(contrato.numero, contrato)

    def remove(self, numero: int):
        if isinstance(numero, int):
            super().remove(numero)
