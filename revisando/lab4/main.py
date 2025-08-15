from randomtester import RandomTester

class main:
    if __name__ == "__main__":

        teste1 = RandomTester()
        
        #imprimem
        print("5 numeros aleatorios")
        teste1.printMultiRandom(5)
        print("um numero aleatorio")
        teste1.printOneRandom()


        #retornam
        print("um numero de 1 a 6")
        print(teste1.throwDice())
        print("um umero de 2 a 8")
        print(teste1.RandomMinMax(2,8))
        print("um numero no maximo 5")
        print(teste1.RandomMax(5))
        print("um numero no maximo 10")
        print(teste1.Random1Max(10))