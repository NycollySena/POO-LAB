from notebook import Notebook

class main:

    teste1 = Notebook()
    nota = input("digite sua nota: ")
    nota2 = input("digite sua segunda nota: ")


    teste1.storeNote(nota)
    teste1.storeNote(nota2)
    
    print("primeira lista das notas")
    teste1.listNotesfor()
    print("numero de notas")
    print(teste1.numberOfNotes())
   
    print("mostrando a primeira nota")
    teste1.showNote(0)
    print("removendo uma nota")
    teste1.removeNote(nota)
    print("lista atualizada")
    teste1.listNotesfor()


    