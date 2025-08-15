import random

class CD:
    def __init__(self, titulo, tempo, artista, possuo, comentario):
        self.__titulo = titulo
        self.__tempo = tempo
        self.__artista = artista
        self.__trilhas = self.__gerarTrilhas()
        self.__possuo = possuo
        self.__comentario = comentario

    #metodo interno(por isso é privado) para gerar uma trilha aleatoria 
    def __gerarTrilhas (self):
        return random.randint(1,20)
        

        #get
    def getTitulo(self):
        return self.__titulo
    
    def getTempo(self):
        return self.__tempo
    
    def getArtista(self):
        return self.__artista
    
    def getPossuo(self):
        return self.__possuo
    
    def getComentario(self):
        return self.__comentario
    
    def getTrilhas(self):
        return self.__trilhas
    
         #set

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setTempo(self, tempo):
        self.__tempo = tempo

    def setArtista(self, artista):
        self.__artista = artista

    def setPossuo(self, possuo):
        self.__possuo = possuo

    def setComentario(self, comentario):
        self.__comentario = comentario


    #metodo imprime

    def imprime(self):
        print(f"titulo: {self.__titulo}")
        print(f"Artista: {self.__artista}")
        print(f"tempo de reprodução: {self.__tempo} min")
        print(f"possuo: {self.__possuo}")
        print(f"numero de trilhas: {self.__trilhas}")
        print(f"comentario: {self.__comentario}")
    
    

        
