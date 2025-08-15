from item import Item
from cd import CD
from dvd import DVD
from catalogo import Catalogo

class main:
    teste1 = Catalogo()
    teste1.AdicionarItem(CD("legiao", 1, "renato")) #cd ja é uma subclassse de item, não precisa passar item 
    teste1.listar_itens()
    teste1.AdicionarItem(DVD("legiao urbana", 1, "renato russo"))
    teste1.listar_itens()
    teste1.remover_item("legiao")
    print(f"esta vazio: {teste1.catalogo_vazio()}")
    teste1.BuscarItem("legiao urbana")
    teste1.listar_itens()