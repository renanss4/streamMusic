class TelaUsuario:

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def imprimir_opcoes(self):
        print("\n")
        print('----------USUÁRIO----------')
        print("Escolha a opção")
        print("1 - Cadastrar Usuário")
        print("2 - Editar Usuário")
        print("3 - Listar Usuários")
        print("4 - Excluir Usuário")
        # print("5 - Seguir Artista")
        # print("6 - Deixar de Seguir Artista")
        # print("7 - Mostrar Artistas Seguidos")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pegar_dados_usuario(self):
        print("\n")
        print("-------- CADASTRAR NOVO USUÁRIO ----------")
        nome = input("Nome: ")
        username = input('username: ')
        email = input("Email: ")
        telefone = input("Telefone: ")
        return {"nome": nome, "username": username, "email": email, "telefone": telefone}

    def mostrar_usuario(self, dados_usuario):
        print("\n")
        print("-------- DETALHES DO USUÁRIO ----------")
        print("Nome:", dados_usuario["nome"])
        print("Username:", dados_usuario["username"])
        print("Email:", dados_usuario["email"])
        print("Telefone:", dados_usuario["telefone"])

    def buscar_usuario(self):
        print("\n")
        username = input('Username do usuário que deseja buscar: ')
        return username
    
    def mostrar_mensagem(self, msg):
        print("\n")
        print(msg)

    def pegar_artista(self):
        print("\n")
        artista = input("Nome do artista: ")
        return artista

    def mostrar_artistas_seguidos(self, artistas_seguidos):
        print("\n")
        print("-------- ARTISTAS SEGUIDOS ----------")
        if artistas_seguidos:
            for artista in artistas_seguidos:
                print(artista)
        else:
            print("Nenhum artista seguido.")
