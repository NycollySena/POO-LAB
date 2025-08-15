from revisão.lab3.numberdisplay import NumberDisplay

class ClockDisplay:
    def __init__(self):
        self.__hours = NumberDisplay(24,0)
        self.__minutes= NumberDisplay(60,0)
        self.__segundos = NumberDisplay(60,0)
        self.__displayString = ""
        self.__updateDisplay()

#ajusta o visual do horario
    def __updateDisplay(self):
        self.__displayString = self.__hours.getDisplayValue() + ":" + self.__minutes.getDisplayValue() + ":" + self.__segundos.getDisplayValue()

#horario pronto para ser exibido
    def getTime (self):
        return self.__displayString
    
    #modifica o horário para o que vc quiser
    def setTime(self,hour,minute, segundos):
        self.__hours.setValue(hour)
        self.__minutes.setValue(minute)
        self.__segundos.setValue(segundos)
        self.__updateDisplay()

    #simula a passagem de segundos
    def timeTick(self):
        self.__segundos.increment()
        self.__updateDisplay()
        if (self.__segundos.getValue()==0): #Isso porque __valor é privado e você não pode ler ele diretamente fora do NumberDisplay.
            self.__minutes.increment()
            self.__updateDisplay()
            if(self.__minutes.getValue() == 0):
            # acaba de voltar a zero!
                self.__hours.increment()
                self.__updateDisplay()
            