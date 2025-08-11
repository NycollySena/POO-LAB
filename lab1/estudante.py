class Estudante :
    def __init__(self, nome, matricula, creditos):
        self.__nome = nome 
        self.__matricula = matricula
        self.__creditos = creditos



    def setAdicionarCreditos(self, numero):
        self.__creditos += numero


    def setAlterarNome(self, nome):
        self.__nome = nome


    def getNome(self):
        return self.__nome
    
    def getMatricula(self):
        return self.__matricula
    
    def getCreditos(self):
        return self.__creditos
    
    def setDecremento(self, numero):
        self.__creditos -= numero

    