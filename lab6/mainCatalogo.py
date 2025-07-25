from catalogo import CatalogoCDs


class main ():
    teste = CatalogoCDs()

    teste.adicionarCD("legião urbana", "1", "renato russo", True, "muito bom")
    teste.adicionarCD("legião", "1", "renato", True, "muito bom")
    teste.printar()
    teste.remover("legião")
    print("\n\n\n\n")
    teste.printar()

    cd = teste.buscar("legião urbana")
    
    cd.imprime()


