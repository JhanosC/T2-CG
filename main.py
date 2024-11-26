from OpenGL.GLUT import *  # Import OpenGL Utility Toolkit for creating windows and managing input
from OpenGL.GLU import *  # Import OpenGL Utility Library for perspective and other utilities
from OpenGL.GL import *   # Import OpenGL for rendering

from Objeto3D import *    # Import custom 3D object class
from Morphing import *

# Global variables to hold 3D objects
o: Objeto3D
o2: Objeto3D
o3: Objeto3D
o4: Objeto3D
t = 0.0
direction = 1
state = 1
morpher1: Morphing
morpher2: Morphing
morpher3: Morphing
morpher4: Morphing
morphing_enabled = False
started_morphing = False


def init():
    """
    Initializes the OpenGL context and loads 3D objects.
    Sets up the scene with a clear background color, depth testing, and face culling.
    Also loads files into Objeto3D instances and initializes lighting and camera.
    """
    global o, o2, o3, o4, morpher1, morpher2, morpher3, morpher4
    glClearColor(0.5, 0.5, 0.9, 1.0)  # Set background color to light blue
    glClearDepth(1.0)  # Set depth buffer clear value

    glDepthFunc(GL_LESS)  # Specify the depth comparison function
    glEnable(GL_DEPTH_TEST)  # Enable depth testing
    glEnable(GL_CULL_FACE)  # Enable face culling
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)  # Set polygon mode to fill

    # Load 3D models
    o = Objeto3D()
    o.LoadFile('models\\hard1.obj')
    o.normalize()

    o2 = Objeto3D()
    o2.LoadFile('models\\easy3.obj')
    o2.normalize()

    o3 = Objeto3D()
    #o3.LoadFile('macaco.obj')

    o4 = Objeto3D()
    o4.LoadFile('explosao.obj')

    DefineLuz()  # Set up lighting
    PosicUser()  # Set camera position

    morpher1 = Morphing(o, o4, o3)
    morpher2 = Morphing(o4, o2, o3)
    morpher3 = Morphing(o2, o4, o3)
    morpher4 = Morphing(o4, o, o3)

def DefineLuz():
    """
    Configures the lighting for the scene, defining ambient, diffuse, and specular components.
    Also specifies material properties for the objects.
    """
    luz_ambiente = [0.4, 0.4, 0.4]  # Ambient light intensity
    luz_difusa = [0.7, 0.7, 0.7]    # Diffuse light intensity
    luz_especular = [0.9, 0.9, 0.9] # Specular light intensity
    posicao_luz = [2.0, 3.0, 0.0]   # Position of the light source
    especularidade = [1.0, 1.0, 1.0] # Specular reflection coefficient

    glEnable(GL_COLOR_MATERIAL)  # Enable color tracking for materials
    glEnable(GL_LIGHTING)        # Enable lighting calculations

    # Set ambient light model
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_AMBIENT, luz_ambiente)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luz_difusa)
    glLightfv(GL_LIGHT0, GL_SPECULAR, luz_especular)
    glLightfv(GL_LIGHT0, GL_POSITION, posicao_luz)
    glEnable(GL_LIGHT0)  # Enable light 0

    # Define material properties
    glMaterialfv(GL_FRONT, GL_SPECULAR, especularidade)
    glMateriali(GL_FRONT, GL_SHININESS, 51)  # Shininess level

def PosicUser():
    """
    Sets the camera position and perspective projection for viewing the 3D scene.
    """
    glMatrixMode(GL_PROJECTION)  # Switch to projection matrix
    glLoadIdentity()  # Reset the matrix

    gluPerspective(60, 16/9, 0.01, 50)  # Configure perspective projection (FOV, aspect ratio, near, far)
    glMatrixMode(GL_MODELVIEW)  # Switch to model view matrix
    glLoadIdentity()  # Reset the matrix

    # Set up the camera view
    gluLookAt(0.9, 0.4, 2, 0, 0.2, 0, 0, 0.5, 0)  # Observer position, target, and up vector

def DesenhaLadrilho():
    """
    Draws a single tile (quad) in the 3D scene, including both the filled shape and its border.
    """
    # Draw filled quad
    glColor3f(0.5, 0.5, 0.5)  # Set tile color to gray
    glBegin(GL_QUADS)
    glNormal3f(0, 1, 0)  # Normal vector for lighting
    glVertex3f(-0.5, 0.0, -0.5)
    glVertex3f(-0.5, 0.0, 0.5)
    glVertex3f(0.5, 0.0, 0.5)
    glVertex3f(0.5, 0.0, -0.5)
    glEnd()

    # Draw border
    glColor3f(1, 1, 1)  # Set border color to white
    glBegin(GL_LINE_STRIP)
    glNormal3f(0, 1, 0)
    glVertex3f(-0.5, 0.0, -0.5)
    glVertex3f(-0.5, 0.0, 0.5)
    glVertex3f(0.5, 0.0, 0.5)
    glVertex3f(0.5, 0.0, -0.5)
    glEnd()

