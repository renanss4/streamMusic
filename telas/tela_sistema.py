class TelaSistema:
    def imprimir_opcoes(self):
        """
        Mostra as opções disponíveis para o usuário e retorna a escolha.
        """
        print('\n')
        print("################################")
        print("# --------StreamMusic--------- #")
        print("# Escolha sua opção            #")
        print("#                              #")
        print("# 1 - Usuários                 #")
        print("# 2 - Artistas                 #")
        print("# 3 - Gravadora                #")
        print("# 0 - Encerrar                 #")
        print("################################")

        while True:
            try:
                opcao = int(input('\n' + "Escolha uma opção: "))
                if 0 <= opcao <= 3:
                    return opcao
                else:
                    print('\n' + 'Opção inválida! Escolha uma opção entre 0 e 3.' + '\n')
            except ValueError:
                print('\n' + "Entrada inválida! Digite um número." + '\n')
    
    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        print('\n')
        print('\n' + msg + '\n')
