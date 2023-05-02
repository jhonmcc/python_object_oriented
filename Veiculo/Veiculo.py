# # to export in others files 
# import sys, os ; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

class Veiculo:
    # construtor initial class and initial vars class
    def __init__(self, modelo='', marca='', ligado_desligado=False):
        self.modelo = modelo
        self.marca = marca
        self.ligado_desligado = ligado_desligado

    # encapsulate 
    def setModelo(self, modelo):
        self.modelo = modelo

    def setmarca(self, marca):
        self.marca = marca

    def getModelo(self):
        return self.modelo

    def getmarca(self):
        return self.marca
    
    def setLigadoDesligado(self, ligado_desligado):
        self.ligado_desligado = ligado_desligado

    def getLigadoDesligado(self):
        return self.ligado_desligado

    # methods class 
    def ligaDesliga(self, ligado_desligado):
        self.setLigadoDesligado(ligado_desligado)

    
    # print represent class example
    def __repr__(self) -> str:
        return self.modelo + " - " + str(self.ligado_desligado)


