from telas.tela_artista import TelaArtista
from entidades.artista import Artista
from controles.controlador_musica import ControladorMusica
from controles.controlador_album import ControladorAlbum
from controles.controlador_playlist import ControladorPlaylist
from controles.controlador_contrato import ControladorContrato

class ControladorArtista:

    def __init__(self, controlador_sistema) -> None:
        self.__artistas = []
        self.__tela_artista = TelaArtista()
        self.__controlador_musicas = ControladorMusica(self)
        self.__controlador_albuns = ControladorAlbum(self)
        self.__controlador_playlists = ControladorPlaylist(self)
        self.__controlador_contratos = ControladorContrato(self)
        self.__controlador_sistema = controlador_sistema

    # Métodos auxiliares de busca e listagem de artistas
    def pegar_artista_pelo_username(self, username: str):
        for artista in self.__artistas:
            if artista.username == username:
                return artista
        return None

    def listar_artistas(self):
        if self.__artistas:
            artistas_dados = [{'nome': artista.nome, 'username': artista.username,
                               'email': artista.email, 'telefone': artista.telefone}
                              for artista in self.__artistas]
            self.__tela_artista.mostrar_artistas(artistas_dados)
        else:
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")

    # Métodos de cadastro, edição e remoção de artistas
    def cadastrar_artista(self):
        dados_artista = self.__tela_artista.pegar_dados_artista()
        if self.pegar_artista_pelo_username(dados_artista['username']):
            self.__tela_artista.mostrar_mensagem("Artista já cadastrado!")
        else:
            artista = Artista(
                dados_artista['nome'],
                dados_artista['username'],
                dados_artista['email'],
                dados_artista['telefone']
            )
            self.__artistas.append(artista)
            self.__tela_artista.mostrar_mensagem("Artista cadastrado com sucesso!")

    def editar_artista(self):
        if not self.__artistas:
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        self.listar_artistas()
        username_artista = self.__tela_artista.buscar_artista()
        artista = self.pegar_artista_pelo_username(username_artista)

        if artista is not None:
            novos_dados_artista = self.__tela_artista.pegar_dados_artista()
            artista.nome = novos_dados_artista['nome']
            artista.username = novos_dados_artista['username']
            artista.email = novos_dados_artista['email']
            artista.telefone = novos_dados_artista['telefone']
            self.__tela_artista.mostrar_mensagem("Artista editado com sucesso!")
        else:
            self.__tela_artista.mostrar_mensagem('ATENÇÃO: Artista não existente')

    def remover_artista(self):
        if not self.__artistas:
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        self.listar_artistas()
        username_artista = self.__tela_artista.buscar_artista()
        artista = self.pegar_artista_pelo_username(username_artista)

        if artista is not None:
            self.__artistas.remove(artista)
            self.__tela_artista.mostrar_mensagem("Artista removido com sucesso!")
        else:
            self.__tela_artista.mostrar_mensagem("ATENÇÃO: Artista não existente")

    # Métodos para abrir as telas de músicas, álbuns e playlists
    def abrir_musicas(self):
        self.__controlador_musicas.abre_tela()

    def abrir_albuns(self):
        self.__controlador_albuns.abre_tela()

    def abrir_playlists(self):
        self.__controlador_playlists.abre_tela()

    def abrir_contratos(self):
        self.__controlador_contratos.abre_tela()

    # Métodos de retorno e abertura da tela principal do controlador de artista
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        while True:
            opcao = self.__tela_artista.imprimir_opcoes()
            if opcao == 0:
                self.retornar()
                break
            elif opcao == 1:
                self.cadastrar_artista()
            elif opcao == 2:
                self.listar_artistas()
            elif opcao == 3:
                self.editar_artista()
            elif opcao == 4:
                self.remover_artista()
            elif opcao == 5:
                self.abrir_musicas()
            elif opcao == 6:
                self.abrir_albuns()
            elif opcao == 7:
                self.abrir_playlists()
            elif opcao == 8:
                self.abrir_contratos()
            else:
                self.__tela_artista.mostrar_mensagem('Opção Inválida!')
