from telas.tela_playlist import TelaPlaylist
from entidades.playlist import Playlist


class ControladorPlaylist:
    """Controlador para gerenciar operações relacionadas a playlists."""

    def __init__(self, controlador_artista) -> None:
        """Inicializa o controlador de playlists."""
        self.__playlists = []
        self.__tela_playlist = TelaPlaylist()
        self.__controlador_artista = controlador_artista

    def pegar_playlist_pelo_nome(self, nome: str):
        """Retorna a playlist correspondente ao nome fornecido."""
        for playlist in self.__playlists:
            if playlist.nome == nome:
                return playlist
        return None

    def listar_playlists(self):
        """Lista todas as playlists cadastradas."""
        if self.__playlists:
            playlists_dados = [{'nome': playlist.nome, 'descricao': playlist.descricao} for playlist in self.__playlists]
            self.__tela_playlist.mostrar_playlists(playlists_dados)
        else:
            self.__tela_playlist.mostrar_mensagem("Nenhuma playlist cadastrada.")

    def cadastrar_playlist(self):
        """Realiza o cadastro de uma nova playlist."""
        dados_playlist = self.__tela_playlist.pegar_dados_playlist()
        playlist = Playlist(
            dados_playlist['nome'],
            dados_playlist['descricao']
        )
        if self.pegar_playlist_pelo_nome(dados_playlist['nome']):
            self.__tela_playlist.mostrar_mensagem("Playlist já existente!")
        else:
            self.__playlists.append(playlist)
            self.__tela_playlist.mostrar_mensagem("Playlist cadastrada com sucesso!")

    def editar_playlist(self):
        """Permite a edição dos dados de uma playlist."""
        if not self.__playlists:
            self.__tela_playlist.mostrar_mensagem("Nenhuma playlist cadastrada.")
            return

        self.listar_playlists()
        nome_playlist = input("Digite o nome da playlist que deseja editar: ")
        playlist = self.pegar_playlist_pelo_nome(nome_playlist)

        if playlist is not None:
            novos_dados_playlist = self.__tela_playlist.pegar_dados_playlist()
            playlist.nome = novos_dados_playlist['nome']
            playlist.descricao = novos_dados_playlist['descricao']
            self.__tela_playlist.mostrar_mensagem("Playlist editada com sucesso!")
        else:
            self.__tela_playlist.mostrar_mensagem('ATENÇÃO: Playlist não existente')

    def remover_playlist(self):
        """Remove uma playlist."""
        if not self.__playlists:
            self.__tela_playlist.mostrar_mensagem("Nenhuma playlist cadastrada.")
            return

        self.listar_playlists()
        nome_playlist = input("Digite o nome da playlist que deseja remover: ")
        playlist = self.pegar_playlist_pelo_nome(nome_playlist)

        if playlist is not None:
            self.__playlists.remove(playlist)
            self.__tela_playlist.mostrar_mensagem("Playlist removida com sucesso!")
        else:
            self.__tela_playlist.mostrar_mensagem("ATENÇÃO: Playlist não existente")

    def retornar(self):
        """Retorna ao controlador de artista."""
        self.__controlador_artista.abre_tela()

    def abre_tela(self):
        """Abre a tela do controlador de playlist."""
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
