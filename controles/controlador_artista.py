from telas.tela_artista import TelaArtista
from entidades.artista import Artista
from controles.controlador_musica import ControladorMusica
from controles.controlador_album import ControladorAlbum


class ControladorArtista:

    def __init__(self, controlador_sistema) -> None:
        self.__artistas = []
        self.__tela_artista = TelaArtista()
        self.__controlador_musicas = ControladorMusica(self)
        self.__controlador_albuns = ControladorAlbum(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def controlador_musica(self):
        return self.__controlador_musicas
    
    @property
    def controlador_album(self):
        return self.__controlador_albuns

    def pegar_artista_pelo_username(self, username: str):
        for artista in self.__artistas:
            if artista.username == username:
                return artista
        return None
    
    def listar_artistas(self):
        for artista in self.__artistas:
            self.__tela_artista.mostrar_artista({
                "nome": artista.nome,
                "username": artista.username,
                "email": artista.email,
                "telefone": artista.telefone
            })

    def cadastrar_artista(self):
        dados_artista = self.__tela_artista.pegar_dados_artista()
        artista = Artista(
            dados_artista["nome"],
            dados_artista["username"],
            dados_artista["email"],
            dados_artista["telefone"]
        )
        self.__artistas.append(artista)

    def editar_artista(self):
        self.listar_artistas()
        username_artista = self.__tela_artista.pegar_dados_artista()
        artista = self.pegar_artista_pelo_username(username_artista)

        if (artista is not None):
            novos_dados_artista = self.__tela_artista.pegar_dados_artista()
            artista.nome = novos_dados_artista["nome"],
            artista.username = novos_dados_artista["username"],
            artista.email = novos_dados_artista["email"],
            artista.telefone = novos_dados_artista["telefone"]
            self.listar_artistas()
        else:
            self.__tela_artista.mostrar_mensagem('ATENÇÃO: Artista não existente')

    def remover_artista(self):
        self.listar_artistas()
        username_artista = self.__tela_artista.buscar_artista()
        artista = self.pegar_artista_pelo_username(username_artista)

        if(artista is not None):
            self.__artistas.remove(artista)
            self.listar_artistas()
        else:
            self.__tela_artista.mostrar_mensagem("ATENÇÃO: Artista não existente")

    def abrir_musicas(self):
        self.__controlador_musicas.abre_tela()

    def abrir_albuns(self):
        self.__controlador_albuns.abre_tela()

    def cadastrar_albuns(self):
        self.__controlador_albuns.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_artista,
            2: self.editar_artista,
            3: self.listar_artistas,
            4: self.remover_artista,
            5: self.abrir_musicas,
            # 6: self.abrir_albuns,
            0: self.retornar
        }

        rodando = True
        while rodando:
            opcao = self.__tela_artista.imprimir_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_artista.mostrar_mensagem('Opção Inválida!')