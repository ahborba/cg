from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class github:


    def __init__(self):
        self.pontos = {}
        self.w = 1024
        self.h = 1024
        self.keybindings = {chr(27): exit}
        glutInit()
        glutInitWindowSize(self.w, self.h)
        glutCreateWindow('Github')
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glClearColor(0, 0, 0, 0)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutMouseFunc(self.mouse)
        glShadeModel(GL_FLAT)
        glutInit()
        self.controlPoints = ((0, 0, 0),( 0.03,0.1, 0), (0.07,0.1,0), (0.1,0.0, 0))
        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_FLAT)
        glMap1f(GL_MAP1_VERTEX_3, 1, 0, self.controlPoints)
        glEnable(GL_MAP1_VERTEX_3)

    
    
    def keyboard(self,arg,arg1,arg2):

        print(arg.decode('utf8'),sep='\n\n')
        print(arg1)
        # print(arg,arg1,arg2,sep="\n",end="\n------\n")   
        pass
    
    
    def reshape(self,rsp1,rsp2):
        pass

    def mouse(self,tp1,tp2,tp3,tp4):
        print('\n',tp1,tp2,tp3,tp4,sep="-----",end="\n")
        

    def circle(posx, posy, radius):
        sides = 32
        # radius = 0.85*w
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine = radius * cos(i*2*pi/sides) + posx
            sine = radius * sin(i*2*pi/sides) + posy
            glVertex2f(cosine, sine)
        glEnd()

    def teste_bezier(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1)
        glBegin(GL_LINE_STRIP)
        for i in range(32):
            glEvalCoord1f(float(i)/31)
            print(float(i)/31)
        glEnd()
        glPointSize(5)
        glColor3f(1, 1, 0)
        glBegin(GL_POINTS)
        for point in self.controlPoints:
        	glVertex3fv(point)
        glEnd()
        glFlush()

    def fundo_branco(self):
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(0, 0)  # Coordinates for the bottom left point
        glVertex2f(1, 0)  # Coordinates for the bottom right point
        glVertex2f(1, 1)  # Coordinates for the top right point
        glVertex2f(0, 1)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
        glFlush()

    def display(self):
        self.teste_bezier()
        # self.fundo_branco()


    def inicializa(self):
        self.pontos['fundo_preto'] = (int(self.w/2),int(self.h/2)) # adiciona o fundo preto 

    def square(self,x, y, width, height):
        # We have to declare the points in this sequence: bottom left, bottom right, top right, top left
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(x, y)  # Coordinates for the bottom left point
        glVertex2f(x+width, y)  # Coordinates for the bottom right point
        glVertex2f(x+width, y+height)  # Coordinates for the top right point
        glVertex2f(x, y+height)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
        glFlush()

if __name__ == '__main__':
    git = github()
    git.inicializa()
    glutMainLoop()