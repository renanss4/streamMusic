from telas.tela_contrato import TelaContrato
from entidades.contrato import Contrato

class ControladorContrato:
    def __init__(self, controlador_sistema):
        self.__contratos = []
        self.__tela_contrato = TelaContrato()
        self.__controlador_sistema = controlador_sistema

    def pegar_contrato_pelo_numero(self, numero: int):
        for contrato in self.__contratos:
            if contrato.numero == numero:
                return contrato
        return None
    
    def listar_contratos(self):
        if self.__contratos:
            for contrato in self.__contratos:
                self.__tela_contrato.mostrar_contrato({
                    'numero': contrato.numero,
                    'artista': contrato.artista,
                    'gravadora': contrato.gravadora
                })
        else:
            self.__tela_contrato.mostrar_mensagem("Nenhum contrato cadastrado.")

    def cadastrar_contrato(self):
        dados_contrato = self.__tela_contrato.pegar_dados_contrato()
        numero = dados_contrato['numero']
        artista = dados_contrato['artista']
        gravadora = dados_contrato['gravadora']

        for contrato in self.__contratos:
            if contrato.numero == numero and contrato.artista == artista and contrato.gravadora == gravadora:
                self.__tela_contrato.mostrar_mensagem("Contrato já existente!")
                return

        contrato = Contrato(numero, artista, gravadora)
        self.__contratos.append(contrato)
        self.__tela_contrato.mostrar_mensagem(f"Contrato de Nº {contrato.numero} adicionado com sucesso.")

    def remover_contrato(self):
        if not self.__contratos:
            self.__tela_contrato.mostrar_mensagem("Nenhum contrato cadastrado.")
            return

        self.listar_contratos()
        numero_contrato = self.__tela_contrato.pegar_dados_contrato()
        contrato = self.pegar_contrato_pelo_numero(numero_contrato)

        if contrato is not None:
            self.__contratos.remove(contrato)
            self.listar_contratos()
            self.__tela_contrato.mostrar_mensagem("Contrato removido com sucesso!")
        else:
            self.__tela_contrato.mostrar_mensagem('ATENÇÃO: Contrato não existente')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        while True:
            opcao = self.__tela_contrato.imprimir_opcoes()
            if opcao == 0:
                self.retornar()
                break
            elif opcao == 1:
                self.cadastrar_contrato()
            elif opcao == 2:
                self.listar_contratos()
            elif opcao == 3:
                self.remover_contrato()
            else:
                self.__tela_contrato.mostrar_mensagem('Opção Inválida!')
