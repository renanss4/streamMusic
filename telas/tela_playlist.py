import PySimpleGUI as sg # type: ignore
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class TelaPlaylist:
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
                    if 0 <= opcao <= 4:
                        break
                    else:
                        sg.popup('Opção inválida! Escolha uma opção entre 0 e 4.')
            return opcao
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro: {str(e)}")
        finally:
            if self.__window:
                self.__window.close()

    def pegar_dados_playlist(self):
        try:
            layout = [
                [sg.Text('CADASTRAR/EDITAR PLAYLIST', font=("Helvetica", 15))],
                [sg.Text('Nome'), sg.InputText(key='nome')],
                [sg.Text('Descrição'), sg.Multiline(key='descricao')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            window = sg.Window('Cadastrar/Editar Playlist', layout)
            values = None
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
            return values
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro: {str(e)}")
        finally:
            window.close()

    def buscar_playlist(self):
        try:
            layout = [
                [sg.Text('BUSCAR PLAYLIST', font=("Helvetica", 15))],
                [sg.Text('Nome'), sg.InputText(key='nome')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            window = sg.Window('Buscar Playlist', layout)
            event, values = window.read()
            if event == 'Confirmar':
                return values['nome'].strip()
            return None
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro: {str(e)}")
        finally:
            window.close()

    def mostrar_playlists(self, playlists_dados):
        try:
            layout = [
                [sg.Text('PLAYLISTS CADASTRADAS', font=("Helvetica", 15))],
                [sg.Multiline('\n'.join([f"Nome: {playlist['nome']}\nDescrição: {playlist['descricao']}\n" for playlist in playlists_dados]), size=(60, 10))],
                [sg.Button('Ok')]
            ]
            window = sg.Window('Playlists Cadastradas', layout)
            window.read()
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro: {str(e)}")
        finally:
            window.close()

    def mostrar_mensagem(self, msg):
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
