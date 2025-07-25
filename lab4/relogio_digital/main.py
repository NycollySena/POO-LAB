from sistema.clockdisplay import ClockDisplay

def main():
    relogio = ClockDisplay()

    print(relogio.getTime())

    relogio.setTime(0, 0, 0)
    print(relogio.getTime())

    relogio.timeTick()
    print(relogio.getTime())

    relogio.setTime(0, 0, 59)
    print(relogio.getTime())

    relogio.timeTick()
    print(relogio.getTime())

if __name__ == '__main__':
    main()
