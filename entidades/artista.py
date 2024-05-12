from pessoa import Pessoa
from musica import Musica


class Artista(Pessoa):
    def __init__(self, nome: str, email: str, senha: str, telefone: int,
                 nome_musica: str, letra: str):
        super().__init__(nome, email, senha, telefone, nome_playlist='Músicas Favoritas', descricao='Lista de músicas favoritas')
        self.__musicas[Musica(nome_musica, letra)]

# Exemplo de uso
artista = Artista('Márcio', 'marcio@email.com', 'senha123', 123456789)
print("Playlist do artista:", artista.playlists[0].nome)