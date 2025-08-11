class Professor:
    def __init__(self, nome, SIAPE, carga):
        self.__nome =  nome
        self.__SIAPE = SIAPE
        self.__carga = carga


    def getNome (self):
        return self.__nome
    
    def getSIAPE (self):
        return self.__SIAPE
    
    #carga horária semanal
    def getCarga (self):
        return self.__carga
    
    def setNome(self, nome):
        self.__nome = nome

    def SetSIAPE(self, siape):
        self.__SIAPE = siape

    def setCarga(self, carga):
        self.__carga = carga

    
    def setmaisHoras (self, horas):
        self.__carga += horas

    def setmenosHoras (self, horas):
        self.__carga -= horas