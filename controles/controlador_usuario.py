from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def pegar_usuario_pelo_username(self, username: str):
        for usuario in self.__usuarios:
            if (usuario.username == username):
                return usuario
        return None

    def listar_usuarios(self):
        for usuario in self.__usuarios:
            self.__tela_usuario.mostrar_usuario({
                "nome": usuario.nome,
                "username": usuario.username,
                "email": usuario.email,
                "telefone": usuario.telefone
            })

    def cadastrar_usuario(self):
        dados_usuario = self.__tela_usuario.pegar_dados_usuario()
        usuario = Usuario(
            dados_usuario["nome"],
            dados_usuario["username"],
            dados_usuario["email"],
            dados_usuario["telefone"]
        )
        self.__usuarios.append(usuario)

    def editar_usuario(self):
        self.listar_usuarios()
        username_usuario = self.__tela_usuario.pegar_dados_usuario()
        usuario = self.pegar_usuario_pelo_username(username_usuario)

        if (usuario is not None):
            novos_dados_usuario = self.__tela_usuario.pegar_dados_usuario()
            usuario.nome = novos_dados_usuario["nome"],
            usuario.username = novos_dados_usuario["username"],
            usuario.email = novos_dados_usuario["email"],
            usuario.telefone = novos_dados_usuario["telefone"]
            self.listar_usuarios()
        else:
            self.__tela_usuario.mostrar_mensagem('ATENÇÃO: Usuário não existente')

    def remover_usuario(self):
        self.listar_usuarios()
        username_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pegar_usuario_pelo_username(username_usuario)

        if(usuario is not None):
            self.__usuarios.remove(usuario)
            self.listar_usuarios()
        else:
            self.__tela_usuario.mostrar_mensagem("ATENÇÃO: Usuário não existente")

    # def seguir_artista(self):
    #     self.listar_usuarios()
    #     username_usuario = self.__tela_usuario.buscar_usuario()
    #     usuario = self.pegar_usuario_pelo_username(username_usuario)

    #     if usuario is not None:
    #         artista = self.__tela_usuario.pegar_artista()
    #         usuario.seguir_artista(artista)
    #         self.__tela_usuario.mostrar_mensagem(f"Artista '{artista}' seguido com sucesso!")
    #     else:
    #         self.__tela_usuario.mostrar_mensagem("ATENÇÃO: Usuário não existente")

    # def deixar_de_seguir_artista(self):
    #     self.listar_usuarios()
    #     username_usuario = self.__tela_usuario.buscar_usuario()
    #     usuario = self.pegar_usuario_pelo_username(username_usuario)

    #     if usuario is not None:
    #         artista = self.__tela_usuario.pegar_artista()
    #         usuario.deixar_de_seguir(artista)
    #         self.__tela_usuario.mostrar_mensagem(f"Artista '{artista}' deixado de seguir com sucesso!")
    #     else:
    #         self.__tela_usuario.mostrar_mensagem("ATENÇÃO: Usuário não existente")

    # def mostrar_artistas_seguidos(self):
    #     self.listar_usuarios()
    #     username_usuario = self.__tela_usuario.buscar_usuario()
    #     usuario = self.pegar_usuario_pelo_username(username_usuario)

    #     if usuario is not None:
    #         artistas_seguidos = usuario.mostrar_artistas_seguidos()
    #         self.__tela_usuario.mostrar_artistas_seguidos(artistas_seguidos)
    #     else:
    #         self.__tela_usuario.mostrar_mensagem("ATENÇÃO: Não há nenhum Artista seguido")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_usuario,
            2: self.editar_usuario,
            3: self.listar_usuarios,
            4: self.remover_usuario,
            # 5: self.seguir_artista,
            # 6: self.deixar_de_seguir_artista,
            # 7: self.mostrar_artistas_seguidos,
            0: self.retornar
        }

        rodando = True
        while rodando:
            opcao = self.__tela_usuario.imprimir_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_usuario.mostrar_mensagem("Opção inválida!")