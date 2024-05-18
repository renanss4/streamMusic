class TelaArtista:

    def imprimir_opcoes(self):
        print('\n')
        print('----------ARTISTA----------')
        print("Escolha a opção")
        print("1 - Cadastrar Artista")
        print("2 - Editar Artista")
        print("3 - Listar Artistas")
        print("4 - Excluir Artista")
        print("5 - Página de Músicas")
        print("6 - Página de Álbuns")
        print("7 - Página de Playlists")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pegar_dados_artista(self):
        print("\n")
        print("-------- CADASTRAR NOVO ARTISTA ----------")
        nome = input("Nome: ")
        username = input("Username: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        return {"nome": nome, 'username': username, "email": email, "telefone": telefone}

    def mostrar_artista(self, dados_artista):
        print("\n")
        print("-------- DETALHES DO ARTISTA ----------")
        print("Nome:", dados_artista["nome"])
        print("Email:", dados_artista["email"])
        print("Telefone:", dados_artista["telefone"])

    def buscar_artista(self):
        print("\n")
        nome = input('Nome do artista que deseja buscar: ')
        return nome
    
    def mostrar_mensagem(self, msg):
        print("\n")
        print(msg)

    def pegar_dados_musica(self):
        print("\n")
        print("-------- CADASTRAR NOVA MÚSICA ----------")
        nome = input("Nome da música: ")
        letra = input("Letra da música: ")
        return {"nome": nome, "letra": letra}

    def mostrar_musicas(self, musicas):
        print("\n")
        print("-------- MÚSICAS DO ARTISTA ----------")
        if musicas:
            for musica in musicas:
                print(f"Nome: {musica.nome}, Letra: {musica.letra}")
        else:
            print("Nenhuma música cadastrada.")
