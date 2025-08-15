import random

class Notebook:
    def __init__(self):
        self.__notes = list()

    def storeNote (self, nota):
        return self.__notes.append(nota) #adicionando nova nota
    
    def numberOfNotes(self):
        return len(self.__notes) # mostra a quantidade de notas na lista
    
    def showNote (self, indice): # mostra a nota que esta no indice informado
        if indice < 0: # não existe indice com numero negativo então informa o erro
            print ("esse numero não é um numero de nota valido")

        elif indice < self.numberOfNotes(): # se o numero do indice estiver menor que a quatidade de notas 
            print(self.__notes[indice]) #printa a nota que ta naquela posição

        else:
            print("esse não é um nuemro valido") # caso contrario aos anteriores vai printar erro

    
    def removeNote (self, nota):# remover a nota 
        if nota in self.__notes:
            self.__notes.remove(nota)

        else:
            print("essa nota não é valida")

    
    def listNotesfor (self): #printa todas as notas da lista 
        for i in self.__notes: # indice vai percorrer até o final 
            print(i)
    
    def hasNotes(self): #verifica se a lista esta vazia, se sim true, cas contrario false
        if self.numberOfNotes() == 0: # na versão simplificada não precisa condicional, só retorna o metodo == 0 e ele ja retorna
            return True                     #true ou false
        else:
            return False
        
    def compareNote(self, nota):# para ver se uma nota esta na lista
        for i in self.__notes:
            if i == nota:
                return True    
        return False # retorna false se depois de percorrer todo o loop não achar uma nota igual
    
    def showNoteRandom(self): #mostra uma nota aleatoria 
        return self.__notes[random.randint(0,self.numberOfNotes()-1)]
    
    def showMultiNoteRandom(self, numero):
        if not self.__notes:  # Verifica se a lista está vazia
            print("Nenhuma nota disponível.")
            return
        
        i = 0
        while i < numero:
            indice = random.randint(0,self.numberOfNotes()-1)
            print(self.__notes[indice])
            i +=1





