from veiculo import Veiculo

class Carro (Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, portas):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__portas = portas


    def getPortas (self):
        return self.__portas
    
    def setPortas(self, portas):
        self.__portas = portas


    def imprime(self):
        super().imprime()
        print(self.__portas)


    def emite_som(self):
        super().emite_som()
        print("vrum vum")