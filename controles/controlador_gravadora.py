from telas.tela_gravadora import TelaGravadora
from entidades.gravadora import Gravadora

class ControladorGravadora:
    def __init__(self):
        self.gravadoras = []
        self.__tela_gravadora = TelaGravadora()

    def adicionar_gravadora(self):
        dados_gravadora = self.__tela_gravadora.pegar_dados_gravadora()
        nome = dados_gravadora["nome"]
        gravadora = Gravadora(nome)
        self.gravadoras.append(gravadora)
        self.__tela_gravadora.mostra_mensagem(f"Gravadora {gravadora.nome} adicionada com sucesso.")

    def buscar_gravadora(self, nome):
        for gravadora in self.gravadoras:
            if gravadora.nome == nome:
                self.__tela_gravadora.mostra_gravadora(gravadora)
                return
        self.__tela_gravadora.mostra_mensagem(f"Não foi encontrada nenhuma gravadora com o nome {nome}.")

    def listar_gravadoras(self):
        self.__tela_gravadora.mostra_gravadora(self.gravadoras)

    def editar_gravadora(self, nome):
        for gravadora in self.gravadoras:
            if gravadora.nome == nome:
                novos_dados_gravadora = self.__tela_gravadora.editar_gravadora()
                novo_nome = novos_dados_gravadora.get("nome")
                if novo_nome:
                    gravadora.nome = novo_nome
                self.__tela_gravadora.mostrar_mensagem(f"Gravadora {gravadora.nome} atualizada com sucesso.")
                return
        self.__tela_gravadora.mostrar_mensagem(f"Não foi encontrada nenhuma gravadora com o nome {nome}.")

    def remover_gravadora(self, nome):
        for gravadora in self.gravadoras:
            if gravadora.nome == nome:
                self.gravadoras.remove(gravadora)
                self.__tela_gravadora.mostra_mensagem(f"Gravadora {gravadora.nome} removida com sucesso.")
                return
        self.__tela_gravadora.mostra_mensagem(f"Não foi encontrada nenhuma gravadora com o nome {nome}.")
