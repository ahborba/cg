from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

cos = math.cos
pi = math.pi
sin = math.sin



class github:


    def __init__(self):
        self.pontos = {}
        self.w = 1024
        self.h = 1024
        self.sides = 50
        self.keybindings = {chr(27): exit}
        glutInit()
        glutInitWindowSize(self.w, self.h)
        self.git = glutCreateWindow('Github')
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glClearColor(0, 0, 0, 0)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutMouseFunc(self.mouse)
        glOrtho(0.0, self.w, 0.0, self.h, 0.0, 1.0)
        self.controlPoints = ((100,100, 0),( 130,200, 0), (170,200,0), (200,100, 0))
        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_FLAT)
        glMap1f(GL_MAP1_VERTEX_3, 1, 0, self.controlPoints)
        glEnable(GL_MAP1_VERTEX_3)

    
    
    def keyboard(self,arg,arg1,arg2):
        letra = arg.decode('utf8')
        if letra == '+':
            self.pontos['raio_fundo_preto'] += 10
        elif letra=='-':
            self.pontos['raio_fundo_preto'] -= 10
    
    
    
    def reshape(self,rsp1,rsp2):
        pass

    def mouse(self,tp1,tp2,tp3,tp4):
        print('\n',tp1,tp2,tp3,tp4,sep="-----",end="\n")


    def cabeca(self,x,y,a,b):
        d2r = pi/180.0
        glColor(255,255,255)
        glBegin(GL_POLYGON)
        for i in range(0,360):
            rad = i*d2r
            glVertex2f(cos(rad)*a+ x,sin(rad)*b + y)
        glEnd()

    def circle(self,x, y, raio):
        # raio = 0.85*w
        glColor3f(0, 0, 0)
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine = raio * cos(i*2*pi/self.sides) + x
            sine = raio * sin(i*2*pi/self.sides) + y
            glVertex2f(cosine, sine)
        glEnd()

    def teste_bezier(self,*pontos):
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_STRIP)
        for i in range(32):
            glEvalCoord1f(float(i)/31)
        glEnd()
        glPointSize(5)
        glColor3f(1, 1, 0)
        glBegin(GL_POINTS)
        for point in self.controlPoints:
        	glVertex3fv(point)
        glEnd()

    def fundo_branco(self):
        glColor3f(255, 255, 255)
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(0, 0)  # Coordinates for the bottom left point
        glVertex2f(self.w, 0)  # Coordinates for the bottom right point
        glVertex2f(self.w, self.h)  # Coordinates for the top right point
        glVertex2f(0, self.h)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
    


    def display(self):
        # fundo branco
        self.fundo_branco()
        # fundo preto
        self.circle(*self.pontos['fundo_preto'],self.pontos['raio_fundo_preto'])
        self.cabeca(*self.pontos['cabeca'],*self.pontos['raios_cabeca'])
        self.teste_bezier(*self.pontos['bezier'])
        
        glFlush()


    def inicializa(self):
        self.pontos['fundo_preto'] = (int(self.w/2),int(self.h/2)) # adiciona o fundo preto 
        self.pontos['raio_fundo_preto'] = int(300)
        self.pontos['bezier'] = ((100,100, 0),( 130,200, 0), (170,200,0), (200,100, 0))
        self.pontos['cabeca'] = (int(self.w/2),int(self.h/2)+30)
        self.pontos['raios_cabeca'] = (160,130)


if __name__ == '__main__':
    git = github()
    git.inicializa()
    glutMainLoop()