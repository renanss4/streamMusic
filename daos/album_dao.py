from daos.dao import DAO
from entidades.album import Album
from excecoes.excecoes import InvalidEntityError, EntityNotFoundError

class AlbumDAO(DAO):
    def __init__(self):
        super().__init__('album.pkl')

    def add(self, album: Album):
        try:
            if album is None or not isinstance(album, Album) or not isinstance(album.nome, str):
                raise InvalidEntityError("Álbum inválido ou nome do álbum não é uma string.")
            super().add(album.nome, album)
        except InvalidEntityError as e:
            print(f"Erro ao adicionar álbum: {e}")

    def get(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome do álbum deve ser uma string.")
            return super().get(nome)
        except EntityNotFoundError as e:
            print(f"Erro ao obter álbum: {e}")
            return None
        except InvalidEntityError as e:
            print(f"Erro ao obter álbum: {e}")
            return None

    def update(self, album: Album):
        try:
            if album is None or not isinstance(album, Album) or not isinstance(album.nome, str):
                raise InvalidEntityError("Álbum inválido ou nome do álbum não é uma string.")
            super().update(album.nome, album)
        except EntityNotFoundError as e:
            print(f"Erro ao atualizar álbum: {e}")
        except InvalidEntityError as e:
            print(f"Erro ao atualizar álbum: {e}")

    def remove(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise InvalidEntityError("Nome do álbum deve ser uma string.")
            super().remove(nome)
        except EntityNotFoundError as e:
            print(f"Erro ao remover álbum: {e}")
        except InvalidEntityError as e:
            print(f"Erro ao remover álbum: {e}")
