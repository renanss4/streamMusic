from telas.tela_musica import TelaMusica
from daos.musica_dao import MusicaDAO
from entidades.musica import Musica

class ControladorMusica:
    """Controlador para gerenciar operações relacionadas a músicas."""

    def __init__(self, controlador_artista) -> None:
        """Inicializa o controlador de música."""
        self.__musica_dao = MusicaDAO()  # Instância do DAO para manipular músicas
        self.__tela_musica = TelaMusica()
        self.__controlador_artista = controlador_artista

    def pegar_musica_pelo_nome(self, nome: str):
        """Retorna a música correspondente ao nome fornecido."""
        return self.__musica_dao.get(nome)

    def listar_musicas(self):
        """Lista todas as músicas cadastradas."""
        musicas = self.__musica_dao.get_all()
        if musicas:
            musicas_dados = [{'nome': musica.nome, 'letra': musica.letra} for musica in musicas]
            self.__tela_musica.mostrar_musicas(musicas_dados)
        else:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")

    def cadastrar_musica(self):
        """Realiza o cadastro de uma nova música."""
        dados_musica = self.__tela_musica.pegar_dados_musica()
        if self.pegar_musica_pelo_nome(dados_musica['nome']):
            self.__tela_musica.mostrar_mensagem("Música já existente!")
        else:
            musica = Musica(dados_musica['nome'], dados_musica['letra'])
            self.__musica_dao.add(musica)
            self.__tela_musica.mostrar_mensagem("Música cadastrada com sucesso!")

    def editar_musica(self):
        """Permite a edição dos dados de uma música."""
        musicas = self.__musica_dao.get_all()
        if not musicas:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")
            return

        self.listar_musicas()
        nome_musica = self.__tela_musica.buscar_musica()
        musica = self.pegar_musica_pelo_nome(nome_musica)

        if musica is not None:
            novos_dados_musica = self.__tela_musica.pegar_dados_musica()

            # Remover a música antiga e adicionar a nova
            self.__musica_dao.remove(musica.nome)

            musica.nome = novos_dados_musica['nome']
            musica.letra = novos_dados_musica['letra']

            self.__musica_dao.add(musica)
            self.__tela_musica.mostrar_mensagem("Música editada com sucesso!")
        else:
            self.__tela_musica.mostrar_mensagem('ATENÇÃO: Música não existente')

    def remover_musica(self):
        """Remove uma música."""
        musicas = self.__musica_dao.get_all()
        if not musicas:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")
            return

        self.listar_musicas()
        nome_musica = self.__tela_musica.buscar_musica()
        musica = self.pegar_musica_pelo_nome(nome_musica)

        if musica is not None:
            self.__musica_dao.remove(nome_musica)
            self.__tela_musica.mostrar_mensagem("Música removida com sucesso!")
        else:
            self.__tela_musica.mostrar_mensagem('ATENÇÃO: Música não existente')

    def retornar(self):
        """Retorna ao controlador de artista."""
        self.__controlador_artista.abre_tela()

    def abre_tela(self):
        """Abre a tela do controlador de música."""
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
                self.remover_musica()
            else:
                self.__tela_musica.mostrar_mensagem('Opção Inválida!')
