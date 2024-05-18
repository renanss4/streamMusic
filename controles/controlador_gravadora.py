from telas.tela_gravadora import TelaGravadora
from entidades.gravadora import Gravadora
from controles.controlador_contrato import ControladorContrato

class ControladorGravadora:
    def __init__(self, controlador_sistema):
        self.__gravadoras = []
        self.__tela_gravadora = TelaGravadora()
        self.__controlador_contratos = ControladorContrato(self)
        self.__controlador_sistema = controlador_sistema

    def pegar_gravadora_pelo_nome(self, nome: str):
        for gravadora in self.__gravadoras:
            if gravadora.nome == nome:
                return gravadora
        return None
    
    def listar_gravadoras(self):
        if self.__gravadoras:
            gravadoras_dados = [{'nome': gravadora.nome, 'email': gravadora.email,
                                 'telefone': gravadora.telefone} for gravadora in self.__gravadoras]
            self.__tela_gravadora.mostrar_gravadoras(gravadoras_dados)
        else:
            self.__tela_gravadora.mostrar_mensagem("Nenhuma gravadora cadastrada.")

    def cadastrar_gravadora(self):
        dados_gravadora = self.__tela_gravadora.pegar_dados_gravadora()
        if self.pegar_gravadora_pelo_nome(dados_gravadora['nome']):
            self.__tela_gravadora.mostrar_mensagem("Gravadora já cadastrada!")
        else:
            gravadora = Gravadora(
                dados_gravadora['nome'],
                dados_gravadora['email'],
                dados_gravadora['telefone']
            )
            self.__gravadoras.append(gravadora)
            self.__tela_gravadora.mostrar_mensagem(f"Gravadora {gravadora.nome} adicionada com sucesso.")

    def editar_gravadora(self):
        if not self.__gravadoras:
            self.__tela_gravadora.mostrar_mensagem("Nenhuma gravadora cadastrada.")
            return

        self.listar_gravadoras()
        nome_gravadora = self.__tela_gravadora.buscar_gravadora()
        gravadora = self.pegar_gravadora_pelo_nome(nome_gravadora)

        if gravadora is not None:
            novos_dados_gravadora = self.__tela_gravadora.pegar_dados_gravadora()
            gravadora.nome = novos_dados_gravadora['nome']
            gravadora.email = novos_dados_gravadora['email']
            gravadora.telefone = novos_dados_gravadora['telefone']
            self.listar_gravadoras()
        else:
            self.__tela_gravadora.mostrar_mensagem('ATENÇÃO: Gravadora não existente')

    def remover_gravadora(self):
        if not self.__gravadoras:
            self.__tela_gravadora.mostrar_mensagem("Nenhuma gravadora cadastrada.")
            return

        self.listar_gravadoras()
        nome_gravadora = self.__tela_gravadora.buscar_gravadora()
        gravadora = self.pegar_gravadora_pelo_nome(nome_gravadora)

        if gravadora is not None:
            self.__gravadoras.remove(gravadora)
            self.listar_gravadoras()
            self.__tela_gravadora.mostrar_mensagem("Gravadora removida com sucesso!")
        else:
            self.__tela_gravadora.mostrar_mensagem("ATENÇÃO: Gravadora não existente")

    def abrir_contratos(self):
        self.__controlador_contratos.abre_tela()

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
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
