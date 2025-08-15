from abc import ABC, abstractmethod

class Veiculo (ABC): #classe abstrata
    def __init__(self, modelo, fabricante, rodas, descricao):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__rodas = rodas
        self.__descricao = descricao


    def getModelo (self):
        return self.__modelo
    
    def getFabricante(self):
        return self.__fabricante
    
    def getRodas(self):
        return self.__rodas
    
    def getDescricao(self):
        return self.__descricao
    

    def setModelo(self, modelo):
        self.__modelo = modelo

    def setFabricante(self, fabricante):
        self.__fabricante = fabricante

    def setRodas(self, rodas):
        self.__rodas = rodas

    def setDescricao(self, descricao):
        self.__descricao = descricao

    def imprime(self):
        print(self.__modelo)
        print(self.__fabricante)
        print(self.__rodas)
        print(self.__descricao)

    @abstractmethod  # Método abstrato - deve ser implementado pelas subclasses
    def emite_som(self):
        pass
       