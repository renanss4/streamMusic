class TelaContrato:

    def imprimir_opcoes(self):
        print('\n')
        print('---------- CONTRATO ----------')
        print("Escolha a opção:")
        print("1 - Cadastrar Contrato")
        print("2 - Listar Contratos")
        print("3 - Excluir Contrato")
        print("0 - Retornar")

        while True:
            try:
                opcao = int(input("Escolha a opção: "))
                if 0 <= opcao <= 3:
                    return opcao
                else:
                    print("Opção inválida! Escolha uma opção entre 0 e 3.")
            except ValueError:
                print("Entrada inválida! Digite um número.")

    def pegar_dados_contrato(self):
        print('\n')
        print("-------- CADASTRAR NOVO CONTRATO ----------")
        numero = int(input('Número: '))
        artista = input("Artista: ")
        gravadora = input('Gravadora: ')
        return {'numero': numero, "artista": artista, "gravadora": gravadora}

    def mostrar_contratos(self, contratos_dados):
        print('\n')
        print('-------- DETALHES DOS CONTRATOS ----------')
        for dados_contrato in contratos_dados:
            print('Número:', dados_contrato['numero'])
            print('Artista:', dados_contrato['artista'])
            print('Gravadora:', dados_contrato['gravadora'])
            print('--------------------------------')

    def buscar_contrato(self):
        artista = input('Nome do artista com contrato que deseja buscar: ')
        return artista

    def mostrar_mensagem(self, msg):
        print('\n' + msg + '\n')
