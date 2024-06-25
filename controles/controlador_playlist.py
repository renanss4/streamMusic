from telas.tela_playlist import TelaPlaylist
from entidades.playlist import Playlist
from daos.playlist_dao import PlaylistDAO

class ControladorPlaylist:
    """Controlador para gerenciar operações relacionadas a playlists."""

    def __init__(self, controlador_sistema) -> None:
        """Inicializa o controlador de playlists."""
        self.__playlist_dao = PlaylistDAO()
        self.__tela_playlist = TelaPlaylist()
        self.__controlador_sistema = controlador_sistema

    def pegar_playlist_pelo_nome(self, nome: str):
        """Retorna a playlist correspondente ao nome fornecido."""
        return self.__playlist_dao.get(nome)

    def listar_playlists(self):
        """Lista todas as playlists cadastradas."""
        playlists = self.__playlist_dao.get_all()
        if playlists:
            playlists_dados = [{'nome': playlist.nome, 'descricao': playlist.descricao} for playlist in playlists]
            self.__tela_playlist.mostrar_playlists(playlists_dados)
        else:
            self.__tela_playlist.mostrar_mensagem("Nenhuma playlist cadastrada.")

    def cadastrar_playlist(self):
        """Realiza o cadastro de uma nova playlist."""
        dados_playlist = self.__tela_playlist.pegar_dados_playlist()
        if self.pegar_playlist_pelo_nome(dados_playlist['nome']):
            self.__tela_playlist.mostrar_mensagem("Playlist já existente!")
        else:
            playlist = Playlist(
                dados_playlist['nome'],
                dados_playlist['descricao']
            )
            self.__playlist_dao.add(playlist)
            self.__tela_playlist.mostrar_mensagem("Playlist cadastrada com sucesso!")

    def editar_playlist(self):
        """Permite a edição dos dados de uma playlist."""
        if not self.__playlist_dao.get_all():
            self.__tela_playlist.mostrar_mensagem("Nenhuma playlist cadastrada.")
            return

        self.listar_playlists()
        nome_playlist = self.__tela_playlist.buscar_playlist()
        playlist = self.pegar_playlist_pelo_nome(nome_playlist)

        if playlist is not None:
            novos_dados_playlist = self.__tela_playlist.pegar_dados_playlist()

            # Remover a playlist antiga e adicionar a nova
            self.__playlist_dao.remove(playlist.nome)

            playlist.nome = novos_dados_playlist['nome']
            playlist.descricao = novos_dados_playlist['descricao']

            self.__playlist_dao.add(playlist)
            self.__tela_playlist.mostrar_mensagem("Playlist editada com sucesso!")
        else:
            self.__tela_playlist.mostrar_mensagem('ATENÇÃO: Playlist não existente')

    def remover_playlist(self):
        """Remove uma playlist."""
        if not self.__playlist_dao.get_all():
            self.__tela_playlist.mostrar_mensagem("Nenhuma playlist cadastrada.")
            return

        self.listar_playlists()
        nome_playlist = self.__tela_playlist.buscar_playlist()
        playlist = self.pegar_playlist_pelo_nome(nome_playlist)

        if playlist is not None:
            self.__playlist_dao.remove(nome_playlist)
            self.__tela_playlist.mostrar_mensagem("Playlist removida com sucesso!")
        else:
            self.__tela_playlist.mostrar_mensagem("ATENÇÃO: Playlist não existente")

    def retornar(self):
        """Retorna ao controlador de sistema."""
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        """Abre a tela do controlador de playlists."""
        while True:
            opcao = self.__tela_playlist.imprimir_opcoes()
            if opcao == 0:
                self.retornar()
                break
            elif opcao == 1:
                self.cadastrar_playlist()
            elif opcao == 2:
                self.listar_playlists()
            elif opcao == 3:
                self.editar_playlist()
            elif opcao == 4:
                self.remover_playlist()
            else:
                self.__tela_playlist.mostrar_mensagem('Opção Inválida!')
