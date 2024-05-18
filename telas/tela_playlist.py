class TelaPlaylist:

    def imprimir_opcoes(self):
        print('\n')
        print('----------PLAYLIST----------')
        print("Escolha a opção")
        print("1 - Cadastrar Playlist")
        print("2 - Editar Playlist")
        print("3 - Listar Playlists")
        print("4 - Excluir Playlist")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pegar_dados_playlist(self):
        print('\n')
        print("-------- CADASTRAR NOVA PLAYLIST ----------")
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        return {'nome': nome, 'descricao': descricao}

    def mostrar_playlist(self, dados_playlist):
        print('\n')
        print("-------- DETALHES DA PLAYLIST ----------")
        print("Nome:", dados_playlist["nome"])
        print("Descrição:", dados_playlist["descricao"])

    def buscar_playlist(self):
        nome = input('Nome da playlist que deseja buscar: ')
        return nome

    def mostrar_mensagem(self, msg):
        print(msg)

        