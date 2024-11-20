from Objeto3D import *
from Ponto import *

class Morphing:
    def __init__(self, obj1:Objeto3D, obj2: Objeto3D):
        self.obj1 = obj1
        self.obj2 = obj2
        self.obj1PontosUtilizados = [0] * len(obj1.vertices) #inicializa um array com 0's
        pass

    def morphing(self, t: float) ->  Objeto3D:


        """
          Interpolates between two 3D objects' vertices to create a morphed object,
          handling cases where the objects have different numbers of vertices.
          :param obj1: The starting object.
          :param obj2: The target object.
          :param t: The interpolation parameter (0.0 to 1.0).
          :return: A new morphed Objeto3D instance.
          """
        morphed = Objeto3D()

        vertices1 = self.obj1.vertices
        vertices2 = self.obj2.vertices
        len1, len2 = len(vertices1), len(vertices2)

        # Create a unified vertex set with proportional mapping
        morphed_vertices = []
        max_len = max(len1, len2)

        for i in range(max_len):
            # Get vertices proportionally (wrap around if necessary)
            v1 = vertices1[i % len1]
            v2 = vertices2[i % len2]

            # Interpolate between the two vertices
            interpolated_vertex = Ponto(
                x=(1 - t) * v1.x + t * v2.x,
                y=(1 - t) * v1.y + t * v2.y,
                z=(1 - t) * v1.z + t * v2.z
            )
                #(1 - t) * v1[j] + t * v2[j] for j in range(3)

            morphed_vertices.append(interpolated_vertex)

        # Assign the morphed vertices to the new object
        morphed.vertices = morphed_vertices
        return morphed


    def compareVertices(self):
        pass

    def calcCentroid(self, ponto1: Ponto, ponto2: Ponto):
        pass



