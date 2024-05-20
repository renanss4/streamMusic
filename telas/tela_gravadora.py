class TelaGravadora:

    def imprimir_opcoes(self):
        """
        Mostra as opções disponíveis para o usuário e retorna a escolha.
        """
        print()
        print("###################################")
        print("# ---------- GRAVADORA ---------- #")
        print("# Escolha a opção                 #")
        print("# 1 - Cadastrar Gravadora         #")
        print("# 2 - Listar Gravadoras           #")
        print("# 3 - Editar Gravadora            #")
        print("# 4 - Excluir Gravadora           #")
        print("# 5 - Página de Contratos         #")
        print("# 0 - Retornar                    #")
        print("###################################")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 5:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 5.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_gravadora(self):
        """
        Solicita e retorna os dados de uma nova gravadora.
        """
        print("\n-------- CADASTRAR NOVA GRAVADORA ----------")
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            else:
                print("Nome não pode ser vazio!")

        while True:
            email = input("Email: ").strip()
            if email:
                break
            else:
                print("Email não pode ser vazio!")

        while True:
            telefone = input("Telefone: ").strip()
            if telefone.isdigit():
                break
            else:
                print("Telefone deve conter apenas números!")
        return {"nome": nome, "email": email, "telefone": telefone}

    def mostrar_gravadoras(self, gravadoras_dados):
        """
        Mostra os detalhes das gravadoras cadastradas.
        """
        print("\n-------- DETALHES DAS GRAVADORAS ----------")
        for gravadora in gravadoras_dados:
            print("Nome:", gravadora["nome"])
            print("Email:", gravadora["email"])
            print("Telefone:", gravadora["telefone"])
            print('--------------------------------')


    def buscar_gravadora(self):
        """
        Solicita o nome da gravadora para buscar suas informações.
        """
        print("\n")
        nome = input('Nome da gravadora que deseja buscar: ').strip()
        return nome

    def editar_gravadora(self):
        """
        Solicita o novo nome da gravadora para edição.
        """
        print("\n-------- EDITAR GRAVADORA ----------")
        nome = input("Novo nome da gravadora: ").strip()
        return {"nome": nome}
    
    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        print('\n' + msg + '\n')
