from veiculo import Veiculo

class Moto (Veiculo):
    def __init__(self, modelo, fabricante, rodas, descricao, cilindrada):
        super().__init__(modelo, fabricante, rodas, descricao)
        self.__cilindrada = cilindrada
    
    def getPortas (self):
        return self.__cilindrada
    
    def setPortas (self, cilindrada):
        self.__cilindrada = cilindrada


    def imprime (self):
        super().imprime()
        print ("Cilindrada:", self.__cilindrada)
        

    #metodo emite som
    def emite_som(self):
        print ("randanda")