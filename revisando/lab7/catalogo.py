from item import Item
from cd import CD
from dvd import DVD

class Catalogo:
    def __init__(self):
     self.__itens = [] # Armazena objetos do tipo Item (ou CD/DVD)

    def AdicionarItem(self, item):
        self.__itens.append(item)


    def remover_item(self, titulo):
        """Remove um item pelo título."""
        for item in self.__itens: #percorre toda a lista de itens
            if item.getTitulo() == titulo: # se o item for igual o que vc quer remover 
                self.__itens.remove(item) #remove
                return True #retorna true se conseguir achar e remover
        return False #retorna false se não achar
    
    def listar_itens(self):
        if not self.__itens:#verifica se a lista esta vazia
            print("O catálogo está vazio.")
        else:                                      #Usa isinstance() para verificar o tipo de cada item
            cds = [item for item in self.__itens if isinstance(item, CD)] #Cria uma lista cds contendo apenas os itens que são instâncias da classe CD
            dvds = [item for item in self.__itens if isinstance(item, DVD)]#Cria uma lista dvds contendo apenas os itens que são instâncias da classe DVD
            
        for cd in cds:# percorre todos os CDs ja filtrados
            cd.imprime()#imprime
        for dvd in dvds:#percorre todos os DVDs ja filtrados
            dvd.imprime()#imprime

    def catalogo_vazio(self):
        return len(self.__itens) == 0 #retorna true se for vdd 
    
    def BuscarItem(self, titulo):
        for i in self.__itens:#percorre toda a lista 
                if i.getTitulo() == titulo:#se for igual ao que vc procura 
                 return True #retorna true
        return False # se não achar retorna false

