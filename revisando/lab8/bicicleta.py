from veiculo import Veiculo

class Bicicleta (Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, marchas):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__marchas = marchas


    def getMarchas (self):
        return self.__marchas
    
    def setMarchas(self, marchas):
        self.__marchas = marchas


    def imprime(self):
        super().imprime()
        print(self.__marchas)


    def emite_som(self):
        super().emite_som()
        print("trim trim")