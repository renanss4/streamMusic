from pessoa import Pessoa
from musica import Musica
from album import Album


class Artista(Pessoa):
    def __init__(self, nome: str, email: str, senha: str, telefone: int):
        super().__init__(nome, email, senha, telefone)
        self.__albuns = [Album(f'Mix do {nome}', f'Um mix do artista {nome}')]
        self.__musicas = [Musica()]

    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas

# Exemplo de uso
artista = Artista('Márcio', 'marcio@email.com', 'senha123', 123456789)
print(artista.albuns[0].adicionar_musica(artista.musicas[0]))
for e in artista.albuns[0].musicas:
    print(e.nome)
# print(artista.albuns[0].musicas.nome)
print(artista.albuns[0].musicas[0].nome)