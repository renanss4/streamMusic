

class TelaGravadora:

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def imprimir_opcoes(self):
        print("\n")
        print('----------GRAVADORA----------')
        print("Escolha a opção")
        print("1 - Cadastrar Gravadora")
        print("2 - Editar Gravadora")
        print("3 - Listar Gravadoras")
        print("4 - Excluir Gravadora")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pegar_dados_gravadora(self):
        print("\n")
        print("-------- CADASTRAR NOVA GRAVADORA ----------")
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        telefone = input("Telefone: ")
        return {"nome": nome, "email": email, "senha": senha, "telefone": telefone}

    def mostrar_gravadora(self, dados_gravadora):
        print("\n")
        print("-------- DETALHES DA GRAVADORA ----------")
        print("Nome:", dados_gravadora["nome"])
        print("Email:", dados_gravadora["email"])
        print("Telefone:", dados_gravadora["telefone"])

    def buscar_gravadora(self):
        print("\n")
        username = input('Gravadora que deseja buscar: ')
        return username

    def editar_gravadora(self):
        print("\n")
        print("-------- EDITAR GRAVADORA ----------")
        nome = input("Novo nome da Gravadora: ")
        return {"nome": nome}
    
    def mostrar_mensagem(self, msg):
        print("\n")
        print(msg)
