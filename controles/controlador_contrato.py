from telas.tela_contrato import TelaContrato
from entidades.contrato import Contrato

class ControladorContrato:
    def __init__(self):
        self.__contratos = []
        self.__tela_contrato = TelaContrato()

    def adicionar_contrato(self, contrato, gravadora):
        dados_contrato = self.__tela_contrato.pegar_dados_contrato()
        artista = dados_contrato["artista"]
        gravadora = dados_contrato["gravadora"]
        contrato = Contrato(artista, gravadora)
        contrato.gravadora = gravadora
        self.__contratos.append(contrato)
        self.__tela_contrato.mostra_mensagem(f"Contrato adicionado com sucesso para o artista {contrato.artista.nome}.")

    def buscar_contrato(self, nome_artista):
        for contrato in self.__contratos:
            if contrato.artista.nome == nome_artista:
                self.__tela_contrato.mostra_contrato(contrato)
                return
        self.__tela_contrato.mostra_mensagem(f"Não foi encontrado nenhum contrato para o artista {nome_artista}.")

    def listar_contratos(self, nome_gravadora):
        contratos = [contrato for contrato in self.__contratos if contrato.gravadora.nome == nome_gravadora]
        self.__tela_contrato.mostra_contrato(contratos)

    def editar_contrato(self, nome_artista):
        for contrato in self.__contratos:
            if contrato.artista.nome == nome_artista:
                novos_dados_contrato = self.__tela_contrato.editar_contrato()
                novo_artista = novos_dados_contrato.get("artista")
                nova_gravadora = novos_dados_contrato.get("gravadora")
                if novo_artista:
                    contrato.artista = novo_artista
                if nova_gravadora:
                    contrato.gravadora = nova_gravadora
                self.__tela_contrato.mostrar_mensagem(f"Contrato atualizado com sucesso para o artista {contrato.artista.nome}.")
                return
        self.__tela_contrato.mostrar_mensagem(f"Não foi encontrado nenhum contrato para o artista {nome_artista}.")

    def remover_contrato(self, nome_artista):
        for contrato in self.__contratos:
            if contrato.artista.nome == nome_artista:
                self.__contratos.remove(contrato)
                self.__tela_contrato.mostra_mensagem(f"Contrato removido com sucesso para o artista {nome_artista}.")
                return
        self.__tela_contrato.mostra_mensagem(f"Não foi encontrado nenhum contrato para o artista {nome_artista}.")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_contrato,
            2: self.editar_contrato,
            3: self.listar_contratos,
            4: self.remover_contrato,
            0: self.retornar
        }

        rodando = True
        while rodando:
            lista_opcoes[self.__tela_contrato.imprimir_opcoes()]()
