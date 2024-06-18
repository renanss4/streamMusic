import PySimpleGUI as sg # type: ignore
from datetime import datetime

class TelaArtista:
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
                if 0 <= opcao <= 10:
                    break
                else:
                    sg.popup('Opção inválida! Escolha uma opção entre 0 e 10.')
        self.__window.close()
        return opcao

    def pegar_dados_artista(self):
        """
        Solicita e retorna os dados de um novo artista.
        """
        layout = [
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Text('Email'), sg.InputText(key='email')],
            [sg.Text('Telefone'), sg.InputText(key='telefone')],
            [sg.Text('Data de Nascimento (YYYY-MM-DD)'), sg.InputText(key='data_nascimento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Cadastrar Novo Artista', layout)
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                values = None
                break
            if event == 'Confirmar':
                nome = values['nome'].strip()
                email = values['email'].strip()
                telefone = values['telefone'].strip()
                data_nascimento_str = values['data_nascimento'].strip()
                try:
                    data_nascimento = datetime.strptime(data_nascimento_str, '%Y-%m-%d').date()
                    if nome and email and telefone.isdigit():
                        values = {
                            "nome": nome,
                            "email": email,
                            "telefone": telefone,
                            "data_nascimento": data_nascimento
                        }
                        break
                    else:
                        sg.popup("Dados inválidos! Verifique se todos os campos estão corretos.")
                except ValueError:
                    sg.popup("Data inválida! Por favor, insira no formato YYYY-MM-DD.")
        window.close()
        return values

    def mostrar_artistas(self, artistas_dados):
        """
        Mostra os detalhes dos artistas cadastrados.
        """
        layout = [
            [sg.Text('Detalhes dos Artistas Cadastrados', font=("Helvetica", 15))],
            [sg.Multiline('\n'.join([f"Nome: {artista['nome']}\nEmail: {artista['email']}\nTelefone: {artista['telefone']}\nData de Nascimento: {artista['data_nascimento']}\n" for artista in artistas_dados]), size=(50, 10))],
            [sg.Button('Ok')]
        ]
        window = sg.Window('Artistas Cadastrados', layout)
        window.read()
        window.close()

    def buscar_artista(self):
        """
        Solicita o nome do artista que deseja buscar.
        """
        layout = [
            [sg.Text('Nome do artista que deseja buscar'), sg.InputText(key='nome')],
            [sg.Button('Buscar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Buscar Artista', layout)
        event, values = window.read()
        window.close()
        if event == 'Buscar':
            return values['nome'].strip()
        return None

    def pegar_nome_artista(self):
        """
        Solicita o nome de um artista.
        """
        layout = [
            [sg.Text('Nome do artista'), sg.InputText(key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Nome do Artista', layout)
        event, values = window.read()
        window.close()
        if event == 'Confirmar':
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
            [sg.Text('ARTISTA', font=("Helvetica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
            [sg.Radio('Cadastrar Artista', "RD1", key='1')],
            [sg.Radio('Listar Artistas', "RD1", key='2')],
            [sg.Radio('Editar Artista', "RD1", key='3')],
            [sg.Radio('Excluir Artista', "RD1", key='4')],
            [sg.Radio('Página de Músicas', "RD1", key='5')],
            [sg.Radio('Página de Álbuns', "RD1", key='6')],
            [sg.Radio('Página de Playlists', "RD1", key='7')],
            [sg.Radio('Seguir Artista', "RD1", key='8')],
            [sg.Radio('Deixar de Seguir Artista', "RD1", key='9')],
            [sg.Radio('Ver Artistas Seguidos', "RD1", key='10')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Artista').Layout(layout)

