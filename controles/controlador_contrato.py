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
        for contrato in self.__contratos:
            self.__tela_contrato.mostrar_contrato({
                'numero': contrato.numero,
                'artista': contrato.artista,
                'gravadora': contrato.gravadora
            })

    def cadastrar_contrato(self):
        dados_contrato = self.__tela_contrato.pegar_dados_contrato()
        contrato = Contrato(
            dados_contrato['numero'],
            dados_contrato['artista'],
            dados_contrato['gravadora']
        )
        self.__contratos.append(contrato)
        self.__tela_contrato.mostrar_mensagem(f"Contrato de Nº {contrato.numero} adicionado com sucesso.")

    def remover_contrato(self):
        self.listar_contratos()
        numero_contrato = self.__tela_contrato.pegar_dados_contrato()
        contrato = self.pegar_contrato_pelo_numero(numero_contrato)

        if contrato is not None:
            self.__contratos.remove(contrato)
            self.listar_contratos()
            print('foi apaga com sucesso')
        else:
            self.__tela_contrato.mostrar_mensagem('ATENÇÃO: Contrato não existente')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_contrato,
            2: self.listar_contratos,
            3: self.remover_contrato,
            0: self.retornar
        }

        rodando = True
        while rodando:
            opcao = self.__tela_contrato.imprimir_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_contrato.mostrar_mensagem('Opção Inválida!')
