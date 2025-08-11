from estudante import Estudante

class main: 
    teste1 = Estudante("nycolly", 202400051004, 10)
    teste1.setAdicionarCreditos(10)
    teste1.setAlterarNome("ana")
    print("aluno 1")

    print(teste1.getNome())
    print(teste1.getCreditos())
    print(teste1.getMatricula())

    teste2 = Estudante("joão", 202020200, 244)
    teste2.setAdicionarCreditos(48)
    print("aluno 2")
    print (teste2.getCreditos())

    teste3 = Estudante("Andre", 00000000, 344)
    teste3.setDecremento(48)
    print("aluno 3")
    print(teste3.getCreditos())