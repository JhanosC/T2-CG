from Objeto3D import *
from Ponto import *

class Morphing:
    def __init__(self, obj1:Objeto3D, obj2: Objeto3D):
        self.obj1 = obj1
        self.obj2 = obj2
        self.obj1PontosUtilizados = [0] * len(obj1.vertices) #inicializa um array com 0's
        pass

    def morphing(self):
        pass

    def compareVertices(self):
        pass

    def calcCentroid(self, ponto1: Ponto, ponto2: Ponto):
        pass



