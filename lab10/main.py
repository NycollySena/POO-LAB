from conta import Conta

class main ():
    teste1 = Conta ("Nycolly", "12345")

    while True:
        print ("saque: 1 - deposito: 2 - encerrar: 3")
        op = int(input("digite um numero: "))

        if (op == 1):
            valor = int(input("digite o valor: "))
            try:
                teste1.setSaque(valor)
            except ValueError as e:
                 print("Erro no saque:", e)
                 continue
            print ("saque feito com sucesso")



        elif (op == 2):
            valor = int(input("digite o valor: "))
            try:
                teste1.setDeposito(valor)
            except ValueError as e:
                 print("Erro no depósito:", e)
                 continue
            print ("deposito feito com sucesso")


        elif (op == 3):
            print ("Encerrado")
            break
            


    teste1.getSaldo()

