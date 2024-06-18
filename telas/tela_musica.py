import PySimpleGUI as sg # type: ignore

class TelaMusica:
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

    def pegar_dados_musica(self):
        """
        Solicita e retorna os dados de uma nova música.
        """
        layout = [
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Text('Letra da Música'), sg.Multiline(key='letra')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Cadastrar/Editar Música', layout)
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                values = None
                break
            if event == 'Confirmar':
                nome = values['nome'].strip()
                letra = values['letra'].strip()
                if nome:
                    values = {'nome': nome, 'letra': letra}
                    break
                else:
                    sg.popup("Nome não pode ser vazio!")
        window.close()
        return values

    def mostrar_musicas(self, musicas_dados):
        """
        Mostra os detalhes das músicas cadastradas.
        """
        layout = [
            [sg.Text('Detalhes das Músicas Cadastradas', font=("Helvetica", 15))],
            [sg.Multiline('\n'.join([f"Nome: {musica['nome']}\nLetra: {musica['letra']}\n" for musica in musicas_dados]), size=(50, 10))],
            [sg.Button('Ok')]
        ]
        window = sg.Window('Músicas Cadastradas', layout)
        window.read()
        window.close()

    def buscar_musica(self):
        """
        Solicita o nome da música que deseja buscar.
        """
        layout = [
            [sg.Text('Nome da música que deseja buscar'), sg.InputText(key='nome')],
            [sg.Button('Buscar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Buscar Música', layout)
        event, values = window.read()
        window.close()
        if event == 'Buscar':
            return values['nome'].strip()
        return None

    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        sg.popup(msg)

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('MÚSICA', font=("Helvetica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
            [sg.Radio('Cadastrar Música', "RD1", key='1')],
            [sg.Radio('Listar Músicas', "RD1", key='2')],
            [sg.Radio('Editar Música', "RD1", key='3')],
            [sg.Radio('Excluir Música', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Música').Layout(layout)

