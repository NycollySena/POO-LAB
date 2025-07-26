from veiculo import Veiculo

class Carro (Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, portas):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__portas = portas


    def getPortas (self):
        return self.__portas
    
    def setPortas (self, portas):
        self.__portas = portas

    def imprime (self):
        super().imprime()
        print ("Numero de portas:", self.__portas)
        
    #metodo emite som
    def emite_som(self):
        print ("Vrum vrum")