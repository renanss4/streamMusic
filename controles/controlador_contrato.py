from telas.tela_contrato import TelaContrato
from entidades.contrato import Contrato

class ControladorContrato:
    def __init__(self):
        self.__contratos = {}
        self.__tela_contrato = TelaContrato()

    def adicionar_contrato(self, contrato, gravadora):
        dados_contrato = self.__tela_contrato.pegar_dados_contrato()
        artista = dados_contrato["artista"]
        gravadora = dados_contrato["gravadora"]
        contrato = Contrato(artista, gravadora)
        contrato.gravadora = gravadora
        self.__contratos[contrato.artista.nome] = contrato
        self.__tela_contrato.mostra_mensagem(f"Contrato adicionado com sucesso para o artista {contrato.artista.nome}.")

    def buscar_contrato(self, nome_artista):
        contrato = self.__contratos.get(nome_artista, None)
        if contrato:
            self.__tela_contrato.mostra_contrato(contrato)
        else:
            self.__tela_contrato.mostra_mensagem(f"Não foi encontrado nenhum contrato para o artista {nome_artista}.")

    def listar_contratos_por_gravadora(self, nome_gravadora):
        contratos = [contrato for contrato in self.__contratos.values() if contrato.gravadora.nome == nome_gravadora]
        self.__tela_contrato.mostra_contrato(contratos)

    def remover_contrato(self, nome_artista):
        if nome_artista in self.__contratos:
            del self.__contratos[nome_artista]
            self.__tela_contrato.mostra_mensagem(f"Contrato removido com sucesso para o artista {nome_artista}.")
        else:
            self.__tela_contrato.mostra_mensagem(f"Não foi encontrado nenhum contrato para o artista {nome_artista}.")
