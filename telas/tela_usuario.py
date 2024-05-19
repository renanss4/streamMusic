from datetime import datetime

class TelaUsuario:

    def imprimir_opcoes(self):
        print('\n')
        print('---------- USUÁRIO ----------')
        print("Escolha a opção:")
        print("1 - Cadastrar Usuário")
        print("2 - Listar Usuários")
        print("3 - Editar Usuário")
        print("4 - Excluir Usuário")
        print("5 - Página de Playlists")
        print("6 - Seguir Artista")
        print("7 - Deixar de Seguir Artista")
        print("8 - Ver Artistas Seguidos")
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

    def pegar_dados_usuario(self):
        print('\n')
        print("-------- CADASTRAR NOVO USUÁRIO ----------")

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

    def mostrar_usuarios(self, usuarios_dados):
        print('\n')
        print('-------- DETALHES DOS USUÁRIOS ----------')
        for dados_usuario in usuarios_dados:
            print('Nome:', dados_usuario['nome'])
            print('Email:', dados_usuario['email'])
            print('Telefone:', dados_usuario['telefone'])
            print('Data de Nascimento:', dados_usuario['data_nascimento'])
            print('--------------------------------')

    def buscar_usuario(self):
        nome = input('Nome do usuário que deseja buscar: ').strip()
        return nome

    def pegar_nome_artista(self):
        nome = input('Nome do artista: ').strip()
        return nome

    def mostrar_artistas_seguidos(self, artistas_dados):
        print('\n')
        print('-------- ARTISTAS SEGUIDOS ----------')
        for dados_artista in artistas_dados:
            print('Nome:', dados_artista['nome'])
            print('Email:', dados_artista['email'])
            print('Telefone:', dados_artista['telefone'])
            print('Data de Nascimento:', dados_artista['data_nascimento'])
            print('--------------------------------')

    def mostrar_mensagem(self, msg):
        print('\n')
        print('\n' + msg + '\n')