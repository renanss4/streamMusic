from datetime import datetime


class TelaArtista:

    def imprimir_opcoes(self):
        print('\n---------- ARTISTA ----------')
        print("Escolha a opção:")
        print("1 - Cadastrar Artista")
        print("2 - Listar Artistas")
        print("3 - Editar Artista")
        print("4 - Excluir Artista")
        print("5 - Página de Músicas")
        print("6 - Página de Álbuns")
        print("7 - Página de Playlists")
        print("8 - Página de Contratos")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 8:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 8.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_artista(self):
        print("\n-------- CADASTRAR NOVO ARTISTA ----------")
        nome = input("Nome: ").strip()
        email = input("Email: ").strip()
        telefone = input("Telefone: ").strip()

        while True:
            try:
                data_nascimento = input('Data de Nascimento (YYYY-MM-DD): ')
                data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d').date()
                break
            except ValueError:
                print("Data inválida! Por favor, insira no formato YYYY-MM-DD.")

        return {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "data_nascimento": data_nascimento
        }

    def mostrar_artistas(self, artistas_dados):
        print("\n-------- DETALHES DO ARTISTA ----------")
        for dados_artista in artistas_dados:
            print("Nome:", dados_artista["nome"])
            print("Email:", dados_artista["email"])
            print("Telefone:", dados_artista["telefone"])
            print('Data de Nascimento:', dados_artista['data_nascimento'])
            print('--------------------------------')
   
    def mostrar_mensagem(self, msg):
        print('\n' + msg + '\n')
