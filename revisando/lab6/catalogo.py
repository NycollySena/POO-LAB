from cd import CD

class CatalogoCDs:
    def __init__(self):
        self.__catalogo = [] #lista vazia e privada de cds

    def AdicionarCD (self, titulo, tempo, artista, possuo, comentario):#adicionando objeto do tipo cd na lista catalogo
        return self.__catalogo.append(CD(titulo, tempo, artista, possuo, comentario)) 
    
    def RemoveCD (self, titulo):
        for cd in self.__catalogo: #cd percorre toda a lista de cd do catalogo
            if cd.getTitulo() == titulo: #usa o metodo para conseguir acessar o atributo privado titlo dentro de cd
                self.__catalogo.remove(cd)
                return True # se achar e conseguir remover
        return False #se apos o loop não ter sucesso
        
    def ListarCDs(self):
        for cd in self.__catalogo:
            cd.imprime() #imprime todos os cds da lista

    def Buscar(self, titulo):
        for cd in self.__catalogo:
            if cd.getTitulo() == titulo: #imprime informções do cd encontrado
                cd.imprime()
                return cd
        return None

    def PossuoCD(self, titulo):
        for cd in self.__catalogo:
            if cd.getTitulo() == titulo:# imprime apenas o que for passado como argumento
                if cd.getPossuo():# se eu possuir ai sim eu imprimo
                    cd.imprime()
                    return True
            return False

    def CdPosssuo(self):
        for cd in self.__catalogo:
            if cd.getPossuo(): #ja verifica se é true
                cd.imprime() #imprime todos que eu possuo na lista 

    def esta_vazio(self):
        return len(self.__catalogo) == 0 #retorna true se for vdd



            

    