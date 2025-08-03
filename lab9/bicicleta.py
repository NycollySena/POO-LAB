from veiculo import Veiculo

class Bicicleta (Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, marchas):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__marchas = marchas

    def getPortas (self):
        return self.__marchas
    
    def setPortas (self, marchas):
        self.__marcahs = marchas

    def imprime (self):
        super().imprime()
        print ("Numero de marchas:", self.__marchas)
        

    #metodo emite som
    def emite_som(self):
        print ("trim trim")
    