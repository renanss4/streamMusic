from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario
from controles.controlador_playlist import ControladorPlaylist

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_playlists = ControladorPlaylist(self)
        self.__controlador_sistema = controlador_sistema

    def pegar_usuario_pelo_username(self, username: str):
        for usuario in self.__usuarios:
            if usuario.username == username:
                return usuario
        return None

    def listar_usuarios(self):
        if self.__usuarios:
            usuarios_dados = [{'nome': usuario.nome, 'username': usuario.username,
                               'email': usuario.email, 'telefone': usuario.telefone}
                              for usuario in self.__usuarios]
            self.__tela_usuario.mostrar_usuarios(usuarios_dados)
        else:
            self.__tela_usuario.mostrar_mensagem("Nenhum usuário cadastrado.")

    def cadastrar_usuario(self):
        dados_usuario = self.__tela_usuario.pegar_dados_usuario()
        if self.pegar_usuario_pelo_username(dados_usuario['username']):
            self.__tela_usuario.mostrar_mensagem("Usuário já cadastrado!")
        else:
            usuario = Usuario(
                dados_usuario['nome'],
                dados_usuario['username'],
                dados_usuario['email'],
                dados_usuario['telefone']
            )
            self.__usuarios.append(usuario)
            self.__tela_usuario.mostrar_mensagem("Usuário cadastrado com sucesso!")

    def editar_usuario(self):
        if not self.__usuarios:
            self.__tela_usuario.mostrar_mensagem("Nenhum usuário cadastrado.")
            return

        self.listar_usuarios()
        username_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pegar_usuario_pelo_username(username_usuario)

        if usuario is not None:
            novos_dados_usuario = self.__tela_usuario.pegar_dados_usuario()
            usuario.nome = novos_dados_usuario['nome']
            usuario.username = novos_dados_usuario['username']
            usuario.email = novos_dados_usuario['email']
            usuario.telefone = novos_dados_usuario['telefone']
            self.__tela_usuario.mostrar_mensagem("Usuário editado com sucesso!")
        else:
            self.__tela_usuario.mostrar_mensagem('ATENÇÃO: Usuário não existente')

    def remover_usuario(self):
        if not self.__usuarios:
            self.__tela_usuario.mostrar_mensagem("Nenhum usuário cadastrado.")
            return

        self.listar_usuarios()
        username_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pegar_usuario_pelo_username(username_usuario)

        if usuario is not None:
            self.__usuarios.remove(usuario)
            self.__tela_usuario.mostrar_mensagem("Usuário removido com sucesso!")
        else:
            self.__tela_usuario.mostrar_mensagem("ATENÇÃO: Usuário não existente")

    def abrir_playlists(self):
        self.__controlador_playlists.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
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
            else:
                self.__tela_usuario.mostrar_mensagem("Opção inválida!")
