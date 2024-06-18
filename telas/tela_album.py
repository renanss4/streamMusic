import PySimpleGUI as sg # type: ignore

class TelaAlbum:
    def __init__(self):
        self.__window = None

    def imprimir_opcoes(self):
        """
        Mostra as opções disponíveis para o usuário e retorna a escolha.
        """
        self.init_components()
        while True:
            event, values = self.__window.read()
            if event in (None, 'Cancelar'):
                opcao = 0
                break
            if event == 'Confirmar':
                for key, value in values.items():
                    if value:
                        opcao = int(key)
                        break
                if 0 <= opcao <= 4:
                    break
                else:
                    sg.popup('Opção inválida! Escolha uma opção entre 0 e 4.')
        self.__window.close()
        return opcao

    def pegar_dados_album(self):
        """
        Solicita e retorna os dados de um álbum (nome e descrição).
        """
        layout = [
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Text('Descrição'), sg.InputText(key='descricao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Cadastrar/Editar Álbum', layout)
        event, values = window.read()
        window.close()
        if event == 'Confirmar':
            return values
        return None
    
    def mostrar_albuns(self, albuns_dados):
        """
        Mostra os detalhes dos álbuns cadastrados.
        """
        layout = [
            [sg.Text('Detalhes dos Álbuns Cadastrados', font=("Helvetica", 15))],
            [sg.Multiline('\n'.join([f"Nome: {album['nome']}\nDescrição: {album['descricao']}\n" for album in albuns_dados]), size=(50, 10))],
            [sg.Button('Ok')]
        ]
        window = sg.Window('Álbuns Cadastrados', layout)
        window.read()
        window.close()

    def buscar_album(self):
        """
        Solicita o nome do álbum que deseja buscar.
        """
        layout = [
            [sg.Text('Nome do álbum que deseja buscar'), sg.InputText(key='nome')],
            [sg.Button('Buscar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Buscar Álbum', layout)
        event, values = window.read()
        window.close()
        if event == 'Buscar':
            return values['nome']
        return None
    
    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        sg.popup(msg)

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('ÁLBUM', font=("Helvetica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
            [sg.Radio('Cadastrar Álbum', "RD1", key='1')],
            [sg.Radio('Listar Álbuns', "RD1", key='2')],
            [sg.Radio('Editar Álbum', "RD1", key='3')],
            [sg.Radio('Excluir Álbum', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Álbum').Layout(layout)
