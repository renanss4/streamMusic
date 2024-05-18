from telas.tela_gravadora import TelaGravadora
from entidades.gravadora import Gravadora

class ControladorGravadora:
    def __init__(self, controlador_sistema):
        self.__gravadoras = []
        self.__tela_gravadora = TelaGravadora()
        self.__controlador_sistema = controlador_sistema

    def pegar_gravadora_pelo_nome(self, nome: str):
        for gravadora in self.__gravadoras:
            if gravadora.nome == nome:
                return gravadora
        return None
    
    def listar_gravadoras(self):
        for gravadora in self.__gravadoras:
            self.__tela_gravadora.mostrar_gravadora({
                'nome': gravadora.nome,
                'email': gravadora.email,
                'telefone': gravadora.telefone
            })

    def cadastrar_gravadora(self):
        dados_gravadora = self.__tela_gravadora.pegar_dados_gravadora()
        gravadora = Gravadora(
            dados_gravadora['nome'],
            dados_gravadora['email'],
            dados_gravadora['telefone']
        )
        self.__gravadoras.append(gravadora)
        self.__tela_gravadora.mostrar_mensagem(f"Gravadora {gravadora.nome} adicionada com sucesso.")

    def editar_gravadora(self):
        self.listar_gravadoras()
        nome_gravadora = self.__tela_gravadora.pegar_dados_gravadora()
        gravadora = self.pegar_gravadora_pelo_nome(nome_gravadora)

        if gravadora is not None:
            novos_dados_gravadora = self.__tela_gravadora.pegar_dados_gravadora()
            gravadora.nome = novos_dados_gravadora['nome'],
            gravadora.email = novos_dados_gravadora['email'],
            gravadora.telefone = novos_dados_gravadora['telefone']
            self.listar_gravadoras()
        else:
            self.__tela_gravadora.mostrar_mensagem('ATENÇÃO: Gravadora não existente')

    def remover_gravadora(self):
        self.listar_gravadoras()
        nome_gravadora = self.__tela_gravadora.pegar_dados_gravadora()
        gravadora = self.pegar_gravadora_pelo_nome(nome_gravadora)

        if gravadora is not None:
            self.__gravadoras.remove(gravadora)
            self.listar_gravadoras()
            print('foi apaga com sucesso')
        else:
            self.__tela_gravadora.mostrar_mensagem('ATENÇÃO: Gravadora não existente')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_gravadora,
            2: self.editar_gravadora,
            3: self.listar_gravadoras,
            4: self.remover_gravadora,
            0: self.retornar
        }

        rodando = True
        while rodando:
            opcao = self.__tela_gravadora.imprimir_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_gravadora.mostrar_mensagem('Opção Inválida!')