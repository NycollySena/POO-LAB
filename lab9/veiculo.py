class Veiculo:
    def __init__(self, modelo, fabricante, rodas, descricao):
        self.__modelo = modelo 
        self.__fabricante = fabricante
        self.__rodas = rodas
        self.__descricao = descricao


    #acessos
    def getModelo (self):
        return self.__modelo
    
    def getFabricante (self):
        return self.__fabricante
    
    def getRodas (self):
        return self.__rodas
    
    def getDescricao (self):
        return self.__descricao
    
    #modificações 
    def setModelo (self, modelo):
        self.__modelo = modelo

    def setFabricante (self, fabricante):
        self.__fabricante = fabricante

    def setRodas (self, rodas):
        self.__rodas = rodas

    def setDescricao (self, descricao):
        self.__descricao = descricao


    #metodo imprime 
    def imprime (self):
            print("Modelo:", self.__modelo)
            print ("Fabricante:", self.__fabricante)
            print ("Quantidade de rodas:", self.__rodas)
            print ("Descrição:", self.__descricao)


    #metodo emite som
    def emite_som(self):
        pass
    
            