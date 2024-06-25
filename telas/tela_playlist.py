import PySimpleGUI as sg

class TelaPlaylist:
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

    def pegar_dados_playlist(self):
        """
        Solicita e retorna os dados de uma nova playlist.
        """
        layout = [
            [sg.Text('CADASTRAR/EDITAR PLAYLIST', font=("Helvetica", 15))],
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Text('Descrição'), sg.Multiline(key='descricao')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Cadastrar/Editar Playlist', layout)
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                values = None
                break
            if event == 'Confirmar':
                nome = values['nome'].strip()
                descricao = values['descricao'].strip()
                if nome:
                    values = {'nome': nome, 'descricao': descricao}
                    break
                else:
                    sg.popup("Nome não pode ser vazio!")
        window.close()
        return values

    def buscar_playlist(self):
        """
        Solicita e retorna o nome de uma playlist.
        """
        layout = [
            [sg.Text('BUSCAR PLAYLIST', font=("Helvetica", 15))],
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Buscar Playlist', layout)
        event, values = window.read()
        window.close()
        if event == 'Confirmar':
            return values['nome'].strip()
        return None

    def mostrar_playlists(self, playlists_dados):
        """
        Mostra os detalhes das playlists cadastradas.
        """
        layout = [
            [sg.Text('PLAYLISTS CADASTRADAS', font=("Helvetica", 15))],
            [sg.Multiline('\n'.join([f"Nome: {playlist['nome']}\nDescrição: {playlist['descricao']}\n" for playlist in playlists_dados]), size=(60, 10))],
            [sg.Button('Ok')]
        ]
        window = sg.Window('Playlists Cadastradas', layout)
        window.read()
        window.close()

    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        sg.popup(msg)

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('PLAYLIST', font=("Helvetica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
            [sg.Radio('Cadastrar Playlist', "RD1", key='1')],
            [sg.Radio('Listar Playlists', "RD1", key='2')],
            [sg.Radio('Editar Playlist', "RD1", key='3')],
            [sg.Radio('Excluir Playlist', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Playlist').Layout(layout)
