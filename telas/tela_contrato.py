

class TelaContrato:

    # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def imprimir_opcoes(self):
        print("\n")
        print('----------CONTRATO----------')
        print("Escolha a opção")
        print("1 - Cadastrar Contrato")
        print("2 - Listar Contratos")
        print("3 - Excluir Contrato")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pegar_dados_contrato(self):
        print("\n")
        print("-------- CADASTRAR NOVO CONTRATO ----------")
        numero = int(input('Número: '))
        artista = input("Artista: ")
        gravadora = input('Gravadora: ')
        return {'numero': numero, "artista": artista, "gravadora": gravadora}

    def mostrar_contrato(self, dados_contrato):
        print("\n")
        print("-------- DETALHES DO CONTRATO ----------")
        print('Número:', dados_contrato['numero'])
        print("Artista:", dados_contrato["artista"])
        print("Gravadora:", dados_contrato["gravadora"])

    def buscar_contrato(self):
        print("\n")
        artista = input('Artista com o contrato que deseja buscar: ')
        return artista

    def mostrar_mensagem(self, msg):
        print("\n")
        print(msg)
