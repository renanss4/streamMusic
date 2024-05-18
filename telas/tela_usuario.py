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
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 5:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 5.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_usuario(self):
        print('\n')
        print("-------- CADASTRAR NOVO USUÁRIO ----------")
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        
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

    def mostrar_mensagem(self, msg):
        print('\n' + msg + '\n')
