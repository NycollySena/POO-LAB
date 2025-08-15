from frota import Frota
from veiculo import Veiculo
from carro import Carro
from bicicleta import Bicicleta
from moto import Moto

class main ():
    
    teste1: Veiculo #vinculação estatica ( caso coloque moto, por exemplo, o python não interrompe, é uma desvantagem do python)
    teste1 = Carro ("civic", "honda", 4, "carro", 4) #vinculação dinamica: 
    #o Python só vai decidir em tempo de execução qual método imprime() ou emite_som() usar — o da classe Carro, Moto ou Bicicleta

    teste2: Veiculo 
    teste2 = Moto ("Generico", "fabricante z", 2, "moto", 2)

    teste3: Veiculo
    teste3 = Bicicleta ("Generico", "fabricante y", 2, "bicicleta", 3)

    teste4: Veiculo
    teste4 = Carro ("Generico", "fabricante w", 4, "carro 2", 2)

    frota = Frota()
    #quem decide qual versão do método será executada é o Python em tempo de execução.
    
    frota.adicionarVeiculo(teste1)
    frota.adicionarVeiculo(teste2)
    frota.adicionarVeiculo(teste3)
    frota.adicionarVeiculo(teste4)
    print("veiculos adicionados:")
    frota.listarFrota()
    print("esta sem moto?:")
    print(frota.estaSemMotos())
    print("o carro teste4 esta na lista:")
    print(frota.pesquisarCarro(teste4))
    print("removendo o veiculo teste3")
    frota.removerVeiculo(teste3)
    print("removendo a moto teste2:")
    frota.removerMotos(teste2)
    print("lista de veiculos")
    frota.listarFrota()









    