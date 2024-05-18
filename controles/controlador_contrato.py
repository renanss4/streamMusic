from telas.tela_contrato import TelaContrato
from entidades.contrato import Contrato

class ControladorContrato:
    def __init__(self, controlador_artista_gravadora):
        self.__contratos = []
        self.__tela_contrato = TelaContrato()
        self.__controlador_artista_gravadora = controlador_artista_gravadora

    def pegar_contrato_pelo_numero(self, numero: int):
        for contrato in self.__contratos:
            if contrato.numero == numero:
                return contrato
        return None
    
    def listar_contratos(self):
        if self.__contratos:
            contratos_dados = []
            for contrato in self.__contratos:
                contratos_dados.append({
                    'numero': contrato.numero,
                    'artista': contrato.artista,
                    'gravadora': contrato.gravadora,
                    'data_inicio': contrato.data_inicio,
                    'data_fim': contrato.data_fim
                })
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem("Nenhum contrato cadastrado.")

    def cadastrar_contrato(self):
        dados_contrato = self.__tela_contrato.pegar_dados_contrato()
        numero = dados_contrato['numero']
        artista = dados_contrato['artista']
        gravadora = dados_contrato['gravadora']
        data_inicio = dados_contrato['data_inicio']
        data_fim = dados_contrato['data_fim']

        if data_inicio > data_fim:
            self.__tela_contrato.mostrar_mensagem("A data de início não pode ser maior que a data de fim!")
            return

        for contrato in self.__contratos:
            if contrato.numero == numero and contrato.artista == artista and contrato.gravadora == gravadora:
                self.__tela_contrato.mostrar_mensagem("Contrato já existente!")
                return

        contrato = Contrato(numero, artista, gravadora, data_inicio, data_fim)
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

    def buscar_contrato_por_artista(self):
        artista = self.__tela_contrato.buscar_por_artista()
        contratos_encontrados = [contrato for contrato in self.__contratos if contrato.artista == artista]
        if contratos_encontrados:
            contratos_dados = [{'numero': contrato.numero, 'artista': contrato.artista, 'gravadora': contrato.gravadora, 'data_inicio': contrato.data_inicio, 'data_fim': contrato.data_fim} for contrato in contratos_encontrados]
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado para o artista {artista}.")

    def buscar_contrato_por_gravadora(self):
        gravadora = self.__tela_contrato.buscar_por_gravadora()
        contratos_encontrados = [contrato for contrato in self.__contratos if contrato.gravadora == gravadora]
        if contratos_encontrados:
            contratos_dados = [{'numero': contrato.numero, 'artista': contrato.artista, 'gravadora': contrato.gravadora, 'data_inicio': contrato.data_inicio, 'data_fim': contrato.data_fim} for contrato in contratos_encontrados]
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado para a gravadora {gravadora}.")

    def buscar_contrato_pelo_numero(self):
        numero = self.__tela_contrato.buscar_por_numero()
        contrato = self.pegar_contrato_pelo_numero(numero)
        if contrato:
            contratos_dados = [{
                'numero': contrato.numero,
                'artista': contrato.artista,
                'gravadora': contrato.gravadora,
                'data_inicio': contrato.data_inicio,
                'data_fim': contrato.data_fim
            }]
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado com o número {numero}.")

    def retornar(self):
        self.__controlador_artista_gravadora.abre_tela()

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
            elif opcao == 4:
                self.buscar_contrato_por_artista()
            elif opcao == 5:
                self.buscar_contrato_por_gravadora()
            elif opcao == 6:
                self.buscar_contrato_pelo_numero()
            else:
                self.__tela_contrato.mostrar_mensagem('Opção Inválida!')
