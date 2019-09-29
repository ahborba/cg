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
        self.w = 400
        self.h = 400
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
        self.ultimo = 0
        self.ctrlPoints =  [[35.733333, 4.1009991, 0], [30.450499, 4.1838329000000005, 0], [21.86666632, 22.1009986, 0], [45.250499000000005, 1.2504996, 0], [21.333333, 46.767664599999996, 0], [69.383831, 4.717166199999999, 0], [30.799999399999997, 66.7676646, 0], [91.78383099999999, 36.317165599999996, 0]]
       

    
    
    def keyboard(self,arg,arg1,arg2):
        letra = arg.decode('utf8')
        if letra == '+':
            self.pontos['raio_fundo_preto'] += 10
        elif letra=='-':
            self.pontos['raio_fundo_preto'] -= 10
        elif letra=='q':
            self.ctrlPoints =[[512,512,0],[512,712,0]]
        elif letra == 't':
            self.ctrlPoints.remove(1)
    
    
    
    def reshape(self,rsp1,rsp2):
        pass

    def mouse(self,tp1,tp2,x,y):
        if tp2 ==1:
            p = []
            p.append(x)
            y = self.h - y
            p.append(y)
            p.append(0)
            self.ctrlPoints.insert(len(self.ctrlPoints),p)
            print(self.ctrlPoints)
        self.ultimo +=1



    def teste_bezier(self,*pontos):
        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_FLAT)
        # for ponto in self.ctrlPoints:
        #     ponto[0]*=5
        #     ponto[1]*=5
        glMap1f(GL_MAP1_VERTEX_3, 1, 0, self.ctrlPoints)
        glEnable(GL_MAP1_VERTEX_3)
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_STRIP)
        for i in range(32):
            glEvalCoord1f(float(i)/31)
        glEnd()

        glPointSize(5)
        glColor3f(1, 0, 0)
        glBegin(GL_POINTS)
        for point in self.ctrlPoints:
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
        # self.circle(*self.pontos['fundo_preto'],self.pontos['raio_fundo_preto'])
        # self.cabeca(*self.pontos['cabeca'])
        self.teste_bezier(*self.pontos['bezier'])
        input()
        glFlush()


    def inicializa(self):
        self.pontos['fundo_preto'] = (int(self.w/2),int(self.h/2)) # adiciona o fundo preto 
        self.pontos['raio_fundo_preto'] = int(300)
        self.pontos['bezier'] = ((100,100, 0),( 130,200, 0), (170,200,0), (200,100, 0))
        self.pontos['cabeca'] = (int(self.w/2)-150,int(self.h/2)+100,int(self.w/2)+150,int(self.h/2)-100)


if __name__ == '__main__':
    git = github()
    git.inicializa()
    glutMainLoop()