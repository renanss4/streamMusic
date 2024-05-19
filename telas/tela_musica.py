class TelaMusica:
    def __init__(self):
        pass

    def pegar_dados_musica(self):
        print("----- Cadastrar Música -----")
        nome = input("Nome da música: ")
        letra = input("Letra da música: ")
        return {"nome": nome, "letra": letra}

    def mostrar_musicas(self, musicas):
        print("----- Lista de Músicas -----")
        for musica in musicas:
            print(f"Nome: {musica['nome']}")
            print(f"Letra: {musica['letra']}")
            print("--------------------------")

    def buscar_musica(self):
        print("----- Buscar Música -----")
        nome = input("Nome da música: ")
        return nome

    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)

    def imprimir_opcoes(self):
        print("0: Retornar")
        print("1: Cadastrar Música")
        print("2: Listar Músicas")
        print("3: Editar Música")
        print("4: Remover Música")
        opcao = int(input("Escolha uma opção: "))
        return opcao
