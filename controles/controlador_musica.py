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
        for musica in self.__musicas:
            self.__tela_musica.mostrar_musica({
                'nome': musica.nome,
                'letra': musica.letra
            })

    def cadastrar_musica(self):
        dados_musica = self.__tela_musica.pegar_dados_musica()
        musica = Musica(
            dados_musica['nome'],
            dados_musica['letra']
        )
        self.__musicas.append(musica)

    def editar_musica(self):
        self.listar_musicas()
        nome_musica = self.__tela_musica.pegar_dados_musica()
        musica = self.pegar_musica_pelo_nome(nome_musica)

        if musica is not None:
            novos_dados_musica = self.__tela_musica.pegar_dados_musica()
            musica.nome = novos_dados_musica['nome'],
            musica.letra = novos_dados_musica['letra']
            self.listar_musicas()
        else:
            self.__tela_musica.mostrar_mensagem('ATENÇÃO: Música não existente')

    def remover_musica(self):
        self.listar_musicas()
        nome_musica = self.__tela_musica.pegar_dados_musica()
        musica = self.pegar_musica_pelo_nome(nome_musica)

        if musica is not None:
            self.__musicas.remove(musica)
            self.listar_musicas()
        else:
            self.__tela_musica.mostrar_mensagem('ATENÇÃO: Música não existente')

    def retornar(self):
        self.__controlador_artista.abre_tela()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastrar_musica,
            2: self.editar_musica,
            3: self.listar_musicas,
            4: self.remover_musica,
            0: self.retornar
        }

        rodando = True
        while rodando:
            opcao = self.__tela_musica.imprimir_opcoes()
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
            else:
                self.__tela_musica.mostrar_mensagem('Opção Inválida!')