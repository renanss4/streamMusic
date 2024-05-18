class TelaArtista:

    def imprimir_opcoes(self):
        print('\n')
        print('---------- ARTISTA ----------')
        print("Escolha a opção:")
        print("1 - Cadastrar Artista")
        print("2 - Listar Artistas")
        print("3 - Editar Artista")
        print("4 - Excluir Artista")
        print("5 - Página de Músicas")
        print("6 - Página de Álbuns")
        print("7 - Página de Playlists")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 7:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 7.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_artista(self):
        print("\n")
        print("-------- CADASTRAR NOVO ARTISTA ----------")
        nome = input("Nome: ").strip()
        username = input("Username: ").strip()
        email = input("Email: ").strip()
        telefone = input("Telefone: ").strip()
        return {"nome": nome, 'username': username, "email": email, "telefone": telefone}

    def mostrar_artistas(self, artistas_dados):
        print("\n")
        print("-------- DETALHES DO ARTISTA ----------")
        for dados_artista in artistas_dados:
            print("Nome:", dados_artista["nome"])
            print("Username:", dados_artista["username"])
            print("Email:", dados_artista["email"])
            print("Telefone:", dados_artista["telefone"])
            print('--------------------------------')

    def buscar_artista(self):
        print("\n")
        nome = input('Nome do artista que deseja buscar: ').strip()
        return nome
    
    def mostrar_mensagem(self, msg):
        print("\n")
        print(msg)

    def pegar_dados_musica(self):
        print("\n")
        print("-------- CADASTRAR NOVA MÚSICA ----------")
        nome = input("Nome da música: ").strip()
        letra = input("Letra da música: ").strip()
        return {"nome": nome, "letra": letra}

    def mostrar_musicas(self, musicas):
        print("\n")
        print("-------- MÚSICAS DO ARTISTA ----------")
        if musicas:
            for musica in musicas:
                print(f"Nome: {musica['nome']}, Letra: {musica['letra']}")
        else:
            print("Nenhuma música cadastrada.")
