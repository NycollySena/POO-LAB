import random

class RandomTester:


 def printOneRandom(self):
   print(random.randint(0,9))


 def printMultiRandom(self, many):
  for i in range(many):
    print(random.randint(0,9))


 def throwDice (self):
  return random.randint(1,6)
 
 
 def randomInRange(self, max):
  return random.randint(1, max)
 
 def randomMaxMin (self, minimo, maximo):
  return random.randint(minimo, maximo)
 
 def randomMax (self, max):
  return self.randomMaxMin(1, max)
 


 

