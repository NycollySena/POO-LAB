
class Conta:
    def __init__(self, nome, numero):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = 0
        self.__ativa = True


    def getSaldo(self):
        return self.__saldo
    
    def getNome(self):
        return self.__nome
    
    def getNumero(self):
        return self.__numero
    
    def getAtiva(self):
        return self.__ativa
    
    def setSaldo(self, saldo):
        self.__saldo = saldo
    
    def setNome(self,nome):
        self.__nome = nome
    
    def setNumero(self, numero):
        self.__numero = numero

    def setAtiva(self, ativa):
        self.__ativa = ativa


    def Deposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor precisa ser positivo!")
        self.__saldo += valor
    

    def Saque(self, valor):
        if valor <= 0:
            raise ValueError("O valor precisa ser positivo!")
        if valor > self.__saldo:
            raise ValueError("O valor ultrapassa o saldo")
        else:
            self.__saldo -= valor
