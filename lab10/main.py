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




    #  # Tentar sacar até 3 vezes
    # MAX_ATTEMPTS = 3
    # attempts = 0
    # successful = True
    # while not successful and attempts < MAX_ATTEMPTS:
    #         try:
    #             teste1.setDeposito(100)
    #             successful = True
    #             print("Depósito realizado. Saldo:", teste1.getSaldo())
    #         except ValueError as e:
    #             print("Erro no depósito:", e)
    #             attempts += 1

    # if not successful:
    #         print("Não foi possível realizar o depósito após várias tentativas.")

    # attempts = 0
    # successful = False

    # while not successful and attempts < MAX_ATTEMPTS:
    #     try:
    #         teste1.setSaque(60)
    #         successful = True
    #         print("Saque realizado. Saldo:", teste1.getSaldo())
    #     except ValueError as e:
    #         print("Erro no saque:", e)
    #         attempts += 1

    # if not successful:
    #     print("Não foi possível realizar o saque após várias tentativas.")

