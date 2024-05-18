from telas.tela_sistema import TelaSistema
from controles.controlador_usuario import ControladorUsuario
from controles.controlador_artista import ControladorArtista
from controles.controlador_gravadora import ControladorGravadora
from controles.controlador_contrato import ControladorContrato


class ControladorSistema:

    def __init__(self) -> None:
        self.__tela_sistema = TelaSistema()
        self.__controlador_usuarios = ControladorUsuario(self)
        self.__controlador_artistas = ControladorArtista(self)
        self.__controlador_gravadoras = ControladorGravadora(self)
        self.__controlador_contratos = ControladorContrato(self)

    def abrir_usuarios(self):
        self.__controlador_usuarios.abre_tela()

    def abrir_artistas(self):
        self.__controlador_artistas.abre_tela()

    def abrir_gravadoras(self):
        self.__controlador_gravadoras.abre_tela()

    def abrir_contratos(self):
        self.__controlador_contratos.abre_tela()

    def inicializar_sistema(self):
        self.abre_tela()

    def encerrar_sistema(self):
        exit(0)

    def abre_tela(self):
        while True:
            opcao = self.__tela_sistema.imprimir_opcoes()
            if opcao == 00:
                self.encerrar_sistema()
                break
            elif opcao == 1:
                self.abrir_usuarios()
            elif opcao == 2:
                self.abrir_artistas()
            elif opcao == 3:
                self.abrir_gravadoras()
            elif opcao == 4:
                self.abrir_contratos()
            else:
                self.__tela_sistema.mostrar_mensagem('Opção Inválida!')
