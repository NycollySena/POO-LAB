from numberdisplay import NumberDisplay
from clockdisplay import ClockDisplay

class main ():
    relogio = ClockDisplay()

    print (relogio.getTime())

    relogio.setTime(0,0,0)
    print (relogio.getTime())

    relogio.timeTick()
    print (relogio.getTime())

    relogio.setTime(0,0,59)
    print (relogio.getTime())

    relogio.timeTick()
    print (relogio.getTime())
    