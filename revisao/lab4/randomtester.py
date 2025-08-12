import random

class RandomTester: 

    def printOneRandom(self):
        print(random.randint(0,9))


    def printMultiRandom(self, numero):
        for i in range (numero):
            print(random.randint(0,9))

    def throwDice (self):
        return random.randint(1,6)
    
    def randomMax(self, max):
        return random.randint(1,max)
    
    def randomMaxMin (sel, min, max):
        return random.randint(min, max)
    
    def randomMax2 (self, max):
        return self.randomMaxMin(1, max)
