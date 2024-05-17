class TelaMusica:

    def imprimir_opcoes(self):
        print('\n')
        print('----------MÚSICA----------')
        print("Escolha a opção")
        print("1 - Cadastrar Música")
        print("2 - Editar Música")
        print("3 - Listar Músicas")
        print("4 - Excluir Música")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pegar_dados_musica(self):
        print('\n')
        print("-------- CADASTRAR NOVA MÚSICA ----------")
        nome = input("Nome: ")
        letra = input("Letra: ")
        return {'nome': nome, 'letra': letra}
    
    def mostrar_musica(self, dados_musica):
        print('\n')
        print("-------- DETALHES DA MÚSICA ----------")
        print("Nome:", dados_musica["nome"])
        print("Letra:", dados_musica["letra"])

    def buscar_musica(self):
        nome = input('Nome da música que deseja buscar: ')
        return nome
    
    def mostrar_mensagem(self, msg):
        print(msg)

        