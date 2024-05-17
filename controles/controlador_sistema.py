from telas.tela_sistema import TelaSistema
from controles.controlador_usuario import ControladorUsuario
from controles.controlador_artista import ControladorArtista


class ControladorSistema:

    def __init__(self) -> None:
        self.__tela_sistema = TelaSistema()
        self.__controlador_usuarios = ControladorUsuario(self)
        self.__controlador_artistas = ControladorArtista(self)

    @property
    def controlador_usuario(self):
        return self.__controlador_usuarios
 
    def cadastrar_usuarios(self):
        # Chama o controlador de Usuários
        self.__controlador_usuarios.abre_tela()

    def cadastrar_artistas(self):
        self.__controlador_artistas.abre_tela()
   
    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_usuarios,
            2: self.cadastrar_artistas,
            0: self.encerra_sistema
        }

        rodando = True
        while rodando:
            opcao_escolhida = self.__tela_sistema.imprimir_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()