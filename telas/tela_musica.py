class TelaMusica:
    def imprimir_opcoes(self):
        print()
        print("################################")
        print('# ---------- MÚSICA ---------- #')
        print("# Escolha a opção:             #")
        print("# 1 - Cadastrar Música         #")
        print("# 2 - Listar Músicas           #")
        print("# 3 - Editar Música            #")
        # print("4 - Adicionar Música à Playlist ou Álbum")
        # print("5 - Remover Música de Playlist ou Álbum")
        print("# 4 - Excluir Música           #")
        print("# 0 - Retornar                 #")
        print("################################")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 6:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 6.")
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

    # def pegar_dados_adicao_musica(self):
    #     print('\n-------- ADICIONAR MÚSICA À PLAYLIST/ÁLBUM ----------')
    #     while True:
    #         nome_musica = input("Nome da música: ").strip()
    #         if nome_musica:
    #             break
    #         else:
    #             print("Nome da música não pode ser vazio!")

    #     while True:
    #         tipo = input("Você deseja adicionar a música a uma playlist (1) ou álbum (2)? ").strip()
    #         if tipo in ['1', '2']:
    #             break
    #         else:
    #             print("Entrada inválida! Digite '1' para playlist ou '2' para álbum.")

    #     while True:
    #         nome_playlist_album = input("Nome da playlist/álbum: ").strip()
    #         if nome_playlist_album:
    #             break
    #         else:
    #             print("Nome da playlist/álbum não pode ser vazio!")

    #     return {'nome_musica': nome_musica, 'tipo': tipo, 'nome_playlist_album': nome_playlist_album}
    
    # def pegar_dados_remocao_musica(self):
    #     print('\n-------- REMOVER MÚSICA DE PLAYLIST/ÁLBUM ----------')
    #     while True:
    #         nome_musica = input("Nome da música: ").strip()
    #         if nome_musica:
    #             break
    #         else:
    #             print("Nome da música não pode ser vazio!")

    #     while True:
    #         tipo = input("Você deseja remover a música de uma playlist (1) ou álbum (2)? ").strip()
    #         if tipo in ['1', '2']:
    #             break
    #         else:
    #             print("Entrada inválida! Digite '1' para playlist ou '2' para álbum.")

    #     while True:
    #         nome_playlist_album = input("Nome da playlist/álbum: ").strip()
    #         if nome_playlist_album:
    #             break
    #         else:
    #             print("Nome da playlist/álbum não pode ser vazio!")

    #     return {'nome_musica': nome_musica, 'tipo': tipo, 'nome_playlist_album': nome_playlist_album}

    def mostrar_mensagem(self, msg):
        print('\n')
        print('\n' + msg + '\n')