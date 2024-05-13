

class Musica:
    def __init__(self, nome=None, letra=None) -> None:
        self.__nome = nome
        self.__letra = letra

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def letra(self):
        return self.__letra
    
    @letra.setter
    def letra(self, letra):
        self.__letra = letra