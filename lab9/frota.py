from veiculo import Veiculo
from moto import Moto
from carro import Carro
from bicicleta import Bicicleta

class Frota:
    def __init__(self):
        self.__veiculos = []
 #1
    def adicionarVeiculo(self, veiculo):
     if isinstance(veiculo, Veiculo): #verifica se é um objeto da classe Veiculo ou herdeira dela, ele serve para evitar que você adicione algo que não seja um veículo
        self.__veiculos.append(veiculo)
     else:
        print("Erro: só é permitido adicionar objetos do tipo Veiculo.")

#2
    def removerVeiculo(self, veiculo):
        if veiculo in self.__veiculos:
            self.__veiculos.remove(veiculo)
        else:
            print("Veículo não encontrado.")

#3
    def removerMotos(self):
        antes = len(self.__veiculos)
        self.__veiculos = [v for v in self.__veiculos if not isinstance(v, Moto)]
        removidos = antes - len(self.__veiculos)
        print(f"Removidos {removidos} veículos do tipo Moto.")


#4
    def estaVazia(self):
        return len(self.__veiculos) == 0
        

#5
    def estaSemMotos(self):
        return not any(isinstance(v, Moto) for v in self.__veiculos)

#6
    def pesquisarCarro(self, carro):
            # Verifica se um determinado carro está na frota
            # Aqui assumimos que o parâmetro carro é um objeto da classe Carro
        return carro in [v for v in self.__veiculos if isinstance(v, Carro)]

#7
    def listarFrota(self):
        if not self.__veiculos:
            print("Frota está vazia.")
            return

        # Filtra veículos por tipo
        carros = [v for v in self.__veiculos if isinstance(v, Carro)]
        motos = [v for v in self.__veiculos if isinstance(v, Moto)]
        bicicletas = [v for v in self.__veiculos if isinstance(v, Bicicleta)]

        print("Carros:")
        for carro in carros:
            carro.imprime()
            print("-" * 30)

        print("Motos:")
        for moto in motos:
            moto.imprime()
            print("-" * 30)

        print("Bicicletas:")
        for bike in bicicletas:
            bike.imprime()
            print("-" * 30)


    
