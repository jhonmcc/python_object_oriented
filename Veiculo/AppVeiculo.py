# to see files in others folders
import sys, os ; sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from Veiculo.Carro import Carro
from Veiculo.Moto import Moto


# use example class car
objCarChev = Carro("vectra", "Chevrolet", True)
print(objCarChev)
objCarChev.ligaDesliga(False)
print(objCarChev)

objCarChev = Moto("factor", "Yamaha", False)
print(objCarChev)