class NumberDisplay:
    def __init__(self, limite, valor = 0):
        
        self.__limite = limite
        self.__valor = valor


#incremento circular (quando chegar no limite volta para zero)
    def increment (self):
        self.__valor = (self.__valor + 1) % self.__limite

#para transformar o numero em string que sempre terá dois digitos mesmo qunado for menor que 10 
    def getDisplayValue (self):
        if (self.__valor < 10):
            return "0" + str (self.__valor)
        else: 
            return "" + str (self.__valor)

#conseguir ver o atributo privado em outro lugar sem ser na propria classe
    def getValue (self):
        return self.__valor
    
#conseguir modificaqr o atributo
    def setValue (self, replacementValue):
            if (0 <= replacementValue < self.__limite):
                self.__valor = replacementValue

        
    