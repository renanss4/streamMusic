from telas.tela_album import TelaAlbum
from entidades.album import Album
from daos.album_dao import AlbumDAO

class ControladorAlbum:
    def __init__(self, controlador_artista) -> None:
        """Inicializa o controlador de álbuns com uma lista de álbuns, 
        uma instância de TelaAlbum e um controlador de artistas.
        """
        self.__album_dao = AlbumDAO()
        self.__tela_album = TelaAlbum()
        self.__controlador_artista = controlador_artista

    def pegar_album_pelo_nome(self, nome: str):
        """Retorna um álbum com o nome especificado ou None se não for encontrado."""
        return self.__album_dao.get(nome)

    def listar_albuns(self):
        """Exibe a lista de álbuns cadastrados ou uma mensagem informando que não há álbuns."""
        albuns = self.__album_dao.get_all()
        if albuns:
            albuns_dados = [{'nome': album.nome, 'descricao': album.descricao} for album in albuns]
            self.__tela_album.mostrar_albuns(albuns_dados)
        else:
            self.__tela_album.mostrar_mensagem("Nenhum álbum cadastrado.")

    def cadastrar_album(self):
        """Cadastra um novo álbum após verificar se o álbum já existe."""
        dados_album = self.__tela_album.pegar_dados_album()
        if self.pegar_album_pelo_nome(dados_album['nome']):
            self.__tela_album.mostrar_mensagem("Álbum já existente!")
        else:
            album = Album(dados_album['nome'], dados_album['descricao'])
            self.__album_dao.add(album)
            self.__tela_album.mostrar_mensagem("Álbum cadastrado com sucesso!")

    def editar_album(self):
        """Edita um álbum existente com novos dados fornecidos pelo usuário."""
        if not self.__album_dao.get_all():
            self.__tela_album.mostrar_mensagem("Nenhum álbum cadastrado.")
            return

        self.listar_albuns()
        nome_album = self.__tela_album.buscar_album()
        album = self.pegar_album_pelo_nome(nome_album)

        if album is not None:
            novos_dados_album = self.__tela_album.pegar_dados_album()

            # Remover o álbum antigo do DAO antes de atualizar
            self.__album_dao.remove(album.nome)
            
            # Atualizar os dados do álbum
            album.nome = novos_dados_album['nome']
            album.descricao = novos_dados_album['descricao']
            
            # Adicionar o álbum atualizado ao DAO
            self.__album_dao.add(album)
            
            self.__tela_album.mostrar_mensagem("Álbum editado com sucesso!")
        else:
            self.__tela_album.mostrar_mensagem('ATENÇÃO: Álbum não existente')

    def remover_album(self):
        """Remove um álbum da lista de álbuns cadastrados."""
        if not self.__album_dao.get_all():
            self.__tela_album.mostrar_mensagem("Nenhum álbum cadastrado.")
            return

        self.listar_albuns()
        nome_album = self.__tela_album.buscar_album()
        album = self.pegar_album_pelo_nome(nome_album)

        if album is not None:
            self.__album_dao.remove(nome_album)
            self.__tela_album.mostrar_mensagem("Álbum removido com sucesso!")
        else:
            self.__tela_album.mostrar_mensagem('ATENÇÃO: Álbum não existente')

    def retornar(self):
        """Retorna para a tela do controlador de artistas."""
        self.__controlador_artista.abre_tela()

    def abre_tela(self):
        """Exibe o menu de opções para manipulação dos álbuns e executa as ações correspondentes."""
        while True:
            opcao = self.__tela_album.imprimir_opcoes()
            if opcao == 0:
                self.retornar()
                break
            elif opcao == 1:
                self.cadastrar_album()
            elif opcao == 2:
                self.listar_albuns()
            elif opcao == 3:
                self.editar_album()
            elif opcao == 4:
                self.remover_album()
            else:
                self.__tela_album.mostrar_mensagem('Opção Inválida!')
