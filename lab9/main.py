from veiculo import Veiculo
from carro import Carro
from bicicleta import Bicicleta
from moto import Moto


class main ():
    teste1 = Veiculo("Generico", "fabricante x", 4, "veiculo teste") 
    teste1.imprime()
    teste1.emite_som()

    teste2 = Carro("civic", "honda", 4, "carro", 4)
    teste2.imprime()
    teste2.emite_som()

    teste3 = Bicicleta("Generico", "fabricante y", 2, "bicicleta", 3)
    teste3.imprime()
    teste3.emite_som()

    teste4 = Moto("Generico", "fabricante z", 2, "moto", 2)
    teste4.imprime()
    teste4.emite_som()



