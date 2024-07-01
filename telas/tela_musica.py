import PySimpleGUI as sg # type: ignore
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class TelaMusica:
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

    def pegar_dados_musica(self):
        try:
            layout = [
                [sg.Text('Nome'), sg.InputText(key='nome')],
                [sg.Text('Letra da Música'), sg.Multiline(key='letra')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            window = sg.Window('Cadastrar/Editar Música', layout)
            values = None
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
            return values
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro: {str(e)}")
        finally:
            window.close()

    def mostrar_musicas(self, musicas_dados):
        try:
            layout = [
                [sg.Text('Detalhes das Músicas Cadastradas', font=("Helvetica", 15))],
                [sg.Multiline('\n'.join([f"Nome: {musica['nome']}\nLetra: {musica['letra']}\n" for musica in musicas_dados]), size=(50, 10))],
                [sg.Button('Ok')]
            ]
            window = sg.Window('Músicas Cadastradas', layout)
            window.read()
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro: {str(e)}")
        finally:
            window.close()

    def buscar_musica(self):
        try:
            layout = [
                [sg.Text('Nome da música que deseja buscar'), sg.InputText(key='nome')],
                [sg.Button('Buscar'), sg.Cancel('Cancelar')]
            ]
            window = sg.Window('Buscar Música', layout)
            event, values = window.read()
            if event == 'Buscar':
                return values['nome'].strip()
            return None
        except Exception as e:
            self.mostrar_mensagem(f"Ocorreu um erro: {str(e)}")
        finally:
            window.close()

    def mostrar_mensagem(self, msg):
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
