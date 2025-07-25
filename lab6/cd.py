import random

class CD:
    def __init__(self, titulo, tempo, artista, possuo, comentario):
        self.__titulo = titulo
        self.__tempo = tempo
        self.__artista = artista
        self.__trilhas = self.__gerarTrilhas()
        self.__possuo = possuo
        self.__comentario = comentario

    # Método interno para gerar número de trilhas
    def __gerarTrilhas(self):
        return random.randint(1, 20)

    # Getters (acesso)
    def getTitulo(self):
        return self.__titulo

    def getTempo(self):
        return self.__tempo

    def getArtista(self):
        return self.__artista

    def getTrilhas(self):
        return self.__trilhas

    def getPossuo(self):
        return self.__possuo

    def getComentario(self):
        return self.__comentario

    # Setters (modificação)
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

    # Método para imprimir os dados
    def imprime(self):
        print("Título:", self.__titulo)
        print("Tempo de reprodução:", self.__tempo, "min")
        print("Artista:", self.__artista)
        print("Número de trilhas:", self.__trilhas)
        print("Possuo:", "Sim" if self.__possuo else "Não")
        print("Comentário:", self.__comentario)
