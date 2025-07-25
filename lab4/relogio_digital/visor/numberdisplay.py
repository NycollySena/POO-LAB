class NumberDisplay:
    def __init__(self, value, limite):
        self.__value = value
        self.__limite = limite

    def getValue(self):
        return self.__value

    def getLimite(self):
        return self.__limite

    def setValue(self, replacementValue):
        self.__value = replacementValue

    def getDisplayValue(self):
        if self.__value < 10:
            return "0" + str(self.__value)
        else:
            return str(self.__value)

    def increment(self):
        self.__value = (self.__value + 1) % self.__limite
