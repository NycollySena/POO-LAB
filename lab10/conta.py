class Conta:
    def __init__(self, nome, numero):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = 0
        self.__ativa = True



    def getNome (self):
        print (self.__nome)
    
    def getNumero (self):
        print (self.__numero)
    
    def getSaldo (self):
        print (self.__saldo)
    
    def getAtiva (self):
        print (self.__ativa)


    # Depósito
    def setDeposito(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self.__saldo += valor

    # Saque
    def setSaque(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente para saque.")
        self.__saldo -= valor

   

