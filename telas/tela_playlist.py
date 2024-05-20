class TelaPlaylist:

    def imprimir_opcoes(self):
        """
        Mostra as opções disponíveis para o usuário e retorna a escolha.
        """
        print()
        print("##################################")
        print('# ---------- PLAYLIST ---------- #')
        print("# Escolha a opção                #")
        print("# 1 - Cadastrar Playlist         #")
        print("# 2 - Listar Playlists           #")
        print("# 3 - Editar Playlist            #")
        print("# 4 - Excluir Playlist           #")
        print("# 0 - Retornar                   #")
        print("##################################")

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
        """
        Solicita e retorna os dados de uma nova playlist.
        """
        print('\n-------- CADASTRAR/EDITAR PLAYLIST ----------')
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            else:
                print('Nome não pode ser vazio')
        descricao = input("Descrição: ").strip()
        return {'nome': nome, 'descricao': descricao}

    def mostrar_playlists(self, playlists_dados):
        """
        Mostra os detalhes das playlists cadastradas.
        """
        print('\n-------- DETALHES DA PLAYLIST ----------')
        for dados_playlist in playlists_dados:
            print("Nome:", dados_playlist["nome"])
            print("Descrição:", dados_playlist["descricao"])
            print('--------------------------------')

    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        print('\n' + msg + '\n')
