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
        # print("8 - Página de Contratos")
        print("8 - Seguir Artista")
        print("9 - Deixar de Seguir Artista")
        print("10 - Ver Artistas Seguidos")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 10:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_artista(self):
        print("\n-------- CADASTRAR NOVO ARTISTA ----------")
        
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

    def pegar_nome_artista(self):
        nome = input('Nome do artista: ').strip()
        return nome

    def mostrar_mensagem(self, msg):
        print('\n' + msg + '\n')
