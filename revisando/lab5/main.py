from notebook import Notebook

class main:
    teste1 = Notebook()
    nota = input("digite sua nota: ")
    nota2 = input("digite sua segunda nota: ")
    nota3 = input("digite sua terceira nota: ")
    nota4 = input("digite sua quarta nota: ")


    teste1.storeNote(nota)
    teste1.storeNote(nota2)
    teste1.storeNote(nota3)
    teste1.storeNote(nota4)
    
    
    print("primeira lista das notas")
    teste1.listNotesfor()

    print ("a lista esta vazia?")
    print(teste1.hasNotes())

    print("removendo a primeira nota")
    teste1.removeNote(nota)
    print("a primeira nota esta na lista?")
    print(teste1.compareNote(nota))
    print("a terceira nota esta na lista?")
    print(teste1.compareNote(nota3))
    print("uma nota aleatoria")
    print(teste1.showNoteRandom())
    print("2 notas aleatorias")
    teste1.showMultiNoteRandom(2)