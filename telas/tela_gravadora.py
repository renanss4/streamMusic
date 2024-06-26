import PySimpleGUI as sg # type: ignore
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class TelaGravadora:
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
                    if 0 <= opcao <= 5:
                        break
                    else:
                        sg.popup('Opção inválida! Escolha uma opção entre 0 e 5.')
            self.__window.close()
            return opcao
        except Exception as e:
            sg.popup(f"Ocorreu um erro: {str(e)}")
            if self.__window:
                self.__window.close()

    def pegar_dados_gravadora(self):
        try:
            layout = [
                [sg.Text('Nome'), sg.InputText(key='nome')],
                [sg.Text('Email'), sg.InputText(key='email')],
                [sg.Text('Telefone'), sg.InputText(key='telefone')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            window = sg.Window('Cadastrar Nova Gravadora', layout)
            while True:
                event, values = window.read()
                if event in (None, 'Cancelar'):
                    values = None
                    break
                if event == 'Confirmar':
                    nome = values['nome'].strip()
                    email = values['email'].strip()
                    telefone = values['telefone'].strip()
                    if nome and email and telefone.isdigit():
                        values = {"nome": nome, "email": email, "telefone": telefone}
                        break
                    else:
                        sg.popup("Dados inválidos! Verifique se todos os campos estão corretos e que o telefone contém apenas números.")
            window.close()
            return values
        except Exception as e:
            sg.popup(f"Ocorreu um erro: {str(e)}")
            window.close()

    def mostrar_gravadoras(self, gravadoras_dados):
        try:
            layout = [
                [sg.Text('Detalhes das Gravadoras Cadastradas', font=("Helvetica", 15))],
                [sg.Multiline('\n'.join([f"Nome: {gravadora['nome']}\nEmail: {gravadora['email']}\nTelefone: {gravadora['telefone']}\n" for gravadora in gravadoras_dados]), size=(50, 10))],
                [sg.Button('Ok')]
            ]
            window = sg.Window('Gravadoras Cadastradas', layout)
            window.read()
            window.close()
        except Exception as e:
            sg.popup(f"Ocorreu um erro: {str(e)}")
            window.close()

    def buscar_gravadora(self):
        try:
            layout = [
                [sg.Text('Nome da gravadora que deseja buscar'), sg.InputText(key='nome')],
                [sg.Button('Buscar'), sg.Cancel('Cancelar')]
            ]
            window = sg.Window('Buscar Gravadora', layout)
            event, values = window.read()
            window.close()
            if event == 'Buscar':
                return values['nome'].strip()
            return None
        except Exception as e:
            sg.popup(f"Ocorreu um erro: {str(e)}")
            window.close()

    def editar_gravadora(self):
        try:
            layout = [
                [sg.Text('Novo nome da gravadora'), sg.InputText(key='nome')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            window = sg.Window('Editar Gravadora', layout)
            event, values = window.read()
            window.close()
            if event == 'Confirmar':
                return {"nome": values['nome'].strip()}
            return None
        except Exception as e:
            sg.popup(f"Ocorreu um erro: {str(e)}")
            window.close()

    def mostrar_mensagem(self, msg):
        try:
            sg.popup(msg)
        except Exception as e:
            sg.popup(f"Ocorreu um erro ao mostrar a mensagem: {str(e)}")

    def init_components(self):
        try:
            sg.ChangeLookAndFeel('DarkTeal4')
            layout = [
                [sg.Text('GRAVADORA', font=("Helvetica", 25))],
                [sg.Text('Escolha a opção:', font=("Helvetica", 15))],
                [sg.Radio('Cadastrar Gravadora', "RD1", key='1')],
                [sg.Radio('Listar Gravadoras', "RD1", key='2')],
                [sg.Radio('Editar Gravadora', "RD1", key='3')],
                [sg.Radio('Excluir Gravadora', "RD1", key='4')],
                [sg.Radio('Página de Contratos', "RD1", key='5')],
                [sg.Radio('Retornar', "RD1", key='0')],
                [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
            ]
            self.__window = sg.Window('Gravadora').Layout(layout)
        except Exception as e:
            sg.popup(f"Ocorreu um erro ao inicializar os componentes: {str(e)}")
            if self.__window:
                self.__window.close()
