from cd import CD

class CatalogoCDs:
    def __init__(self):
        self.__catalogo = []

    def adicionarCD(self, titulo, tempo, artista, possuo, comentario):
        self.__catalogo.append(CD(titulo, tempo, artista, possuo, comentario))


    def estarvazio(self):
        return len(self.__catalogo) == 0
    
    def buscar(self, titulo):
        for cd in self.__catalogo:
            if cd.getTitulo() == titulo:
                return cd
            
    def remover(self, titulo):
        for cd in self.__catalogo:
            if cd.getTitulo() == titulo:
                self.__catalogo.remove(cd)
                return True
        return False
    
    def printar(self):
        for cd in self.__catalogo:
            cd.imprime()
            
    

