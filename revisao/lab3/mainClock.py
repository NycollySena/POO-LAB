from revisao.lab3.clockdisplay import ClockDisplay
from revisao.lab3.numberdisplay import NumberDisplay

class main:
    teste1 = ClockDisplay()
    print(teste1.getTime())  # Imprime o horário atual (inicializado)
    teste1.setTime(11, 25, 59)
    print(teste1.getTime())  # Imprime o horário atualizado
    teste1.timeTick()
    print(teste1.getTime())

    #falta tranformar em pacote para conseguir rodar