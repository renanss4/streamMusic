from telas.tela_sistema import TelaSistema
from controles.controlador_usuario import ControladorUsuario
from controles.controlador_artista import ControladorArtista
from controles.controlador_gravadora import ControladorGravadora



class ControladorSistema:
    """Controlador principal do sistema."""

    def __init__(self) -> None:
        """Inicializa o controlador do sistema."""
        self.__tela_sistema = TelaSistema()
        self.__controlador_usuarios = ControladorUsuario(self)
        self.__controlador_artistas = ControladorArtista(self)
        self.__controlador_gravadoras = ControladorGravadora(self)

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    @property
    def controlador_artistas(self):
        return self.__controlador_artistas

    @property
    def controlador_gravadoras(self):
        return self.__controlador_gravadoras

    def abrir_usuarios(self):
        """Abre o controlador de usuários."""
        self.__controlador_usuarios.abre_tela()

    def abrir_artistas(self):
        """Abre o controlador de artistas."""
        self.__controlador_artistas.abre_tela()

    def abrir_gravadoras(self):
        """Abre o controlador de gravadoras."""
        self.__controlador_gravadoras.abre_tela()

    def inicializar_sistema(self):
        """Inicia o sistema."""
        self.abre_tela()

    def encerrar_sistema(self):
        """Encerra o sistema."""
        self.__tela_sistema.mostrar_mensagem("Encerrando o sistema...")
        exit(0)

    def abre_tela(self):
        """Abre a tela principal do sistema."""
        while True:
            opcao = self.__tela_sistema.imprimir_opcoes()
            if opcao == 0:
                self.encerrar_sistema()
                break
            elif opcao == 1:
                self.abrir_usuarios()
            elif opcao == 2:
                self.abrir_artistas()
            elif opcao == 3:
                self.abrir_gravadoras()
            else:
                self.__tela_sistema.mostrar_mensagem('Opção Inválida!')
