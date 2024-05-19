from telas.tela_musica import TelaMusica
from entidades.musica import Musica

class ControladorMusica:
    def __init__(self, controlador_artista) -> None:
        self.__musicas = []
        self.__tela_musica = TelaMusica()
        self.__controlador_artista = controlador_artista

    def pegar_musica_pelo_nome(self, nome: str):
        for musica in self.__musicas:
            if musica.nome == nome:
                return musica
        return None

    def listar_musicas(self):
        if self.__musicas:
            musicas_dados = [{'nome': musica.nome, 'letra': musica.letra} for musica in self.__musicas]
            self.__tela_musica.mostrar_musicas(musicas_dados)
        else:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")

    def cadastrar_musica(self):
        dados_musica = self.__tela_musica.pegar_dados_musica()
        if self.pegar_musica_pelo_nome(dados_musica['nome']):
            self.__tela_musica.mostrar_mensagem("Música já existente!")
        else:
            musica = Musica(dados_musica['nome'], dados_musica['letra'])
            self.__musicas.append(musica)
            self.__tela_musica.mostrar_mensagem("Música cadastrada com sucesso!")

    def editar_musica(self):
        if not self.__musicas:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")
            return

        self.listar_musicas()
        nome_musica = self.__tela_musica.buscar_musica()
        musica = self.pegar_musica_pelo_nome(nome_musica)

        if musica is not None:
            novos_dados_musica = self.__tela_musica.pegar_dados_musica()
            musica.nome = novos_dados_musica['nome']
            musica.letra = novos_dados_musica['letra']
            self.__tela_musica.mostrar_mensagem("Música editada com sucesso!")
        else:
            self.__tela_musica.mostrar_mensagem('ATENÇÃO: Música não existente')

    def adicionar_musica(self, musica):
        self.__musicas.append(musica)


    def remover_musica(self):
        if not self.__musicas:
            self.__tela_musica.mostrar_mensagem("Nenhuma música cadastrada.")
            return

        self.listar_musicas()
        nome_musica = self.__tela_musica.buscar_musica()
        musica = self.pegar_musica_pelo_nome(nome_musica)

        if musica is not None:
            self.__musicas.remove(musica)
            self.__tela_musica.mostrar_mensagem("Música removida com sucesso!")
        else:
            self.__tela_musica.mostrar_mensagem('ATENÇÃO: Música não existente')

    def pegar_dados_musica(self):
        return self.__tela_musica.pegar_dados_musica()

    def mostrar_musicas(self, musicas):
        self.__tela_musica.mostrar_musicas(musicas)

    def mostrar_mensagem(self, mensagem: str):
        self.__tela_musica.mostrar_mensagem(mensagem)

    def pegar_musicas_por_artista(self, artista):
        musicas_do_artista = [musica for musica in self.__musicas if musica.artista == artista]
        return musicas_do_artista


    def retornar(self):
        self.__controlador_artista.abre_tela()

    def abre_tela(self):
        while True:
            opcao = self.__tela_musica.imprimir_opcoes()
            if opcao == 0:
                self.retornar()
                break
            elif opcao == 1:
                self.cadastrar_musica()
            elif opcao == 2:
                self.listar_musicas()
            elif opcao == 3:
                self.editar_musica()
            elif opcao == 4:
                self.remover_musica()
            else:
                self.__tela_musica.mostrar_mensagem('Opção Inválida!')
