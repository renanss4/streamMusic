from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario
from controles.controlador_playlist import ControladorPlaylist
from daos.usuario_dao import UsuarioDAO



class ControladorUsuario:
    def __init__(self, controlador_sistema):
        """Inicializa o controlador de usuários com uma lista vazia de usuários,
        uma instância de TelaUsuario, um controlador de playlists e uma referência
        ao controlador do sistema.
        """
        self.__usuario_dao = UsuarioDAO()
        self.__tela_usuario = TelaUsuario()
        self.__controlador_playlists = ControladorPlaylist(self)
        self.__controlador_sistema = controlador_sistema

    def pegar_usuario_pelo_nome(self, nome: str):
        """Retorna o usuário com o nome especificado ou None se não for encontrado."""
        return self.__usuario_dao.get(nome)

    def listar_usuarios(self):
        """Lista os usuários cadastrados."""
        usuarios = self.__usuario_dao.get_all()
        if usuarios:
            usuarios_dados = [
                {
                    'nome': usuario.nome,
                    'email': usuario.email,
                    'telefone': usuario.telefone,
                    'data_nascimento': usuario.data_nascimento
                } for usuario in usuarios
            ]
            self.__tela_usuario.mostrar_usuarios(usuarios_dados)
        else:
            self.__tela_usuario.mostrar_mensagem("Nenhum usuário cadastrado.")

    def cadastrar_usuario(self):
        """Cadastra um novo usuário após verificar se o usuário já existe."""
        dados_usuario = self.__tela_usuario.pegar_dados_usuario()
        if self.pegar_usuario_pelo_nome(dados_usuario['nome']):
            self.__tela_usuario.mostrar_mensagem("Usuário já cadastrado!")
        else:
            usuario = Usuario(
                dados_usuario['nome'],
                dados_usuario['email'],
                dados_usuario['telefone'],
                dados_usuario['data_nascimento']
            )
            self.__usuario_dao.add(usuario)
            self.__tela_usuario.mostrar_mensagem("Usuário cadastrado com sucesso!")

    def editar_usuario(self):
        """Edita um usuário existente com novos dados fornecidos pelo usuário."""
        if not self.__usuario_dao.get_all():
            self.__tela_usuario.mostrar_mensagem("Nenhum usuário cadastrado.")
            return

        self.listar_usuarios()
        nome_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pegar_usuario_pelo_nome(nome_usuario)

        if usuario is not None:
            novos_dados_usuario = self.__tela_usuario.pegar_dados_usuario()

            # Remover o usuário antigo do DAO antes de atualizar
            self.__usuario_dao.remove(usuario.nome)
            
            # Atualizar os dados do usuário
            usuario.nome = novos_dados_usuario['nome']
            usuario.email = novos_dados_usuario['email']
            usuario.telefone = novos_dados_usuario['telefone']
            usuario.data_nascimento = novos_dados_usuario['data_nascimento']
            
            # Adicionar o usuário atualizado ao DAO
            self.__usuario_dao.add(usuario)
            
            self.__tela_usuario.mostrar_mensagem("Usuário editado com sucesso!")
        else:
            self.__tela_usuario.mostrar_mensagem('ATENÇÃO: Usuário não existente')

    def remover_usuario(self):
        """Remove um usuário da lista de usuários cadastrados."""
        if not self.__usuario_dao.get_all():
            self.__tela_usuario.mostrar_mensagem("Nenhum usuário cadastrado.")
            return

        self.listar_usuarios()
        nome_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pegar_usuario_pelo_nome(nome_usuario)

        if usuario is not None:
            self.__usuario_dao.remove(nome_usuario)
            self.__tela_usuario.mostrar_mensagem("Usuário removido com sucesso!")
        else:
            self.__tela_usuario.mostrar_mensagem("ATENÇÃO: Usuário não existente")

    def seguir_artista(self):
        """Permite que um usuário siga um artista."""
        self.__tela_usuario.mostrar_mensagem("Seguir Artista")
        if not self.__controlador_sistema.controlador_artistas.artistas:
            self.__tela_usuario.mostrar_mensagem("Nenhum artista cadastrado.")
            return

        nome_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pegar_usuario_pelo_nome(nome_usuario)

        if usuario:
            nome_artista = self.__tela_usuario.pegar_nome_artista()
            artista = self.__controlador_sistema.controlador_artistas.pegar_artista_pelo_nome(nome_artista)

            if artista:
                usuario.artistas_seguidos.append(artista)
                self.__usuario_dao.update(usuario)
                self.__tela_usuario.mostrar_mensagem(f"Você seguiu o artista {artista.nome}!")
            else:
                self.__tela_usuario.mostrar_mensagem("Artista não encontrado!")
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário não encontrado!")

    def ver_artistas_seguidos(self):
        """Exibe os artistas seguidos pelo usuário."""
        self.__tela_usuario.mostrar_mensagem("Artistas Seguidos")
        nome_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pegar_usuario_pelo_nome(nome_usuario)

        if usuario:
            artistas_dados = []
            for artista in usuario.artistas_seguidos:
                artista_info = {
                    'nome': artista.nome,
                    'email': artista.email,
                    'telefone': artista.telefone,
                    'data_nascimento': artista.data_nascimento
                }
                artistas_dados.append(artista_info)

            if artistas_dados:
                self.__tela_usuario.mostrar_artistas_seguidos(artistas_dados)
            else:
                self.__tela_usuario.mostrar_mensagem("Você não segue nenhum artista.")
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário não encontrado!")

    def deixar_de_seguir_artista(self):
        """Permite que um usuário deixe de seguir um artista."""
        self.__tela_usuario.mostrar_mensagem("Deixar de Seguir Artista")
        nome_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pegar_usuario_pelo_nome(nome_usuario)

        if usuario:
            nome_artista = self.__tela_usuario.pegar_nome_artista()
            artista = self.__controlador_sistema.controlador_artistas.pegar_artista_pelo_nome(nome_artista)

            if artista:
                if artista in usuario.artistas_seguidos:
                    usuario.artistas_seguidos.remove(artista)
                    self.__usuario_dao.update(usuario)
                    self.__tela_usuario.mostrar_mensagem(f"Você deixou de seguir o artista {artista.nome}!")
                else:
                    self.__tela_usuario.mostrar_mensagem("Você não segue esse artista!")
            else:
                self.__tela_usuario.mostrar_mensagem("Artista não encontrado!")
        else:
            self.__tela_usuario.mostrar_mensagem("Usuário não encontrado!")

    def abrir_playlists(self):
        """Abre a tela de playlists."""
        self.__controlador_playlists.abre_tela()

    def retornar(self):
        """Retorna para a tela do controlador de sistema."""
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        """Exibe o menu de opções para manipulação de usuários e artistas e executa as ações correspondentes."""
        while True:
            opcao = self.__tela_usuario.imprimir_opcoes()
            if opcao == 0:
                self.retornar()
                break
            elif opcao == 1:
                self.cadastrar_usuario()
            elif opcao == 2:
                self.listar_usuarios()
            elif opcao == 3:
                self.editar_usuario()
            elif opcao == 4:
                self.remover_usuario()
            elif opcao == 5:
                self.abrir_playlists()
            elif opcao == 6:
                self.seguir_artista()
            elif opcao == 7:
                self.deixar_de_seguir_artista()
            elif opcao == 8:
                self.ver_artistas_seguidos()
            else:
                self.__tela_usuario.mostrar_mensagem("Opção inválida!")
