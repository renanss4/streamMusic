from telas.tela_musica import TelaMusica
from entidades.musica import Musica

class ControladorMusica:
    def __init__(self, controlador_artista, controlador_album, controlador_playlist) -> None:
        self.__musicas = []
        self.__tela_musica = TelaMusica()
        self.__controlador_artista = controlador_artista
        # self.__controlador_album = controlador_album
        # self.__controlador_playlist = controlador_playlist

    def pegar_musica_pelo_nome(self, nome: str):
        for musica in self.__musicas:
            if musica.nome == nome:
                return musica
        return None

    def listar_musicas(self):
        if self.__musicas:
            musicas_dados = [{'nome': musica.nome, 'letra': musica.letra} for musica in self.__musicas]
            self.__tela_musica.mostrar_musicas(musicas_dados)
        else:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")

    def cadastrar_musica(self):
        dados_musica = self.__tela_musica.pegar_dados_musica()
        if self.pegar_musica_pelo_nome(dados_musica['nome']):
            self.__tela_musica.mostrar_mensagem("Música já existente!")
        else:
            musica = Musica(dados_musica['nome'], dados_musica['letra'])
            self.__musicas.append(musica)
            self.__tela_musica.mostrar_mensagem("Música cadastrada com sucesso!")

    def editar_musica(self):
        if not self.__musicas:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")
            return

        self.listar_musicas()
        nome_musica = self.__tela_musica.buscar_musica()
        musica = self.pegar_musica_pelo_nome(nome_musica)

        if musica is not None:
            novos_dados_musica = self.__tela_musica.pegar_dados_musica()
            musica.nome = novos_dados_musica['nome']
            musica.letra = novos_dados_musica['letra']
            self.__tela_musica.mostrar_mensagem("Música editada com sucesso!")
        else:
            self.__tela_musica.mostrar_mensagem('ATENÇÃO: Música não existente')
    
    # def adicionar_musica(self, tipo, nome_musica, nome_album, nome_playlist):
    #     tipo_adicao = self.__tela_musica.pegar_dados_adicao_musica(tipo)
    #     if tipo_adicao == 1:
    #         musica = self.pegar_musica_pelo_nome(nome_musica)
    #         playlist = self.__controlador_playlist.pegar_playlist_pelo_nome(nome_playlist)
    #         if musica and playlist:
    #             playlist.adicionar_musica(musica)
    #             self.__tela_musica.mostrar_mensagem("Música adicionada à playlist com sucesso!")
    #         else:
    #             self.__tela_musica.mostrar_mensagem("Música ou playlist não existente!")
    #     elif tipo_adicao == 2:
    #         musica = self.pegar_musica_pelo_nome(nome_musica)
    #         album = self.__controlador_album.pegar_album_pelo_nome(nome_album)
    #         if musica and album:
    #             album.adicionar_musica(musica)
    #             self.__tela_musica.mostrar_mensagem("Música adicionada ao álbum com sucesso!")
    #         else:
    #             self.__tela_musica.mostrar_mensagem("Música ou álbum não existente!")
    
    # def remover_musica(self, tipo, nome_musica, nome_album, nome_playlist):
    #     musica = self.pegar_musica_pelo_nome(nome_musica)
    #     if tipo == 1:
    #         playlist = self.__controlador_playlist.pegar_playlist_pelo_nome(nome_playlist)
    #         if musica and playlist and playlist.remover_musica(musica):
    #             self.__tela_musica.mostrar_mensagem("Música removida da playlist com sucesso!")
    #         else:
    #             self.__tela_musica.mostrar_mensagem("Música ou playlist não existente!")
    #     elif tipo == 2:
    #         album = self.__controlador_album.pegar_album_pelo_nome(nome_album)
    #         if musica and album and album.remover_musica(musica):
    #             self.__tela_musica.mostrar_mensagem("Música removida do álbum com sucesso!")
    #         else:
    #             self.__tela_musica.mostrar_mensagem("Música ou álbum não existente!")

    def remover_musica(self):
        if not self.__musicas:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")
            return

        self.listar_musicas()
        nome_musica = self.__tela_musica.buscar_musica()
        musica = self.pegar_musica_pelo_nome(nome_musica)

        if musica is not None:
            self.__musicas.remove(musica)
            self.__tela_musica.mostrar_mensagem("Música removida com sucesso!")
        else:
            self.__tela_musica.mostrar_mensagem('ATENÇÃO: Música não existente')

    def retornar(self):
        self.__controlador_artista.abre_tela()

    def abre_tela(self):
        while True:
            opcao = self.__tela_musica.imprimir_opcoes()
            if opcao == 0:
                self.retornar()
                break
            elif opcao == 1:
                self.cadastrar_musica()
            elif opcao == 2:
                self.listar_musicas()
            elif opcao == 3:
                self.editar_musica()
            elif opcao == 4:
                self.adicionar_musica()
            elif opcao == 5:
                self.remover_musica()
            elif opcao == 6:
                self.remover_musica()
            else:
                self.__tela_musica.mostrar_mensagem('Opção Inválida!')