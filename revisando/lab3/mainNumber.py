from revisão.lab3.numberdisplay import NumberDisplay

class main:
    teste1 = NumberDisplay(1, 24)
    print(teste1.getDisplayValue())
    teste1.increment()
    print(teste1.getDisplayValue())
    teste1.setValue(10)
    print(teste1.getValue())