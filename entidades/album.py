from entidades.musica import Musica
from entidades.playlist import Playlist

class Album(Playlist):
    def __init__(self, nome: str, descricao: str = '', musicas: list[Musica] = None):
        super().__init__(nome, descricao, musicas)

    # def adicionar_musica(self, musica):
    #     if musica not in self.musicas:
    #         self.musicas.append(musica)
    #     else:
    #         print("Música já existente no álbum!")

    # def remover_musica(self, musica):
    #     if musica in self.__musicas:
    #         self.__musicas.remove(musica)
    #         print("Música removida do álbum!")
    #     else:
    #         print("Música não existente no álbum!")