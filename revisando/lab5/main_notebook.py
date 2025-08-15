from notebook import Notebook

class main ():

    teste = Notebook()
    

    num = int(input("Quantas notas?"))

    for i in range(num):
        nota = input("digite a nota: ")
        teste.storeNote(nota)

    teste.listNotesfor()
    teste.showMultiNoteRandom(num)


    

