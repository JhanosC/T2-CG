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
        """
        Morph obj1's faces into the coordinates of obj2's faces, matching face by face.
        :param t: Interpolation parameter (0.0 to 1.0).
        :return: A new morphed Objeto3D instance (obj3).
        """
        morphed = Objeto3D()

<<<<<<< Updated upstream
        # References to vertices and faces
=======
        #Referencias para os vertices e faces dos objetos
>>>>>>> Stashed changes
        vertices1 = self.obj1.vertices
        vertices2 = self.obj2.vertices
        faces1 = self.obj1.faces
        faces2 = self.obj2.faces

        max_len = max(faces1,faces2)

        # Morph vertices and adjust faces
        morphed_vertices = []
        morphed_faces = []
        
        for i, face1 in enumerate(max_len):
<<<<<<< Updated upstream
=======
            face1 = faces1[i % len(faces1)]
>>>>>>> Stashed changes
            face2 = faces2[i % len(faces2)]

            # Create a new face and interpolate vertices
            new_face = []
            for j in range(max(len(face1), len(face2))):
                v1 = vertices1[face1[j % len(face1)]]
                v2 = vertices2[face2[j % len(face2)]]

                # Interpolate vertex positions
                interpolated_vertex = Ponto(
                    x=(1 - t) * v1.x + t * v2.x,
                    y=(1 - t) * v1.y + t * v2.y,
                    z=(1 - t) * v1.z + t * v2.z
                )

                # Add the new vertex to the morphed vertices list
                morphed_vertices.append(interpolated_vertex)

                # Add the index of the new vertex to the current face
                new_face.append(len(morphed_vertices) - 1)
            
            # Add the new face to the morphed object
            morphed_faces.append(new_face)

        # Assign the morphed vertices and faces to the new object
        morphed.vertices = morphed_vertices
        morphed.faces = morphed_faces

        self.obj3.vertices = morphed_vertices
        self.obj3.faces = morphed_faces

        return morphed


    def morphing2(self):
        pass
    def compareVertices(self):
        pass

    def calcCentroid(self, ponto1: Ponto, ponto2: Ponto):
        pass



