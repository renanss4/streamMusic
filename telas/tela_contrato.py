from datetime import datetime


class TelaContrato:

    def imprimir_opcoes(self):
        """
        Mostra as opções disponíveis para o usuário e retorna a escolha.
        """
        print()
        print("######################################")
        print('# ---------- CONTRATO ----------     #')
        print("# Escolha a opção:                   #")
        print("# 1 - Cadastrar Contrato             #")
        print("# 2 - Listar Contratos               #")
        print("# 3 - Buscar Contratos por Artista   #")
        print("# 4 - Buscar Contratos por Gravadora #")
        print("# 5 - Buscar Contrato por Número     #")
        print("# 0 - Retornar                       #")
        print("######################################")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 5:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 5.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_contrato(self):
        """
        Solicita e retorna os dados de um novo contrato.
        """
        print('\n-------- CADASTRAR NOVO CONTRATO ----------')
        while True:
            numero = input("Número: ").strip()
            if numero.isdigit():
                break
            else:
                print("Número deve conter apenas números!")
        
        while True:
            artista = input("Artista: ").strip()
            if artista:
                break
            else:
                print("Nome do artista não pode ser vazio!")
        
        while True:
            gravadora = input('Gravadora: ').strip()
            if gravadora:
                break
            else:
                print("Nome da gravadora não pode ser vazio!")

        while True:
            try:
                data_inicio = input('Data de Início (YYYY-MM-DD): ')
                data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
                break
            except ValueError:
                print("Data inválida! Por favor, insira no formato YYYY-MM-DD.")
        
        while True:
            try:
                data_fim = input('Data de Fim (YYYY-MM-DD): ')
                data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
                if data_inicio > data_fim:
                    print("A data de início não pode ser maior que a data de fim!")
                    continue
                break
            except ValueError:
                print("Data inválida! Por favor, insira no formato YYYY-MM-DD.")
        
        return {'numero': numero, "artista": artista, "gravadora": gravadora, 'data_inicio': data_inicio, 'data_fim': data_fim}

    def mostrar_contratos(self, contratos_dados):
        """
        Mostra os detalhes dos contratos cadastrados.
        """
        print('\n-------- DETALHES DOS CONTRATOS ----------')
        for dados_contrato in contratos_dados:
            print('Número:', dados_contrato['numero'])
            print('Artista:', dados_contrato['artista'])
            print('Gravadora:', dados_contrato['gravadora'])
            print('Data de Início:', dados_contrato['data_inicio'])
            print('Data de Fim:', dados_contrato['data_fim'])
            print('--------------------------------')

    def buscar_por_artista(self):
        """
        Solicita o nome do artista para buscar contratos associados a ele.
        """
        artista = input('Nome do artista com contrato que deseja buscar: ')
        return artista

    def buscar_por_gravadora(self):
        """
        Solicita o nome da gravadora para buscar contratos associados a ela.
        """
        gravadora = input('Nome da gravadora com contrato que deseja buscar: ')
        return gravadora

    def buscar_por_numero(self):
        """
        Solicita o número do contrato para buscar um contrato específico.
        """
        while True:
            try:
                numero = int(input('Número do contrato que deseja buscar: '))
                return numero
            except ValueError:
                print("Entrada inválida! Por favor, insira um número.")

    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        print('\n' + msg + '\n')
