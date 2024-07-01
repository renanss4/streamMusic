import PySimpleGUI as sg  # type: ignore
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class TelaSistema:
    def __init__(self):
        self.__window = None

    def imprimir_opcoes(self):
        try:
            self.init_components()
            opcao = None
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
                    if 0 <= opcao <= 3:
                        break
                    else:
                        sg.popup('Opção inválida! Escolha uma opção entre 0 e 3.')
            return opcao
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro: {str(e)}")
        finally:
            if self.__window:
                self.__window.close()

    def mostrar_mensagem(self, msg):
        try:
            sg.popup(msg)
        except Exception as e:
            sg.popup(f"Ocorreu um erro ao tentar mostrar a mensagem: {str(e)}")

    def init_components(self):
        try:
            sg.ChangeLookAndFeel('DarkTeal4')
            layout = [
                [sg.Text('Bem vindo ao StreamMusic!', font=("Helvetica", 25))],
                [sg.Text('Escolha sua opção', font=("Helvetica", 15))],
                [sg.Radio('Usuários', "RD1", key='1')],
                [sg.Radio('Artistas', "RD1", key='2')],
                [sg.Radio('Gravadora', "RD1", key='3')],
                [sg.Radio('Encerrar', "RD1", key='0')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('StreamMusic').Layout(layout)
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro ao inicializar os componentes da tela: {str(e)}")
