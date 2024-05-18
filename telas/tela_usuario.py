class TelaUsuario:

    def imprimir_opcoes(self):
        print('\n')
        print('---------- USUÁRIO ----------')
        print("Escolha a opção:")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Editar Usuário")
        print("4 - Excluir Usuário")
        print("5 - Página de Playlists")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 5:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 5.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_usuario(self):
        print('\n')
        print("-------- CADASTRAR NOVO USUÁRIO ----------")
        nome = input("Nome: ")
        username = input('Username: ')
        email = input("Email: ")
        telefone = input("Telefone: ")
        return {"nome": nome, "username": username, "email": email, "telefone": telefone}

    def mostrar_usuarios(self, usuarios_dados):
        print('\n')
        print('-------- DETALHES DOS USUÁRIOS ----------')
        for dados_usuario in usuarios_dados:
            print('Nome:', dados_usuario['nome'])
            print('Username:', dados_usuario['username'])
            print('Email:', dados_usuario['email'])
            print('Telefone:', dados_usuario['telefone'])
            print('--------------------------------')

    def buscar_usuario(self):
        username = input('Username do usuário que deseja buscar: ')
        return username

    def mostrar_mensagem(self, msg):
        print('\n' + msg + '\n')
