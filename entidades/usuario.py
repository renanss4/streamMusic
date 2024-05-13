from pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome: str, email: str, senha: str, telefone: int):
        super().__init__(nome, email, senha, telefone)

# Exemplo de uso
usuario = Usuario('João', 'joao@email.com', 'senha123', 123456789)
print("Playlist do usuário:", usuario.playlists[0].nome)
