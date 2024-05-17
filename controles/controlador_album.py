from telas.tela_album import TelaAlbum
from entidades.album import Album


class ControladorAlbum:
    def __init__(self, controlador_artista) -> None:
        self.__albuns = []
        self.__tela_album = TelaAlbum
        self.__controlador_artista = controlador_artista

    def pegar_album_pelo_nome(self, nome: str):
        for album in self.__albuns:
            if album.nome == nome:
                return album
        return None

    def listar_albuns(self):
        for album in self.__albuns:
            self.__tela_album.mostrar_album({
                'nome': album.nome,
                'descricao': album.descricao
            })

    def cadastrar_album(self):
        dados_album = self.__tela_album.pegar_dados_album()
        album = Album(
            dados_album['nome'],
            dados_album['descricao']
        )
        self.__albuns.append(album)

    def editar_album(self):
        self.listar_albuns()
        nome_album = self.__tela_album.pegar_dados_album()
        album = self.pegar_album_pelo_nome(nome_album)

        if album is not None:
            novos_dados_album = self.__tela_album.pegar_dados_album()
            album.nome = novos_dados_album['nome'],
            album.letra = novos_dados_album['descricao']
            self.listar_albuns()
        else:
            self.__tela_album.mostrar_mensagem('ATENÇÃO: Álbum não existente')

    def remover_album(self):
        self.listar_albuns()
        nome_album = self.__tela_album.pegar_dados_album()
        album = self.pegar_album_pelo_nome(nome_album)

        if album is not None:
            self.__albuns.remove(album)
            self.listar_albuns()
        else:
            self.__tela_album.mostrar_mensagem('ATENÇÃO: Álbum não existente')

    def retornar(self):
        self.__controlador_artista.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_album,
            2: self.editar_album,
            3: self.listar_albuns,
            4: self.remover_album,
            0: self.retornar
        }

        rodando = True
        while rodando:
            opcao = self.__tela_album.imprimir_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_album.mostrar_mensagem('Opção Inválida!')