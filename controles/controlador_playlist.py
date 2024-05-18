from telas.tela_playlist import TelaPlaylist
from entidades.playlist import Playlist


class ControladorPlaylist:
    def __init__(self, controlador_artista) -> None:
        self.__playlists = []
        self.__tela_playlist = TelaPlaylist()
        self.__controlador_artista = controlador_artista

    def pegar_playlist_pelo_nome(self, nome: str):
        for playlist in self.__playlists:
            if playlist.nome == nome:
                return playlist
        return None

    def listar_playlists(self):
        for playlist in self.__playlists:
            self.__tela_playlist.mostrar_playlist({
                'nome': playlist.nome,
                'descricao': playlist.descricao
            })

    def cadastrar_playlist(self):
        dados_playlist = self.__tela_playlist.pegar_dados_playlist()
        playlist = Playlist(
            dados_playlist['nome'],
            dados_playlist['descricao']
        )
        self.__playlists.append(playlist)

    def editar_playlist(self):
        self.listar_playlists()
        nome_playlist = self.__tela_playlist.pegar_dados_playlist()
        playlist = self.pegar_playlist_pelo_nome(nome_playlist)

        if playlist is not None:
            novos_dados_playlist = self.__tela_playlist.pegar_dados_playlist()
            playlist.nome = novos_dados_playlist['nome'],
            playlist.descricao = novos_dados_playlist['descricao']
            self.listar_playlists()
        else:
            self.__tela_playlist.mostrar_mensagem('ATENÇÃO: Playlist não existente')

    def remover_playlist(self):
        self.listar_playlists()
        nome_playlist = self.__tela_playlist.pegar_dados_playlist()
        playlist = self.pegar_playlist_pelo_nome(nome_playlist)

        if playlist is not None:
            self.__playlists.remove(playlist)
            self.listar_playlists()
        else:
            self.__tela_playlist.mostrar_mensagem('ATENÇÃO: Playlist não existente')

    def retornar(self):
        self.__controlador_artista.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_playlist,
            2: self.editar_playlist,
            3: self.listar_playlists,
            4: self.remover_playlist,
            0: self.retornar
        }

        rodando = True
        while rodando:
            opcao = self.__tela_playlist.imprimir_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_playlist.mostrar_mensagem('Opção Inválida!')