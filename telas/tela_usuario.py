

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
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pegar_dados_usuario(self):
        print("\n")
        print("-------- CADASTRAR NOVO USUÁRIO ----------")
        nome = input("Nome: ")
        identificador = input('Identificador: ')
        email = input("Email: ")
        senha = input("Senha: ")
        telefone = input("Telefone: ")
        return {"nome": nome, "identificador": identificador, "email": email, "senha": senha, "telefone": telefone}

    def mostrar_usuario(self, dados_usuario):
        print("\n")
        print("-------- DETALHES DO USUÁRIO ----------")
        print("Nome:", dados_usuario["nome"])
        print("Identificador:", dados_usuario["identificador"])
        print("Email:", dados_usuario["email"])
        print("Telefone:", dados_usuario["telefone"])

    def buscar_usuario(self):
        print("\n")
        identificador = input('Identificador do usuário que deseja buscar: ')
        return identificador
    
    def mostrar_mensagem(self, msg):
        print("\n")
        print(msg)
