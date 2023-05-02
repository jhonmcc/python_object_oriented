from .Veiculo import Veiculo

class Carro(Veiculo):
    # construtor initial class and initial vars class
    def __init__(self, modelo='', marca='', ligado_desligado=False):
        Veiculo.__init__(self, modelo, marca, ligado_desligado)
        self.qtdeRodas = 4