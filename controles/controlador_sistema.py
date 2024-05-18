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

    @property
    def controlador_usuario(self):
        return self.__controlador_usuarios
 
    def abrir_usuarios(self):
        # Chama o controlador de Usuários
        self.__controlador_usuarios.abre_tela()

    def abrir_artistas(self):
        self.__controlador_artistas.abre_tela()

    def abrir_gravadora(self):
        self.__controlador_gravadoras.abre_tela()

    def abrir_contrato(self):
        self.__controlador_contratos.abre_tela()
   
    def inicializa_sistema(self):
        self.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {
            1: self.abrir_usuarios,
            2: self.abrir_artistas,
            3: self.abrir_gravadora,
            4: self.abrir_contrato,
            0: self.encerra_sistema
        }

        rodando = True
        while rodando:
            opcao_escolhida = self.__tela_sistema.imprimir_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()