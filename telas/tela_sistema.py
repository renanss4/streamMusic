class TelaSistema:
    def imprimir_opcoes(self):
        print("################################")
        print("# --------StreamMusic--------- #")
        print("# Escolha sua opção            #")
        print("#                              #")
        print("# 1 - Usuários                 #")
        print("# 2 - Artistas                 #")
        print("# 0 - Encerrar                 #")
        print("################################")

        opcao = int(input("Escolha a opção: "))
        return opcao