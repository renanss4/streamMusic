class TelaMusica:
    def imprimir_opcoes(self):
        print('\n---------- MÚSICA ----------')
        print("Escolha a opção:")
        print("1 - Cadastrar Música")
        print("2 - Listar Músicas")
        print("3 - Editar Música")
        print("4 - Excluir Música")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 4:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 4.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_musica(self):
        print('\n-------- CADASTRAR/EDITAR MÚSICA ----------')
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            else:
                print("Nome não pode ser vazio!")

        letra = input("Letra da música: ").strip()
        return {'nome': nome, 'letra': letra}

    def mostrar_musicas(self, musicas_dados):
        print('\n-------- DETALHES DAS MÚSICAS CADASTRADAS ----------')
        for dados_musica in musicas_dados:
            print('Nome:', dados_musica['nome'])
            print('Letra:', dados_musica['letra'])
            print('--------------------------------')

    def buscar_musica(self):
        nome = input('Nome da música que deseja buscar: ').strip()
        return nome

    def mostrar_mensagem(self, msg):
        print('\n' + msg + '\n')
