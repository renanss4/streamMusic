class TelaAlbum:

    def imprimir_opcoes(self):
        print('\n')
        print('----------ÁLBUM----------')
        print("Escolha a opção")
        print("1 - Cadastrar Álbum")
        print("2 - Editar Álbum")
        print("3 - Listar Álbuns")
        print("4 - Excluir Álbum")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao
    
    def pegar_dados_album(self):
        print('\n')
        print("-------- CADASTRAR NOVA ÁLBUM ----------")
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        musicas = input('Músicas: ')
        return {'nome': nome, 'descricao': descricao, 'musicas': musicas}
    
    def mostrar_album(self, dados_album):
        print('\n')
        print("-------- DETALHES DA ÁLBUM ----------")
        print("Nome:", dados_album["nome"])
        print("Descrição:", dados_album["descricao"])
        print('Músicas: ', dados_album['musicas'])

    def buscar_album(self):
        nome = input('Nome da álbum que deseja buscar: ')
        return nome
    
    def mostrar_mensagem(self, msg):
        print(msg)

        