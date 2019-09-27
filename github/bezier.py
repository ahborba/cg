from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

cos = math.cos
pi = math.pi
sin = math.sin
sqrt = math.sqrt



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
        self.ctrlPoints = [[100,100,0],[130,200,0],[170,200,0],[200,100,0]]
        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_FLAT)
        glMap1f(GL_MAP1_VERTEX_3, 1, 0, self.ctrlPoints)
        glEnable(GL_MAP1_VERTEX_3)
        self.indice=0
        self.linha=0
        self.vet_inicial=vet_inicial = [[[373, 667, 0], [456, 721, 0], [552, 726, 0], [645, 713, 0], [680, 654, 0]], [[316, 604, 0], [446, 619, 0], [502, 617, 0], [570, 635, 0], [719, 604, 0]], [[315, 503, 0], [463, 575, 0], [512, 575, 0], [578, 576, 0], [721, 514, 0]], [[357, 467, 0], [433, 420, 0], [515, 429, 0], [605, 421, 0], [682, 462, 0]]]

    
    
    def keyboard(self,arg,arg1,arg2):
        letra = arg.decode('utf8')
        if letra == '+':
            self.pontos['raio_fundo_preto'] += 10
        elif letra=='-':
            self.pontos['raio_fundo_preto'] -= 10
        elif letra=='r':
            self.pontos['cabeca'] = self.vet_inicial
        elif letra =='p':
            print('\n',self.pontos['cabeca'])
        elif letra =='t':
            print('\n\n',self.pontos['cabeca'],'\n\n')
            self.vet_inicial = self.pontos['cabeca']
    
    
    def reshape(self,rsp1,rsp2):
        pass

    def mouse(self,tp1,tp2,x,y):
        y = self.h-y
        if tp2==0:
            self.indice = 0
            self.linha =0
            menor = 1025
            j=0
            for pontos in self.pontos['cabeca']:
                i = 0
                for ponto in pontos:
                    px = ponto[0]
                    py = ponto[1]
                    euclidiana = sqrt((x-px)**2+(y-py)**2)
                    if euclidiana < menor:
                        self.indice = i
                        self.linha=j
                        menor = euclidiana
                    i+=1
                j+=1
        else:
            self.pontos['cabeca'][self.linha][self.indice] = [x,y,0]



    def cabeca(self,x1,y1,x2,y2):
        glColor3f(255, 255, 0)
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(x1, y1)  # Coordinates for the bottom left point
        glVertex2f(x2,y1)  # Coordinates for the bottom right point
        glVertex2f(x2, y2)  # Coordinates for the top right point
        glVertex2f(x1, y2)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing

    def circle(self,x, y, raio):
        # raio = 0.85*w
        glColor3f(0, 0, 0)
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine = raio * cos(i*2*pi/self.sides) + x
            sine = raio * sin(i*2*pi/self.sides) + y
            glVertex2f(cosine, sine)
        glEnd()

    def cabeca(self,pontos):
        glClearColor(0.0,0.0,0.0,0.0)
        glColor3f(255, 255, 255)
        glMap2d(GL_MAP2_VERTEX_3,0, 1, 1, 0,pontos)
        glEnable(GL_MAP2_VERTEX_3)
        glEnable(GL_AUTO_NORMAL)
        glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
        glShadeModel(GL_FLAT)
        glPushMatrix()
        # glRotatef(85.0,1.0,1.0,1.0)
        glEvalMesh2(GL_FILL,0,20,0,20)
        glPopMatrix()
        glPointSize(5)
        glColor3f(255, 0,0)
        glBegin(GL_POINTS)
        for lista in pontos:
            for ponto in lista:
                glVertex3fv(ponto)
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
        self.cabeca(self.pontos['cabeca'])
        # self.teste_bezier(*self.pontos['bezier'])
        
        glFlush()


    def inicializa(self):
        self.pontos['fundo_preto'] = (int(self.w/2),int(self.h/2)) # adiciona o fundo preto 
        self.pontos['raio_fundo_preto'] = int(300)
        self.pontos['bezier'] = ((100,100, 0),( 130,200, 0), (170,200,0), (200,100, 0))
        self.pontos['cabeca'] =   self.vet_inicial[:]



if __name__ == '__main__':
    git = github()
    git.inicializa()
    glutMainLoop()