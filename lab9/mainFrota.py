from frota import Frota
from veiculo import Veiculo
from carro import Carro
from bicicleta import Bicicleta
from moto import Moto

class main ():
    
    teste1: Veiculo
    teste1 = Carro ("civic", "honda", 4, "carro", 4)

    teste2: Veiculo 
    teste2 = Moto ("Generico", "fabricante z", 2, "moto", 2)

    teste3: Veiculo
    teste3 = Bicicleta ("Generico", "fabricante y", 2, "bicicleta", 3)

    teste4: Veiculo
    teste4 = Carro ("Generico", "fabricante w", 4, "carro 2", 2)

    frota = Frota()

    frota.adicionarVeiculo(teste1)
    frota.adicionarVeiculo(teste2)
    frota.adicionarVeiculo(teste3)
    frota.adicionarVeiculo(teste4)

    frota.listarFrota()

    frota.estaSemMotos()

    frota.pesquisarCarro(teste4)

    frota.removerVeiculo(teste3)

    frota.removerMotos()
    
    frota.listarFrota()









    