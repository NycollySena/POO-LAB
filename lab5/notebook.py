import random
class Notebook:
    def __init__(self):
        self.__note = list()

    #Adiciona uma nova anotação (note) na lista
    def storeNote(self, note):
        self.__note.append(note) #append(): Método de lista que insere um item no final
    
     #Retorna a quantidade de anotações armazenadas.
    def numberOfNotes(self):
        return len(self.__note) #len(): Retorna quantos itens a lista possui.
    
    #Mostra o conteúdo da anotação no índice (noteNumber) passado
    def showNote (self, noteNumber): #noteNumber representa o indice
        if noteNumber < 0 or noteNumber >= self.numberOfNotes(): # se o indice for negativo é invalido ou se ele for maior igual a qtd de itens 
         print("Este não é um número de nota válido")

        else:
         print(self.__note[noteNumber]) #mostra a nota pelo indice passado

    #Remove a anotação que corresponde ao conteúdo (note) informado.
    def removeNote(self, note):
        if note in self.__note: 
         self.__note.remove(note)
         return True
        else:
         print ("Esta não é uma nota válida")
         return False

    #Lista todas as anotações, imprimindo uma por linha
    def listNotesfor(self):
     for lista in self.__note:
      print (lista)

    #Retorna True se existir pelo menos uma anotação, caso contrário False
    def hasNotes (self):
       return len(self.__note) > 0 
    
    #Verifica se a nota (nota) está armazenada
    def compareNote (self, nota):
       if nota in self.__note:
          return True
       else:
          return False
       
    #Retornar uma anotação aleatória da lista.
    def showNoteRandom (self):
       indice = random.randint(0, self.numberOfNotes() - 1)
       return self.__note[indice]

       #return random.randint(self.__note)
       
    #Mostra várias notas aleatórias, a quantidade sendo notas
    def showMultiNoteRandom (self, notas):
       i = 0
       while i < notas:
          indice = random.randint(0, self.numberOfNotes() - 1)
          print(f"Nota {i+1}: {self.__note[indice]}")
          i += 1


          

       


       
 