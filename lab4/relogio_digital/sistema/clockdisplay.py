from visor.numberdisplay import NumberDisplay

class ClockDisplay:
    def __init__(self):
        self.__horas = NumberDisplay(0, 24)
        self.__minutos = NumberDisplay(0, 60)
        self.__segundos = NumberDisplay(0, 60)
        self.__displayString = ""
        self.__updateDisplay()

    def getTime(self):
        return self.__displayString

    def __updateDisplay(self):
        self.__displayString = self.__horas.getDisplayValue() + ':' + self.__minutos.getDisplayValue() + ':' + self.__segundos.getDisplayValue()

    def setTime(self, hour, minute, second):
        self.__horas.setValue(hour)
        self.__minutos.setValue(minute)
        self.__segundos.setValue(second)
        self.__updateDisplay()

    def timeTick(self):
        self.__segundos.increment()
        self.__updateDisplay()
        if self.__segundos.getValue() == 0:
            self.__minutos.increment()
            self.__updateDisplay()
            if self.__minutos.getValue() == 0:
                self.__horas.increment()
                self.__updateDisplay()
