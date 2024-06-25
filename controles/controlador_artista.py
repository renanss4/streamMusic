from telas.tela_artista import TelaArtista
from entidades.artista import Artista
from controles.controlador_musica import ControladorMusica
from controles.controlador_album import ControladorAlbum
from controles.controlador_playlist import ControladorPlaylist
from daos.artista_dao import ArtistaDAO

class ControladorArtista:

    def __init__(self, controlador_sistema) -> None:
        self.__artista_dao = ArtistaDAO()
        self.__tela_artista = TelaArtista()
        self.__controlador_musicas = ControladorMusica(self)
        self.__controlador_albuns = ControladorAlbum(self)
        self.__controlador_playlists = ControladorPlaylist(self)
        # self.__controlador_contratos = ControladorContrato(self)
        self.__controlador_sistema = controlador_sistema

    def pegar_artista_pelo_nome(self, nome: str):
        """Retorna um artista com o nome especificado ou None se não for encontrado."""
        return self.__artista_dao.get(nome)

    def listar_artistas(self):
        """Exibe a lista de artistas cadastrados ou uma mensagem informando que não há artistas."""
        artistas = self.__artista_dao.get_all()
        if artistas:
            artistas_dados = [{'nome': artista.nome,
                               'email': artista.email,
                               'telefone': artista.telefone,
                               'data_nascimento': artista.data_nascimento}
                              for artista in artistas]
            self.__tela_artista.mostrar_artistas(artistas_dados)
        else:
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")

    def cadastrar_artista(self):
        """Cadastra um novo artista após verificar se o artista já existe."""
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
            self.__artista_dao.add(artista)
            self.__tela_artista.mostrar_mensagem("Artista cadastrado com sucesso!")

    def editar_artista(self):
        """Edita um artista existente com novos dados fornecidos pelo usuário."""
        if not self.__artista_dao.get_all():
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        self.listar_artistas()
        nome_artista = self.__tela_artista.buscar_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if artista is not None:
            novos_dados_artista = self.__tela_artista.pegar_dados_artista()

            # Remover o artista antigo do DAO antes de atualizar
            self.__artista_dao.remove(artista.nome)
            
            # Atualizar os dados do artista
            artista.nome = novos_dados_artista['nome']
            artista.email = novos_dados_artista['email']
            artista.telefone = novos_dados_artista['telefone']
            artista.data_nascimento = novos_dados_artista['data_nascimento']
            
            # Adicionar o artista atualizado ao DAO
            self.__artista_dao.add(artista)
            
            self.__tela_artista.mostrar_mensagem("Artista editado com sucesso!")
        else:
            self.__tela_artista.mostrar_mensagem('ATENÇÃO: Artista não existente')

    def remover_artista(self):
        """Remove um artista da lista de artistas cadastrados."""
        if not self.__artista_dao.get_all():
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        self.listar_artistas()
        nome_artista = self.__tela_artista.buscar_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if artista is not None:
            self.__artista_dao.remove(nome_artista)
            self.__tela_artista.mostrar_mensagem("Artista removido com sucesso!")
        else:
            self.__tela_artista.mostrar_mensagem("ATENÇÃO: Artista não existente")

    def seguir_artista(self):
        """Permite que um artista siga outro artista."""
        self.__tela_artista.mostrar_mensagem("Seguir Artista")
        if not self.__artista_dao.get_all():
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        nome_artista = self.__tela_artista.pegar_nome_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if artista:
            nome_artista_seguir = self.__tela_artista.pegar_nome_artista()
            artista_seguir = self.pegar_artista_pelo_nome(nome_artista_seguir)

            if artista_seguir:
                artista.artistas_seguidos.append(artista_seguir)
                self.__artista_dao.update(artista)
                self.__tela_artista.mostrar_mensagem(f"Você seguiu o artista {artista_seguir.nome}!")
            else:
                self.__tela_artista.mostrar_mensagem("Artista não encontrado!")
        else:
            self.__tela_artista.mostrar_mensagem("Artista não encontrado!")

    def deixar_de_seguir_artista(self):
        """Permite que um artista deixe de seguir outro artista."""
        self.__tela_artista.mostrar_mensagem("Deixar de Seguir Artista")
        if not self.__artista_dao.get_all():
            self.__tela_artista.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        nome_artista = self.__tela_artista.pegar_nome_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if artista:
            nome_artista_deixar = self.__tela_artista.pegar_nome_artista()
            artista_deixar = self.pegar_artista_pelo_nome(nome_artista_deixar)

            if artista_deixar:
                if artista_deixar in artista.artistas_seguidos:
                    artista.artistas_seguidos.remove(artista_deixar)
                    self.__artista_dao.update(artista)
                    self.__tela_artista.mostrar_mensagem(f"Você deixou de seguir o artista {artista_deixar.nome}!")
                else:
                    self.__tela_artista.mostrar_mensagem("Você não segue esse artista!")
            else:
                self.__tela_artista.mostrar_mensagem("Artista não encontrado!")
        else:
            self.__tela_artista.mostrar_mensagem("Artista não encontrado!")

    def ver_artistas_seguidos(self):
        """Exibe a lista de artistas seguidos por um artista específico."""
        self.__tela_artista.mostrar_mensagem("Artistas Seguidos")
        nome_artista = self.__tela_artista.pegar_nome_artista()
        artista = self.pegar_artista_pelo_nome(nome_artista)

        if artista:
            artistas_dados = [{'nome': artista_seguido.nome, 'email': artista_seguido.email, 'telefone': artista_seguido.telefone,
                               'data_nascimento': artista_seguido.data_nascimento} for artista_seguido in artista.artistas_seguidos]
            if artistas_dados:
                self.__tela_artista.mostrar_artistas(artistas_dados)
            else:
                self.__tela_artista.mostrar_mensagem("Esse artista não segue nenhum outro artista.")
        else:
            self.__tela_artista.mostrar_mensagem("Artista não encontrado!")

    def abrir_musicas(self):
        """Abre a tela do controlador de músicas."""
        self.__controlador_musicas.abre_tela()

    def abrir_albuns(self):
        """Abre a tela do controlador de álbuns."""
        self.__controlador_albuns.abre_tela()

    def abrir_playlists(self):
        """Abre a tela do controlador de playlists."""
        self.__controlador_playlists.abre_tela()

    def retornar(self):
        """Retorna para a tela do controlador de sistema."""
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        """Exibe o menu de opções para manipulação dos artistas e executa as ações correspondentes."""
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
                self.seguir_artista()
            elif opcao == 9:
                self.deixar_de_seguir_artista()
            elif opcao == 10:
                self.ver_artistas_seguidos()
            else:
                self.__tela_artista.mostrar_mensagem('Opção Inválida!')
