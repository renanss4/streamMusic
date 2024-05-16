from telas.tela_usuario import TelaUsuario
from entidades.usuario import Usuario

class ControladorUsuario:
    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def pega_usuario_pelo_identificador(self, identificador: str):
        for usuario in self.__usuarios:
            if (usuario.identificador == identificador):
                return usuario
        return None

    def listar_usuarios(self):
        for usuario in self.__usuarios:
            self.__tela_usuario.mostrar_usuario({
                "nome": usuario.nome,
                "identificador": usuario.identificador,
                "email": usuario.email,
                "telefone": usuario.telefone
            })

    def cadastrar_usuario(self):
        dados_usuario = self.__tela_usuario.pegar_dados_usuario()
        usuario = Usuario(
            dados_usuario["nome"],
            dados_usuario["identificador"],
            dados_usuario["email"],
            dados_usuario["senha"],
            dados_usuario["telefone"]
        )
        self.__usuarios.append(usuario)

    def editar_usuario(self):
        self.listar_usuarios()
        identificador_usuario = self.__tela_usuario.pegar_dados_usuario()
        usuario = self.pega_usuario_pelo_identificador(identificador_usuario)

        if (usuario is not None):
            novos_dados_usuario = self.__tela_usuario.pegar_dados_usuario()
            usuario.nome = novos_dados_usuario["nome"],
            usuario.identificador = novos_dados_usuario["identificador"],
            usuario.email = novos_dados_usuario["email"],
            usuario.senha = novos_dados_usuario["senha"],
            usuario.telefone = novos_dados_usuario["telefone"]
            self.listar_usuarios()
        else:
            self.__tela_usuario.mostrar_mensagem('ATENÇÃO: Usuário não existente')

    def remover_usuario(self):
        self.listar_usuarios()
        identificador_usuario = self.__tela_usuario.buscar_usuario()
        usuario = self.pega_usuario_pelo_identificador(identificador_usuario)

        if(usuario is not None):
            self.__usuarios.remove(usuario)
            self.listar_usuarios()
        else:
            self.__tela_usuario.mostrar_mensagem("ATENCAO: Usuário não existente")

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_usuario,
            2: self.editar_usuario,
            3: self.listar_usuarios,
            4: self.remover_usuario,
            0: self.retornar
        }

        rodando = True
        while rodando:
            lista_opcoes[self.__tela_usuario.imprimir_opcoes()]()