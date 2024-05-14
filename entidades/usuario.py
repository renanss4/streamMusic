from pessoa import Pessoa
from datetime import date
from album import Album


class Usuario(Pessoa):
    def __init__(self, nome: str, email: str, senha: str, telefone: int, eh_artista: bool, data_nascimento: date):
        super().__init__(nome, email, senha, telefone)
        self.__eh_artista = eh_artista

# Exemplo de uso
usuario = Usuario('João', 'joao@email.com', 'senha123', 123456789)
print("Playlist do usuário:", usuario.playlists[0].nome)
