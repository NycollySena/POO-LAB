from randomTester import RandomTester    

class main:
    if __name__ == "__main__":

        tester = RandomTester() #criando objeto do tipo RandomTester

        #métodos que imprimem 
        tester.printOneRandom()  # Imprimir um número aleatório de 0 a 9
        tester.printMultiRandom(5)  #Imprimir vários números aleatórios

       
        #métodos que retornam 
        print (tester.throwDice()) #Simular dado de 6 lados
        print (tester.randomInRange(10)) #Número aleatório de 1 até max
        print (tester.randomMaxMin(5,10)) #Número aleatório entre minimo e maximo
        print (tester.randomMax(5)) #Chama o anterior, com mínimo fixo em 1
