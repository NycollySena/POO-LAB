import random
from item import Item

class CD(Item):# cd é uma subclasse de item
    def __init__(self, titulo, tempo, artista): #possuo e comentario já estão em item são inicializados pelo construtor da classe Item.
        super().__init__(titulo, tempo)# herda os atributos titulo e tempo que ja tem na classe base que é item
        self.__artista = artista #agrega um novo atributo da classe especifica cd
        self.__trilhas = self.__gerarTrilhas() # usa self pq chama um metodo interno (novo atributo tbm)


    def __gerarTrilhas(self):
        return random.randint(1,20)
        
        #gets
    
    def getArtista(self):
        return self.__artista
    
    def getTrilhas(self):
        return self.__trilhas
    
    
        #sets (não precisa para trilhas, pq é gerado aleatorio)

    def setArtista(self, artista):
        self.__artista = artista


        #metodo que imprime todas as informações 

     # Sobrescreve o método imprime() para incluir o diretor:
    def imprime(self):
        super().imprime()  # Chama a versão da superclasse (mostra título, tempo, etc.)
        print(f"Artista: {self.__artista}")  # Adiciona info específica
        print(f"Trilhas: {self.__trilhas}")  # Adiciona info específica

        
