class TelaArtista:

    def imprimir_opcoes(self):
        print('\n---------- ARTISTA ----------')
        print("Escolha a opção:")
        print("1 - Cadastrar Artista")
        print("2 - Listar Artistas")
        print("3 - Editar Artista")
        print("4 - Excluir Artista")
        print("5 - Página de Músicas")
        print("6 - Página de Álbuns")
        print("7 - Página de Playlists")
        print("8 - Página de Contratos")
        print("9 - Seguir Artista")
        print("10 - Deixar de Seguir Artista")
        print("11 - Ver Artistas Seguidos")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 11:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 11.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_artista(self):
        print("----- Cadastrar Artista -----")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        data_nascimento = input("Data de Nascimento: ")
        return {"nome": nome, "email": email, "telefone": telefone, "data_nascimento": data_nascimento}

    def pegar_nome_artista(self):
        nome = input("Nome do Artista: ")
        return nome

    def mostrar_artistas(self, artistas):
        print("----- Lista de Artistas -----")
        for artista in artistas:
            print(f"Nome: {artista['nome']}")
            print(f"Email: {artista['email']}")
            print(f"Telefone: {artista['telefone']}")
            print(f"Data de Nascimento: {artista['data_nascimento']}")
            print("--------------------------")

    def buscar_artista(self):
        print("----- Buscar Artista -----")
        nome = input("Nome do artista: ")
        return nome

    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)

    def imprimir_opcoes(self):
        print("0: Retornar")
        print("1: Cadastrar Artista")
        print("2: Listar Artistas")
        print("3: Editar Artista")
        print("4: Remover Artista")
        print("5: Cadastrar Música")
        print("6: Ver Músicas do Artista")
        opcao = int(input("Escolha uma opção: "))
        return opcao
