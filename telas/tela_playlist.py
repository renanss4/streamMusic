class TelaPlaylist:

    def imprimir_opcoes(self):
        print('\n')
        print('---------- PLAYLIST ----------')
        print("Escolha a opção")
        print("1 - Cadastrar Playlist")
        print("2 - Listar Playlists")
        print("3 - Editar Playlist")
        print("4 - Excluir Playlist")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 4:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 4.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_playlist(self):
        print('\n')
        print("-------- CADASTRAR/EDITAR PLAYLIST ----------")
        nome = input("Nome: ").strip()
        descricao = input("Descrição: ").strip()
        return {'nome': nome, 'descricao': descricao}

    def mostrar_playlists(self, playlists_dados):
        print('\n')
        print("-------- DETALHES DA PLAYLIST ----------")
        for dados_playlist in playlists_dados:
            print("Nome:", dados_playlist["nome"])
            print("Descrição:", dados_playlist["descricao"])
            print('--------------------------------')

    def buscar_playlist(self):
        print("\n")
        nome = input('Nome da playlist que deseja buscar: ').strip()
        return nome

    def mostrar_mensagem(self, msg):
        print("\n")
        print(msg)
