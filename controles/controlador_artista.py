from telas.tela_artista import TelaArtista
from entidades.artista import Artista
from entidades.musica import Musica  # Adicionando esta linha para importar a classe Musica
from controles.controlador_musica import ControladorMusica
from controles.controlador_album import ControladorAlbum
from controles.controlador_playlist import ControladorPlaylist
# from controles.controlador_contrato import ControladorContrato

class ControladorArtista:

    def __init__(self, controlador_sistema) -> None:
        self.__artistas = []
        self.__tela_artista = TelaArtista()
        self.__controlador_musicas = ControladorMusica(self)
        self.__controlador_albuns = ControladorAlbum(self)
        self.__controlador_playlists = ControladorPlaylist(self)
        # self.__controlador_contratos = ControladorContrato(self)
        self.__controlador_sistema = controlador_sistema

    @property
    def artistas(self):
        return self.__artistas

    # Métodos de música
    def cadastrar_musica(self):
        nome_artista = self.__tela_artista.pegar_nome_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if not artista:
            self.__tela_artista.mostrar_mensagem("Artista não encontrado!")
            return

        dados_musica = self.__controlador_musicas.pegar_dados_musica()
        musica_existente = self.__controlador_musicas.pegar_musica_pelo_nome(dados_musica['nome'])

        if musica_existente:
            self.__tela_artista.mostrar_mensagem("Música já existente!")
            return

        musica = Musica(dados_musica['nome'], dados_musica['letra'], artista)
        artista.musicas.append(musica)
        self.__controlador_musicas.adicionar_musica(musica)
        self.__controlador_musicas.mostrar_mensagem("Música cadastrada com sucesso!")



    def ver_musicas_do_artista(self):
        nome_artista = self.__tela_artista.pegar_nome_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if not artista:
            self.__tela_artista.mostrar_mensagem("Artista não encontrado!")
            return

        musicas_do_artista = self.__controlador_musicas.pegar_musicas_por_artista(artista)
        if musicas_do_artista:
            musicas_dados = [{'nome': musica.nome, 'letra': musica.letra} for musica in musicas_do_artista]
            self.__controlador_musicas.mostrar_musicas(musicas_dados)
        else:
            self.__tela_artista.mostrar_mensagem("Nenhuma música encontrada para este artista.")

    # Outros métodos de seguir, deixar de seguir, listar etc., permanecem os mesmos

    def pegar_artista_pelo_nome(self, nome: str):
        for artista in self.__artistas:
            if artista.nome == nome:
                return artista
        return None

    def listar_artistas(self):
        if self.__artistas:
            artistas_dados = [{'nome': artista.nome,
                               'email': artista.email,
                               'telefone': artista.telefone,
                               'data_nascimento': artista.data_nascimento}
                              for artista in self.__artistas]
            self.__tela_artista.mostrar_artistas(artistas_dados)
        else:
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")

    # Métodos de cadastro, edição e remoção de artistas
    def cadastrar_artista(self):
        dados_artista = self.__tela_artista.pegar_dados_artista()
        if self.pegar_artista_pelo_nome(dados_artista['nome']):
            self.__tela_artista.mostrar_mensagem("Artista já cadastrado!")
        else:
            artista = Artista(
                dados_artista['nome'],
                dados_artista['email'],
                dados_artista['telefone'],
                dados_artista['data_nascimento']
            )
            self.__artistas.append(artista)
            self.__tela_artista.mostrar_mensagem("Artista cadastrado com sucesso!")

    def editar_artista(self):
        if not self.__artistas:
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        self.listar_artistas()
        nome_artista = self.__tela_artista.buscar_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if artista is not None:
            novos_dados_artista = self.__tela_artista.pegar_dados_artista()
            artista.nome = novos_dados_artista['nome']
            artista.email = novos_dados_artista['email']
            artista.telefone = novos_dados_artista['telefone']
            artista.data_nascimento = novos_dados_artista['data_nascimento']
            self.__tela_artista.mostrar_mensagem("Artista editado com sucesso!")
        else:
            self.__tela_artista.mostrar_mensagem('ATENÇÃO: Artista não existente')

    def remover_artista(self):
        if not self.__artistas:
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        self.listar_artistas()
        nome_artista = self.__tela_artista.buscar_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if artista is not None:
            self.__artistas.remove(artista)
            self.__tela_artista.mostrar_mensagem("Artista removido com sucesso!")
        else:
            self.__tela_artista.mostrar_mensagem('ATENÇÃO: Artista não existente')

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
                self.cadastrar_musica()
            elif opcao == 6:
                self.ver_musicas_do_artista()
            else:
                self.__tela_artista.mostrar_mensagem('Opção Inválida!')
