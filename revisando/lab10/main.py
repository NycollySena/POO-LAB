from conta import Conta


class main:
    teste1 = Conta("Nycolly", 12345)

    while True:
        print("Escolha uma opção: 1- deposito  2- Saque 3- encerrar")
        op = int(input("digite a opção: ")) #precisa ter o int no começo pq o input só retorna string e o int transfoma no tipo que a gente precisa


        if (op == 1):
            valor = int(input("qual valor deseja depositar?: "))
            try:
                teste1.Deposito(valor)
            except ValueError as e: # caso ocorra o erro vai printar a mensagem 
                print("Erro no deposito: ",e) # o "e" puxa a mesagem de erro que fizemos no raise do metodo
                continue # para continuar o loop e voltar para escolher a opção 

            print(f"você depositou: R${valor},00 ")
            print(f"Saldo atual: {teste1.getSaldo()}")


        elif (op == 2):
            valor = int(input("qual valor deseja sacar?: "))
            try:
                teste1.Saque(valor)
            except ValueError as e:
                print("erro no saque:",e)
                continue

            print(f"você sacou: R${valor},00 ")
            print(f"Saldo atual: {teste1.getSaldo()}")


        elif (op == 3):
            print("Encerrando...")
            break
    
    teste1.getSaldo()