def DesenhaPiso():
    """
    Draws a floor composed of multiple tiles by translating the tile object across the grid.
    """
    glPushMatrix()  # Save the current matrix
    glTranslated(-20, -1, -10)  # Position the floor
    for x in range(-20, 20):  # Iterate over rows
        glPushMatrix()
        for z in range(-20, 20):  # Iterate over columns
            DesenhaLadrilho()  # Draw a single tile
            glTranslated(0, 0, 1)  # Move to the next position in the row
        glPopMatrix()
        glTranslated(1, 0, 0)  # Move to the next row
    glPopMatrix()  # Restore the matrix

def DesenhaCubo():
    glPushMatrix()
    glColor3f(1, 0, 0)
    glTranslated(0, 0.5, 0)
    glutSolidCube(1)

    glColor3f(0.5, 0.5, 0)
    glTranslated(0, 0.5, 0)
    glRotatef(90, -1, 0, 0)
    glRotatef(45, 0, 0, 1)
    glutSolidCone(1, 1, 4, 4)
    glPopMatrix()

def desenha():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)

    DesenhaPiso()
    o.Desenha()
    o.DesenhaWireframe()
    #o.DesenhaVertices()

    glutSwapBuffers()
    pass

def desenha2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)

    DesenhaPiso()
    o2.Desenha()
    o2.DesenhaWireframe()
    #o.DesenhaVertices()

    glutSwapBuffers()
    pass

def desenha3():
    global t, direction, morpher1, morpher2, morpher3, morphing_enabled, morpherAnim, state, o1,o2,o3,o4
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)

    DesenhaPiso()  # Draw the floor

    o3.Desenha()
    o3.DesenhaWireframe()
    #o3.DesenhaVertices()
    if state == 1:
        morpher1.morphing(t)
    if state == 2:
        morpher2.morphing(t)
    if state == 3:
        morpher3.morphing(t)
        
    if state == 4:
        morpher4.morphing(t)


    if morphing_enabled:
        t += direction * 0.05
        o3.rotation = (0, 1, 0, o3.rotation[3] + 90)
        if t >= 1.0 or t <= 0.0:
            state += 1
            t = 0
            if state == 5:
                state = 1
            #direction *= -1  # Reverse direction at bounds
            if state == 1 or state == 3:
                morphing_enabled = False
            

    glutSwapBuffers()
    glutPostRedisplay()  # Request the next frame
    
    pass

'''
def teclado(key, x, y):
    o3.rotation = (0, 1, 0, o3.rotation[3] + 10)

    glutPostRedisplay()
    pass
'''

def teclado(key, x, y):
    global morphing_enabled, started_morphing

    # Conversão das teclas para questão de compatibilidade
    key = key.decode('utf-8').lower()

    if key == ' ':  # Liga e desliga morphing com barra de espaço
        morphing_enabled = not morphing_enabled  # Toggle morphing state
        #print(f"Morphing {'enabled' if morphing_enabled else 'disabled'}")

    if key == 'a' and not started_morphing:
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(400, 400)
        glutInitWindowPosition(1000, 100)
        glutCreateWindow('Computacao Grafica: 3D 3rd window')
        init()
        glutDisplayFunc(desenha3)
        glutKeyboardFunc(teclado)
        started_morphing = True

    # Rotaciona objeto
    if key == 'd':
        o3.rotation = (0, 1, 0, o3.rotation[3] + 10)
    if key == 'a' and started_morphing:
        o3.rotation = (0, 1, 0, o3.rotation[3] - 10)
    glutPostRedisplay()


def main():
    """
    Main function to initialize GLUT, set up multiple windows, and start the rendering loop.
    """
    global morphing_enabled
    # Initialize and configure the first window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(100, 100)
    glutCreateWindow('Computacao Grafica - 3D')
    init()  # Call initialization
    glutDisplayFunc(desenha)  # Set display callback
    glutKeyboardFunc(teclado)  # Set keyboard callback

    # Repeat setup for the second window
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(550, 100)
    glutCreateWindow('Computacao Grafica: 3D 2nd window')
    init()
    glutDisplayFunc(desenha2)
    glutKeyboardFunc(teclado)
    if morphing_enabled:
    # Repeat setup for the third window
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
        glutInitWindowSize(400, 400)
        glutInitWindowPosition(1000, 100)
        glutCreateWindow('Computacao Grafica: 3D 3rd window')
        init()
        glutDisplayFunc(desenha3)
        glutKeyboardFunc(teclado)

    try:
        # Start the GLUT event processing loop
        glutMainLoop()
    except SystemExit:
        print('GLUT main loop exited.')

if __name__ == '__main__':
    main()