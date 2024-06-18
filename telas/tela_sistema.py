import PySimpleGUI as sg # type: ignore

class TelaSistema:
    def __init__(self):
        self.__window = None

    def imprimir_opcoes(self):
        """
        Mostra as opções disponíveis para o usuário e retorna a escolha.
        """
        self.init_components()
        while True:
            event, values = self.__window.read()
            if event in (None, 'Cancelar'):  # Usuário clicou no botão Cancelar ou fechou a janela
                opcao = 0
                break
            if event == 'Confirmar':  # Usuário clicou no botão Confirmar
                for key, value in values.items():
                    if value:
                        opcao = int(key)
                        break
                if 0 <= opcao <= 3:
                    break
                else:
                    sg.popup('Opção inválida! Escolha uma opção entre 0 e 3.')
        self.__window.close()
        return opcao

    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        sg.popup(msg)

    def init_components(self):
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

