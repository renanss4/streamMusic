import PySimpleGUI as sg # type: ignore
from datetime import datetime

class TelaUsuario:
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
                if 0 <= opcao <= 8:
                    break
                else:
                    sg.popup('Opção inválida! Escolha uma opção entre 0 e 8.')
        self.__window.close()
        return opcao

    def pegar_dados_usuario(self):
        """
        Solicita e retorna os dados de um novo usuário.
        """
        layout = [
            [sg.Text('CADASTRAR NOVO USUÁRIO', font=("Helvetica", 15))],
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Text('Email'), sg.InputText(key='email')],
            [sg.Text('Telefone'), sg.InputText(key='telefone')],
            [sg.Text('Data de Nascimento (YYYY-MM-DD)'), sg.InputText(key='data_nascimento')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Cadastrar Novo Usuário', layout)
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                values = None
                break
            if event == 'Confirmar':
                nome = values['nome'].strip()
                email = values['email'].strip()
                telefone = values['telefone'].strip()
                try:
                    data_nascimento = datetime.strptime(values['data_nascimento'], '%Y-%m-%d').date()
                except ValueError:
                    sg.popup('Data inválida! Por favor, insira no formato YYYY-MM-DD.')
                    continue
                
                if nome and email and telefone.isdigit():
                    values = {'nome': nome, 'email': email, 'telefone': telefone, 'data_nascimento': data_nascimento}
                    break
                else:
                    sg.popup('Preencha todos os campos corretamente!')
        window.close()
        return values

    def mostrar_usuarios(self, usuarios_dados):
        """
        Mostra os detalhes dos usuários cadastrados.
        """
        layout = [
            [sg.Text('DETALHES DOS USUÁRIOS CADASTRADOS', font=("Helvetica", 15))],
            [sg.Multiline('\n'.join([f"Nome: {usuario['nome']}\nEmail: {usuario['email']}\nTelefone: {usuario['telefone']}\nData de Nascimento: {usuario['data_nascimento']}\n" for usuario in usuarios_dados]), size=(60, 10))],
            [sg.Button('Ok')]
        ]
        window = sg.Window('Usuários Cadastrados', layout)
        window.read()
        window.close()

    def buscar_usuario(self):
        """
        Solicita o nome do usuário para buscar suas informações.
        """
        layout = [
            [sg.Text('Buscar Usuário', font=("Helvetica", 15))],
            [sg.Text('Nome do usuário'), sg.InputText(key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Buscar Usuário', layout)
        event, values = window.read()
        window.close()
        if event == 'Confirmar':
            return values['nome'].strip()
        return None

    def pegar_nome_artista(self):
        """
        Solicita o nome do artista.
        """
        layout = [
            [sg.Text('Nome do Artista', font=("Helvetica", 15))],
            [sg.Text('Nome do artista'), sg.InputText(key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Nome do Artista', layout)
        event, values = window.read()
        window.close()
        if event == 'Confirmar':
            return values['nome'].strip()
        return None

    def mostrar_artistas_seguidos(self, artistas_dados):
        """
        Mostra os detalhes dos artistas seguidos pelo usuário.
        """
        layout = [
            [sg.Text('ARTISTAS SEGUIDOS', font=("Helvetica", 15))],
            [sg.Multiline('\n'.join([f"Nome: {artista['nome']}\nEmail: {artista['email']}\nTelefone: {artista['telefone']}\nData de Nascimento: {artista['data_nascimento']}\n" for artista in artistas_dados]), size=(60, 10))],
            [sg.Button('Ok')]
        ]
        window = sg.Window('Artistas Seguidos', layout)
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
            [sg.Text('USUÁRIO', font=("Helvetica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
            [sg.Radio('Cadastrar Usuário', "RD1", key='1')],
            [sg.Radio('Listar Usuários', "RD1", key='2')],
            [sg.Radio('Editar Usuário', "RD1", key='3')],
            [sg.Radio('Excluir Usuário', "RD1", key='4')],
            [sg.Radio('Página de Playlists', "RD1", key='5')],
            [sg.Radio('Seguir Artista', "RD1", key='6')],
            [sg.Radio('Deixar de Seguir Artista', "RD1", key='7')],
            [sg.Radio('Ver Artistas Seguidos', "RD1", key='8')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Usuário').Layout(layout)

