from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
# from transformacao import Transformacao

class cubo:
    def __init__(self):
        glutInit()
        glutInitWindowSize(500,500)
        git = glutCreateWindow('Cubo')
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glutKeyboardFunc(self.keyboard)
        glutMouseFunc(self.mouse)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        self.transformacao=True
        self.rotacao=False
        glEnable(GL_MAP1_VERTEX_3)
        self.linhas=[[[0.5,0.5,0.5],[0.5,-0.5,0.5],[0.5,-0.5,-0.5],[0.5,0.5,-0.5],[0.5,0.5,0.5]],[[-0.5,0.5,0.5],[-0.5,-0.5,0.5],[-0.5,-0.5,-0.5],[-0.5,0.5,-0.5],[-0.5,0.5,0.5]],[[-0.5,0.5,0.5],[0.5,0.5,0.5],[0.5,-0.5,0.5],[-0.5,-0.5,0.5],[-0.5,0.5,0.5]],[[-0.5,0.5,-0.5],[0.5,0.5,-0.5],[0.5,-0.5,-0.5],[-0.5,-0.5,-0.5],[-0.5,0.5,-0.5]]]
        self.cores = [[195,54,44],[255,134,66],[244,220,181],[129,108,91],[195,183,172],[231,227,215],[102,141,60],[177,221,161],[229,243,207],[0,151,172],[60,214,230],[151,234,244],[0,121,150],[6,194,244],[95,216,250]]

    def mouse(self,tp1,tp2,x,y):
        x-=250
        y-=250
        y/=250
        x/=250
        if tp2==1:
            print('[',x,',',y,',',0,'],',sep='')
        
    def keyboard(self,arg,arg1,arg2):
        letra = arg.decode('utf8')
        dx,dy=0,0
        if letra=='p':
            if self.transformacao:
                self.transformacao = False
                print('perspectiva desativada')
            else:
                self.transformacao = True
                print('perspectiva ativada')
        elif letra =='a':
            dx=-0.1
        elif letra=='d':
            dx=0.1
        elif letra =='w':
            dy=0.1
        elif letra == 's':
            dy=-0.1
        elif letra=='r':
            if self.rotacao:
                self.rotacao = False
                print('perspectiva desativada')
            else:
                self.rotacao = True
                print('perspectiva ativada')

    def transformacao_perspectiva(self):
        linhas_perspectiva = []
        for face in self.linhas:
            pontos_face=[]
            for ponto in face:
                X,Y,Z = ponto
                d = 2
                x =  (X * d) / (Z + d)
                y = (Y * d) / (Z + d)
                pontos_face.append([x,y,0])
            linhas_perspectiva.append(pontos_face)
        self.perspectiva(linhas_perspectiva)
        
        


    def fundo_branco(self):
        glColor3f(255, 255, 255)
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(-10, 10)  # Coordinates for the bottom left point
        glVertex2f(10, 10)  # Coordinates for the bottom right point
        glVertex2f(10, -10)  # Coordinates for the top right point
        glVertex2f(-10,-10)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
    

    def display(self):
        self.fundo_branco()
        glClearColor(0,0,0,1)
        if self.transformacao:
            self.transformacao_perspectiva()
        else:
            self.perspectiva(self.linhas)
        if self.rotacao:
            # glRotate(0.1,1,0,0)
        glFlush()

    def perspectiva(self,lin):
        i = 0
        for face in lin:
            r,g,b = self.cores[i]
            glColor3f(0,0,0)
            i+=1
            # if i ==1:
            #     continue
            glBegin(GL_LINE_STRIP)
            for ponto in face:
                glVertex3fv(ponto)
                # print(ponto)
            glEnd()
            # glFlush()
            # print('face: ',i)
            # input()

if __name__=='__main__':
    cubo = cubo()
    glutMainLoop()