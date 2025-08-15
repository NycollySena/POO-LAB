from veiculo import Veiculo

class Moto (Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, cilindrada):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__cilindrada = cilindrada


    def getCilindrada (self):
        return self.__cilindrada
    
    def setCilindrada(self, cilindrada):
        self.__cilindrada = cilindrada


    def imprime(self):
        super().imprime()
        print(self.__cilindrada)


    def emite_som(self):
        super().emite_som()
        print("Randanda")