import random

class DVD:
    def __init__(self, titulo, tempo, diretor, possuo, comentario):
        self.__titulo = titulo
        self.__tempo = tempo
        self.__diretor = diretor
        self.__possuo = possuo
        self.__comentario = comentario

    # Getters (acesso)
    def getTitulo(self):
        return self.__titulo

    def getTempo(self):
        return self.__tempo

    def getDiretor(self):
        return self.__diretor

    def getPossuo(self):
        return self.__possuo

    def getComentario(self):
        return self.__comentario

    # Setters (modificação)
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setTempo(self, tempo):
        self.__tempo = tempo

    def setDiretor(self, diretor):
        self.__diretor = diretor

    def setPossuo(self, possuo):
        self.__possuo = possuo

    def setComentario(self, comentario):
        self.__comentario = comentario

    # Método para imprimir os dados
    def imprime(self):
        print("Título:", self.__titulo)
        print("Tempo de reprodução:", self.__tempo, "min")
        print("Diretor:", self.__diretor)
        print("Possuo:", "Sim" if self.__possuo else "Não")
        print("Comentário:", self.__comentario)
