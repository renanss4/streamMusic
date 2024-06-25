from telas.tela_contrato import TelaContrato
from entidades.contrato import Contrato
from daos.contrato_dao import ContratoDAO

class ControladorContrato:
    """Controlador para gerenciar operações relacionadas a contratos."""

    def __init__(self, controlador_gravadora):
        """Inicializa o controlador de contrato."""
        self.__contrato_dao = ContratoDAO()
        self.__tela_contrato = TelaContrato()
        self.__controlador_gravadora = controlador_gravadora

    def pegar_contrato_pelo_numero(self, numero: int):
        """Retorna o contrato correspondente ao número fornecido."""
        return self.__contrato_dao.get(numero)

    def listar_contratos(self):
        """Lista todos os contratos cadastrados."""
        contratos = self.__contrato_dao.get_all()
        if contratos:
            contratos_dados = []
            for contrato in contratos:
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
        """Realiza o cadastro de um novo contrato."""
        dados_contrato = self.__tela_contrato.pegar_dados_contrato()
        numero = int(dados_contrato['numero'])
        artista = dados_contrato['artista']
        gravadora_nome = dados_contrato['gravadora']
        data_inicio = dados_contrato['data_inicio']
        data_fim = dados_contrato['data_fim']

        if data_inicio > data_fim:
            self.__tela_contrato.mostrar_mensagem("A data de início não pode ser maior que a data de fim!")
            return

        if self.pegar_contrato_pelo_numero(numero):
            self.__tela_contrato.mostrar_mensagem("Contrato já existente!")
            return

        gravadora = self.__controlador_gravadora.pegar_gravadora_pelo_nome(gravadora_nome)
        if not gravadora:
            self.__tela_contrato.mostrar_mensagem("Gravadora não cadastrada!")
            return

        contrato = Contrato(numero, artista, gravadora, data_inicio, data_fim)
        self.__contrato_dao.add(contrato)
        self.__tela_contrato.mostrar_mensagem(f"Contrato de Nº {contrato.numero} adicionado com sucesso.")

    def buscar_contrato_por_artista(self):
        """Busca e exibe contratos de um determinado artista."""
        artista = self.__tela_contrato.buscar_por_artista()
        contratos = self.__contrato_dao.get_all()
        contratos_encontrados = [contrato for contrato in contratos if contrato.artista == artista]

        if contratos_encontrados:
            contratos_dados = []
            for contrato in contratos_encontrados:
                contratos_dados.append({
                    'numero': contrato.numero,
                    'artista': contrato.artista,
                    'gravadora': contrato.gravadora.nome,
                    'data_inicio': contrato.data_inicio,
                    'data_fim': contrato.data_fim
                })
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado para o artista {artista}.")

    def buscar_contrato_por_gravadora(self):
        """Busca e exibe contratos de uma determinada gravadora."""
        gravadora_nome = self.__tela_contrato.buscar_por_gravadora()
        contratos = self.__contrato_dao.get_all()
        contratos_encontrados = [contrato for contrato in contratos if contrato.gravadora.nome == gravadora_nome]

        if contratos_encontrados:
            contratos_dados = []
            for contrato in contratos_encontrados:
                contratos_dados.append({
                    'numero': contrato.numero,
                    'artista': contrato.artista,
                    'gravadora': contrato.gravadora.nome,
                    'data_inicio': contrato.data_inicio,
                    'data_fim': contrato.data_fim
                })
            self.__tela_contrato.mostrar_contratos(contratos_dados)
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado para a gravadora {gravadora_nome}.")

    def buscar_contrato_pelo_numero(self):
        """Busca um contrato pelo número e exibe suas informações."""
        numero = self.__tela_contrato.buscar_por_numero()
        contrato = self.pegar_contrato_pelo_numero(numero)

        if contrato:
            contrato_dado = {
                'numero': contrato.numero,
                'artista': contrato.artista,
                'gravadora': contrato.gravadora.nome,
                'data_inicio': contrato.data_inicio,
                'data_fim': contrato.data_fim
            }
            self.__tela_contrato.mostrar_contratos([contrato_dado])
        else:
            self.__tela_contrato.mostrar_mensagem(f"Nenhum contrato encontrado com o número {numero}.")

    def retornar(self):
        """Retorna ao controlador de gravadora."""
        self.__controlador_gravadora.abre_tela()

    def abre_tela(self):
        """Abre a tela do controlador de contrato."""
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
