from Objeto3D import *
from Ponto import *

class Morphing:
    def __init__(self, obj1:Objeto3D, obj2: Objeto3D, obj3: Objeto3D):
        self.obj1 = obj1
        self.obj2 = obj2
        self.obj1PontosUtilizados = [0] * len(obj1.vertices) #inicializa um array com 0's
        self.obj3 = obj3
        pass

    def morphing(self, t: float) -> Objeto3D:
        #Ajusta coordenadas de faces e vertices de um objeto1 e coloca nas coordenadas do objeto2
        #As faces e vertices sendo interpoladas são guardadas no objeto3
        morphed = Objeto3D()

        #Referencias para os vertices e faces dos objetos
        vertices1 = self.obj1.vertices
        vertices2 = self.obj2.vertices
        faces1 = self.obj1.faces
        faces2 = self.obj2.faces

        max_len_faces = max(faces1,faces2)

        #Arrays que guardam as faces e vertices sendo interpolados
        morphed_vertices = []
        morphed_faces = []
        
        for i, face1 in enumerate(max_len_faces):
            face1 = faces1[i % len(faces1)]
            face2 = faces2[i % len(faces2)]

            #Array auxiliar para guardar as faces com os vertices interpolados
            new_faces = []

            for j in range(max(len(face1), len(face2))):
                v1 = vertices1[face1[j % len(face1)]]
                v2 = vertices2[face2[j % len(face2)]]

                #Interpolação dos vertices
                interpolated_vertex = Ponto(
                    x=(1 - t) * v1.x + t * v2.x,
                    y=(1 - t) * v1.y + t * v2.y,
                    z=(1 - t) * v1.z + t * v2.z
                )

                #Adiciona os vertices sendo interpolados a lista de vertices a ser aplicado ao objeto
                morphed_vertices.append(interpolated_vertex)

                #Adiciona os vertices sendo interpolados as novas faces que serão aplicadas ao objeto
                new_faces.append(len(morphed_vertices) - 1)

            morphed_faces.append(new_faces)

        morphed.vertices = morphed_vertices

        #Aplica as faces e vertices sendo interpolados ao objeto
        self.obj3.vertices = morphed_vertices
        self.obj3.faces = morphed_faces

        return morphed


    def morphing2(self):
        pass
    def compareVertices(self):
        pass

    def calcCentroid(self, ponto1: Ponto, ponto2: Ponto):
        pass



