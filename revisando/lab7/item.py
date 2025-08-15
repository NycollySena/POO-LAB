

class Item:
    def __init__(self, titulo, tempo):
        self.__titulo = titulo
        self.__tempo = tempo
        self.__possuo = False
        self.__comentario = ""

     #acesso aos atributos da superclasse
    def getTitulo(self):
        return self.__titulo 
        
    def getTempo(self):
        return self.__tempo 
    
    def getPosssuo(self):
        return self.__possuo
    
    def getComentario(self):
        return self.__comentario
    
    #modificação dos atributos da superclasse
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setTempo(self, tempo):
        self.__tempo = tempo

    def setPossuo(self, possuo):
        self.__possuo = possuo

    def setComentario(self, comentario):
        self.__comentario =  comentario

    #imprime as informações dos atributos
    def imprime(self):
        print(f"titulo: {self.__titulo}")
        print(f"tempo: {self.__tempo}")
        print(f"possuo: {self.__possuo}")
        print(f"comentario: {self.__comentario}")
    