class TelaArtista:
    def __init__(self):
        pass

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
