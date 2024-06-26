from telas.tela_gravadora import TelaGravadora
from daos.gravadora_dao import GravadoraDAO
from entidades.gravadora import Gravadora
from controles.controlador_contrato import ControladorContrato

class ControladorGravadora:
    """Controlador para gerenciar operações relacionadas a gravadoras."""

    def __init__(self, controlador_sistema):
        """Inicializa o controlador de gravadora."""
        self.__gravadora_dao = GravadoraDAO()  # Instância do DAO para manipular gravadoras
        self.__tela_gravadora = TelaGravadora()
        self.__controlador_contratos = ControladorContrato(self)
        self.__controlador_sistema = controlador_sistema

    def pegar_gravadora_pelo_nome(self, nome: str):
        """Retorna a gravadora correspondente ao nome fornecido."""
        return self.__gravadora_dao.get(nome)

    def listar_gravadoras(self):
        """Lista todas as gravadoras cadastradas."""
        gravadoras = self.__gravadora_dao.get_all()
        if gravadoras:
            gravadoras_dados = [{'nome': gravadora.nome, 'email': gravadora.email,
                                 'telefone': gravadora.telefone} for gravadora in gravadoras]
            self.__tela_gravadora.mostrar_gravadoras(gravadoras_dados)
        else:
            self.__tela_gravadora.mostrar_mensagem("Nenhuma gravadora cadastrada.")

    def cadastrar_gravadora(self):
        """Realiza o cadastro de uma nova gravadora."""
        dados_gravadora = self.__tela_gravadora.pegar_dados_gravadora()
        if self.pegar_gravadora_pelo_nome(dados_gravadora['nome']):
            self.__tela_gravadora.mostrar_mensagem("Gravadora já cadastrada!")
        else:
            gravadora = Gravadora(
                dados_gravadora['nome'],
                dados_gravadora['email'],
                dados_gravadora['telefone']
            )
            self.__gravadora_dao.add(gravadora)
            self.__tela_gravadora.mostrar_mensagem(f"Gravadora {gravadora.nome} adicionada com sucesso.")

    def editar_gravadora(self):
        """Permite a edição dos dados de uma gravadora."""
        gravadoras = self.__gravadora_dao.get_all()
        if not gravadoras:
            self.__tela_gravadora.mostrar_mensagem("Nenhuma gravadora cadastrada.")
            return

        self.listar_gravadoras()
        nome_gravadora = self.__tela_gravadora.buscar_gravadora()
        gravadora = self.pegar_gravadora_pelo_nome(nome_gravadora)

        if gravadora is not None:
            novos_dados_gravadora = self.__tela_gravadora.pegar_dados_gravadora()

            # Remover a gravadora antiga e adicionar a nova
            self.__gravadora_dao.remove(gravadora.nome)

            gravadora.nome = novos_dados_gravadora['nome']
            gravadora.email = novos_dados_gravadora['email']
            gravadora.telefone = novos_dados_gravadora['telefone']
            
            self.__gravadora_dao.add(gravadora)
            self.__tela_gravadora.mostrar_mensagem("Gravadora editada com sucesso!")
        else:
            self.__tela_gravadora.mostrar_mensagem('ATENÇÃO: Gravadora não existente')

    def remover_gravadora(self):
        """Remove uma gravadora."""
        gravadoras = self.__gravadora_dao.get_all()
        if not gravadoras:
            self.__tela_gravadora.mostrar_mensagem("Nenhuma gravadora cadastrada.")
            return

        self.listar_gravadoras()
        nome_gravadora = self.__tela_gravadora.buscar_gravadora()
        gravadora = self.pegar_gravadora_pelo_nome(nome_gravadora)

        if gravadora is not None:
            self.__gravadora_dao.remove(nome_gravadora)
            self.__tela_gravadora.mostrar_mensagem("Gravadora removida com sucesso!")
        else:
            self.__tela_gravadora.mostrar_mensagem("ATENÇÃO: Gravadora não existente")

    def abrir_contratos(self):
        """Abre o controlador de contrato."""
        self.__controlador_contratos.abre_tela()

    def retornar(self):
        """Retorna ao controlador de sistema."""
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        """Abre a tela do controlador de gravadora."""
        while True:
            opcao = self.__tela_gravadora.imprimir_opcoes()
            if opcao == 0:
                self.retornar()
                break
            elif opcao == 1:
                self.cadastrar_gravadora()
            elif opcao == 2:
                self.listar_gravadoras()
            elif opcao == 3:
                self.editar_gravadora()
            elif opcao == 4:
                self.remover_gravadora()
            elif opcao == 5:
                self.abrir_contratos()
            else:
                self.__tela_gravadora.mostrar_mensagem('Opção Inválida!')
