import random
from item import Item

class DVD(Item):
    def __init__(self, titulo, tempo, diretor):
        super().__init__(titulo, tempo)# herda os atributos titulo e tempo que ja tem na classe base que é item
        self.__diretor = diretor #agrega um novo atributo da classe especifica cd
        
        #gets
    
    def getDiretor(self):
        return self.__diretor
    
        #sets (não precisa para trilhas, pq é gerado aleatorio)

    def setDiretor(self, diretor):
        self.__diretor = diretor


        #metodo que imprime todas as informações 

 # Sobrescreve o método imprime() para incluir o diretor:
    def imprime(self):
        super().imprime()  # Chama a versão da superclasse (mostra título, tempo, etc.)
        print(f"Diretor: {self.__diretor}")  # Adiciona info específica
        
