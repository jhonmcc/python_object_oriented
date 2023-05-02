from .Veiculo import Veiculo

class Moto(Veiculo):
    # construtor initial class and initial vars class
    def __init__(self, modelo='', marca='', ligado_desligado=False):
        self.modelo = modelo
        self.marca = marca
        self.ligado_desligado = ligado_desligado
        self.qtdeRodas = 2