from controles.controlador_sistema import ControladorSistema

if __name__ == "__main__":
  ControladorSistema().inicializa_sistema()

# from entidades.musica import Musica
# from entidades.playlist import Playlist
# from entidades.album import Album

# Criando algumas músicas
# musica1 = Musica(nome="Música 1", letra="Letra da Música 1")
# musica2 = Musica(nome="Música 2", letra="Letra da Música 2")
# musica3 = Musica(nome="Música 3", letra="Letra da Música 3")

# Criando uma playlist e adicionando músicas
# minha_playlist = Playlist(nome="Minha Playlist", descricao="Playlist de teste", musicas=[musica1, musica2])

# Acessando os atributos da playlist
# print("Nome da Playlist:", minha_playlist.nome)
# print("Descrição da Playlist:", minha_playlist.descricao)

# Acessando as músicas da playlist
# print("Músicas na Playlist:")
# for musica in minha_playlist.musicas:
#     print("Nome:", musica.nome)
#     print("Letra:", musica.letra)

# Criando um álbum (herdando de Playlist) e adicionando uma música
# meu_album = Album(nome="Meu Álbum", descricao="Álbum de teste", musicas=[musica3])

# Acessando os atributos do álbum
# print("Nome do Álbum:", meu_album.nome)
# print("Descrição do Álbum:", meu_album.descricao)

# Acessando as músicas do álbum
# print("Músicas no Álbum:")
# for musica in meu_album.musicas:
#     print("Nome:", musica.nome)
#     print("Letra:", musica.letra)
