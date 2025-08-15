from veiculo import Veiculo
from carro import Carro
from bicicleta import Bicicleta
from moto import Moto

class Frota:
    def __init__(self):  
      self.__veiculos = []


    def adicionarVeiculo(self, veiculo):
       if isinstance(veiculo, Veiculo):# se veiculo for do tipo Veiculo
          self.__veiculos.append(veiculo)

    def removerVeiculo(self, veiculo):
       if veiculo in self.__veiculos:# se veiculo for da lista de veiculos
          self.__veiculos.remove(veiculo)

    def removerMotos(self, moto):
        motos = [moto for moto in self.__veiculos if isinstance(moto, Moto)] #filtrando uma lista só com as motos
        for i in motos: #percorre a lista de motos 
          self.__veiculos.remove(moto) #remove uma por uma as motos


    def Frota_vazia(self):
       return len(self.__veiculos) == 0#retorna true ou false 
    
    def estaSemMotos(self):
       motos = [moto for moto in self.__veiculos if isinstance(moto, Moto)]
       return len(motos) == 0 #retorna true ou false
    
    def pesquisarCarro(self, carro):
       carros = [carro for carro in self.__veiculos if isinstance(carro, Carro)]
       for i in carros:
          if i == carro:
             return True
       return False
    
    def listarFrota(self):
       carros = [carro for carro in self.__veiculos if isinstance(carro, Carro)]
       motos = [moto for moto in self.__veiculos if isinstance(moto, Moto)]
       bicicletas = [bicicleta for bicicleta in self.__veiculos if isinstance(bicicleta, Bicicleta)]

        
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
       
       
       