import random

class RandomTester:

    def printOneRandom(self):
        print(random.randint(0,9))


    def printMultiRandom(self, many):
        for i in range(many):
            print(random.randint(0,9))
            # i + 1 ( não precisa disso)

    
    def throwDice (self):
        return random.randint(1,6)
    

    def RandomMax (self, max):
        return random.randint(1,max)
    
    def RandomMinMax (self, min, max):
        return random.randint(min, max)
    
    def Random1Max(self, max):
        return self.RandomMinMax(1, max)

