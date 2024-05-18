from datetime import datetime

class TelaContrato:

    def imprimir_opcoes(self):
        print('\n')
        print('---------- CONTRATO ----------')
        print("Escolha a opção:")
        print("1 - Cadastrar Contrato")
        print("2 - Listar Contratos")
        print("3 - Excluir Contrato")
        print("4 - Buscar Contratos por Artista")
        print("5 - Buscar Contratos por Gravadora")
        print("6 - Buscar Contratos pelo Número")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 6:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 6.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_contrato(self):
        print('\n')
        print("-------- CADASTRAR NOVO CONTRATO ----------")
        numero = int(input('Número: '))
        artista = input("Artista: ")
        gravadora = input('Gravadora: ')
        
        while True:
            data_inicio_str = input('Data de Início (YYYY-MM-DD): ')
            try:
                data_inicio = datetime.strptime(data_inicio_str, '%Y-%m-%d').date()
                break
            except ValueError:
                print("Data inválida! Por favor, use o formato YYYY-MM-DD.")
        
        while True:
            data_fim_str = input('Data de Fim (YYYY-MM-DD): ')
            try:
                data_fim = datetime.strptime(data_fim_str, '%Y-%m-%d').date()
                break
            except ValueError:
                print("Data inválida! Por favor, use o formato YYYY-MM-DD.")
        
        return {
            'numero': numero, 
            "artista": artista, 
            "gravadora": gravadora, 
            "data_inicio": data_inicio, 
            "data_fim": data_fim
        }

    def mostrar_contratos(self, contratos_dados):
        print('\n')
        print('-------- DETALHES DOS CONTRATOS ----------')
        for dados_contrato in contratos_dados:
            print('Número:', dados_contrato['numero'])
            print('Artista:', dados_contrato['artista'])
            print('Gravadora:', dados_contrato['gravadora'])
            print('Data de Início:', dados_contrato['data_inicio'])
            print('Data de Fim:', dados_contrato['data_fim'])
            print('--------------------------------')

    def buscar_por_artista(self):
        artista = input('Nome do artista: ')
        return artista

    def buscar_por_gravadora(self):
        gravadora = input('Nome da gravadora: ')
        return gravadora

    def buscar_por_numero(self):
        numero = int(input('Número do contrato que deseja buscar: '))
        return numero

    def mostrar_mensagem(self, msg):
        print('\n' + msg + '\n')
