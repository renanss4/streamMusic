from telas.tela_contrato import TelaContrato
from entidades.contrato import Contrato
from entidades.gravadora import Gravadora

class ControladorContrato:
    def __init__(self, controlador_gravadora):
        self.__contratos = []
        self.__tela_contrato = TelaContrato()
        self.__controlador_gravadora = controlador_gravadora

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
                    'gravadora': contrato.gravadora.nome,
                    'data_inicio': contrato.data_inicio,
                    'data_fim': contrato.data_fim
                })
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem("Nenhum contrato cadastrado.")

    def cadastrar_contrato(self):
        dados_contrato = self.__tela_contrato.pegar_dados_contrato()
        numero = int(dados_contrato['numero'])  # Convertendo para int
        artista = dados_contrato['artista']
        gravadora_nome = dados_contrato['gravadora']
        data_inicio = dados_contrato['data_inicio']
        data_fim = dados_contrato['data_fim']

        if data_inicio > data_fim:
            self.__tela_contrato.mostrar_mensagem("A data de início não pode ser maior que a data de fim!")
            return

        for contrato in self.__contratos:
            if contrato.numero == numero and contrato.artista == artista and contrato.gravadora.nome == gravadora_nome:
                self.__tela_contrato.mostrar_mensagem("Contrato já existente!")
                return

        # Verifica se o artista está cadastrado
        # artista = self.__controlador_artista_gravadora.pegar_artista_pelo_nome(dados_contrato['artista'])
        # if not artista:
        #     self.__tela_contrato.mostrar_mensagem("Artista não cadastrado!")
        #     return

        # Verifica se a gravadora está cadastrada
        gravadora = self.__controlador_gravadora.pegar_gravadora_pelo_nome(gravadora_nome)
        if not gravadora:
            self.__tela_contrato.mostrar_mensagem("Gravadora não cadastrada!")
            return

        # Verifica se o contrato já existe
        # for contrato in self.__contratos:
        #     if contrato.numero == numero and contrato.artista == artista and contrato.gravadora == gravadora:
        #         self.__tela_contrato.mostrar_mensagem("Contrato já existente!")
        #         return

        contrato = Contrato(numero, artista, gravadora, data_inicio, data_fim)
        self.__contratos.append(contrato)
        self.__tela_contrato.mostrar_mensagem(f"Contrato de Nº {contrato.numero} adicionado com sucesso.")

    def buscar_contrato_por_artista(self):
        artista = self.__tela_contrato.buscar_por_artista()
        contratos_encontrados = [contrato for contrato in self.__contratos if contrato.artista == artista]
        if contratos_encontrados:
            contratos_dados = [{'numero': contrato.numero, 'artista': contrato.artista, 'gravadora': contrato.gravadora.nome, 'data_inicio': contrato.data_inicio, 'data_fim': contrato.data_fim} for contrato in contratos_encontrados]
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado para o artista {artista}.")

    def buscar_contrato_por_gravadora(self):
        gravadora_nome = self.__tela_contrato.buscar_por_gravadora()
        contratos_encontrados = [contrato for contrato in self.__contratos if contrato.gravadora.nome == gravadora_nome]
        if contratos_encontrados:
            contratos_dados = [{'numero': contrato.numero, 'artista': contrato.artista, 'gravadora': contrato.gravadora.nome, 'data_inicio': contrato.data_inicio, 'data_fim': contrato.data_fim} for contrato in contratos_encontrados]
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado para a gravadora {gravadora_nome}.")

    def buscar_contrato_pelo_numero(self):
        numero = self.__tela_contrato.buscar_por_numero()
        contrato = self.pegar_contrato_pelo_numero(numero)
        if contrato:
            contratos_dados = [{
                'numero': contrato.numero,
                'artista': contrato.artista,
                'gravadora': contrato.gravadora.nome,
                'data_inicio': contrato.data_inicio,
                'data_fim': contrato.data_fim
            }]
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado com o número {numero}.")

    def retornar(self):
        self.__controlador_gravadora.abre_tela()

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
                self.buscar_contrato_por_artista()
            elif opcao == 4:
                self.buscar_contrato_por_gravadora()
            elif opcao == 5:
                self.buscar_contrato_pelo_numero()
            else:
                self.__tela_contrato.mostrar_mensagem('Opção Inválida!')
