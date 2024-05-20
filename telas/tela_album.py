class TelaAlbum:

    def imprimir_opcoes(self):
        """
        Mostra as opções disponíveis para o usuário e retorna a escolha.
        """
        print()
        print('################################')
        print('# ---------- ÁLBUM ----------  #')
        print("# Escolha a opção:             #")
        print("# 1 - Cadastrar Álbum          #")
        print("# 2 - Listar Álbuns            #")
        print("# 3 - Editar Álbum             #")
        print("# 4 - Excluir Álbum            #")
        print("# 0 - Retornar                 #")
        print('################################')

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 4:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 4.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_album(self):
        """
        Solicita e retorna os dados de um álbum (nome e descrição).
        """
        print('\n-------- CADASTRAR/EDITAR ÁLBUM ----------')
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            else:
                print('Nome não pode ser vazio')
        descricao = input("Descrição: ").strip()
        return {'nome': nome, 'descricao': descricao}
    
    def mostrar_albuns(self, albuns_dados):
        """
        Mostra os detalhes dos álbuns cadastrados.
        """
        print('\n-------- DETALHES DOS ÁLBUNS CADASTRADOS ----------')
        for dados_album in albuns_dados:
            print('Nome:', dados_album['nome'])
            print('Descrição:', dados_album['descricao'])
            print('--------------------------------')

    def buscar_album(self):
        """
        Solicita o nome do álbum que deseja buscar.
        """
        print('\n')
        nome = input('Nome do álbum que deseja buscar: ').strip()
        return nome
    
    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        print('\n' + msg + '\n')
