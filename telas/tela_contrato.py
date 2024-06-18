import PySimpleGUI as sg # type: ignore
from datetime import datetime

class TelaContrato:
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
                if 0 <= opcao <= 5:
                    break
                else:
                    sg.popup('Opção inválida! Escolha uma opção entre 0 e 5.')
        self.__window.close()
        return opcao

    def pegar_dados_contrato(self):
        """
        Solicita e retorna os dados de um novo contrato.
        """
        layout = [
            [sg.Text('Número'), sg.InputText(key='numero')],
            [sg.Text('Artista'), sg.InputText(key='artista')],
            [sg.Text('Gravadora'), sg.InputText(key='gravadora')],
            [sg.Text('Data de Início (YYYY-MM-DD)'), sg.InputText(key='data_inicio')],
            [sg.Text('Data de Fim (YYYY-MM-DD)'), sg.InputText(key='data_fim')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Cadastrar Novo Contrato', layout)
        while True:
            event, values = window.read()
            if event in (None, 'Cancelar'):
                values = None
                break
            if event == 'Confirmar':
                numero = values['numero'].strip()
                artista = values['artista'].strip()
                gravadora = values['gravadora'].strip()
                data_inicio_str = values['data_inicio'].strip()
                data_fim_str = values['data_fim'].strip()
                try:
                    data_inicio = datetime.strptime(data_inicio_str, '%Y-%m-%d').date()
                    data_fim = datetime.strptime(data_fim_str, '%Y-%m-%d').date()
                    if numero.isdigit() and artista and gravadora and data_inicio <= data_fim:
                        values = {
                            "numero": numero,
                            "artista": artista,
                            "gravadora": gravadora,
                            "data_inicio": data_inicio,
                            "data_fim": data_fim
                        }
                        break
                    else:
                        sg.popup("Dados inválidos! Verifique se todos os campos estão corretos.")
                except ValueError:
                    sg.popup("Data inválida! Por favor, insira no formato YYYY-MM-DD.")
        window.close()
        return values

    def mostrar_contratos(self, contratos_dados):
        """
        Mostra os detalhes dos contratos cadastrados.
        """
        layout = [
            [sg.Text('Detalhes dos Contratos Cadastrados', font=("Helvetica", 15))],
            [sg.Multiline('\n'.join([f"Número: {contrato['numero']}\nArtista: {contrato['artista']}\nGravadora: {contrato['gravadora']}\nData de Início: {contrato['data_inicio']}\nData de Fim: {contrato['data_fim']}\n" for contrato in contratos_dados]), size=(50, 10))],
            [sg.Button('Ok')]
        ]
        window = sg.Window('Contratos Cadastrados', layout)
        window.read()
        window.close()

    def buscar_por_artista(self):
        """
        Solicita o nome do artista para buscar contratos associados a ele.
        """
        layout = [
            [sg.Text('Nome do artista com contrato que deseja buscar'), sg.InputText(key='artista')],
            [sg.Button('Buscar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Buscar Contrato por Artista', layout)
        event, values = window.read()
        window.close()
        if event == 'Buscar':
            return values['artista'].strip()
        return None

    def buscar_por_gravadora(self):
        """
        Solicita o nome da gravadora para buscar contratos associados a ela.
        """
        layout = [
            [sg.Text('Nome da gravadora com contrato que deseja buscar'), sg.InputText(key='gravadora')],
            [sg.Button('Buscar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Buscar Contrato por Gravadora', layout)
        event, values = window.read()
        window.close()
        if event == 'Buscar':
            return values['gravadora'].strip()
        return None

    def buscar_por_numero(self):
        """
        Solicita o número do contrato para buscar um contrato específico.
        """
        layout = [
            [sg.Text('Número do contrato que deseja buscar'), sg.InputText(key='numero')],
            [sg.Button('Buscar'), sg.Cancel('Cancelar')]
        ]
        window = sg.Window('Buscar Contrato por Número', layout)
        event, values = window.read()
        window.close()
        if event == 'Buscar':
            try:
                return int(values['numero'].strip())
            except ValueError:
                sg.popup("Entrada inválida! Por favor, insira um número.")
        return None

    def mostrar_mensagem(self, msg):
        """
        Mostra uma mensagem na tela.
        """
        sg.popup(msg)

    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('CONTRATO', font=("Helvetica", 25))],
            [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
            [sg.Radio('Cadastrar Contrato', "RD1", key='1')],
            [sg.Radio('Listar Contratos', "RD1", key='2')],
            [sg.Radio('Buscar Contratos por Artista', "RD1", key='3')],
            [sg.Radio('Buscar Contratos por Gravadora', "RD1", key='4')],
            [sg.Radio('Buscar Contrato por Número', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Contrato').Layout(layout)
