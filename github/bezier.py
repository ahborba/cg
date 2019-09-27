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
        self.teste ,self.print= False,False
        self.operacao = 'orelha_direita'


    
    
    def keyboard(self,arg,arg1,arg2):
        letra = arg.decode('utf8')
        if letra=='r':
            self.pontos[self.operacao] =[[[573, 668, 0], [602, 681, 0], [674, 710, 0], [661, 722, 0], [691, 647, 0], [663, 618, 0]], [[564, 664, 0], [650, 618, 0], [618, 630, 0], [593, 647, 0], [573, 655, 0], [663, 621, 0]]]
        elif letra =='p':
            print('\n',self.pontos[self.operacao])
        elif letra =='c':
            if self.teste:
                self.teste = False
            else:
                self.teste=True
        elif letra=='q':
            if self.print:
                self.print = False
            else:
                self.print=True
        elif letra=='t':
            self.operacao = input('self.operacao: ')
            print('escolhido: ',self.operacao)
    
    
    def reshape(self,rsp1,rsp2):
        pass

    def substitui(self,tp2,x,y):
        y = self.h-y
        if tp2==0:
            self.indice = 0
            self.linha =0
            menor = 1025
            j=0
            for pontos in self.pontos[self.operacao]:
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
            self.pontos[self.operacao][self.linha][self.indice] = [x,y,0]

    def mouse(self,tp1,tp2,x,y):
        if self.teste:
            self.substitui(tp2,x,y)
        elif tp2==1:
            print('[',x,',',self.h-y,',',0,'],',sep='')
        




    def circle(self,x, y, raio):
        # raio = 0.85*w
        glColor3f(0, 0, 0)
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine = raio * cos(i*2*pi/self.sides) + x
            sine = raio * sin(i*2*pi/self.sides) + y
            glVertex2f(cosine, sine)
        glEnd()

    def bezier(self,pontos,tipo):
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
        if tipo ==self.operacao and self.print:
            glPointSize(5)
            glBegin(GL_POINTS)
            glColor3f(255, 0,0)
            i = 0
            for lista in pontos:
                if i==1:
                    glColor(0,255,0)
                elif i ==2:
                    glColor(0,0,255)
                elif i ==3:
                    glColor(255,255,0)
                for ponto in lista:
                    glVertex3fv(ponto)
                i+=1
                
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
        self.bezier(self.pontos['cabeca'],'cabeca')
        self.bezier(self.pontos['orelha_esquerda'],'orelha_esquerda')
        self.bezier(self.pontos['orelha_direita'],'orelha_direita')
        self.bezier(self.pontos['braco'],'braco')
        self.bezier(self.pontos['pescoco'],'pescoco')
        # self.teste_bezier(*self.pontos['bezier'])
        
        glFlush()


    def inicializa(self):
        self.pontos['fundo_preto'] = (int(self.w/2),int(self.h/2)) # adiciona o fundo preto 
        self.pontos['raio_fundo_preto'] = int(300)
        self.pontos['bezier'] = ((100,100, 0),( 130,200, 0), (170,200,0), (200,100, 0))
        self.pontos['cabeca'] =  [[[357, 636, 0], [428, 700, 0], [559, 698, 0], [631, 663, 0], [664, 627, 0]], [[312, 593, 0], [533, 597, 0], [438, 572, 0], [613, 587, 0], [702, 576, 0]], [[305, 515, 0], [450, 529, 0], [535, 496, 0], [622, 481, 0], [703, 508, 0]], [[337, 445, 0], [390, 377, 0], [541, 366, 0], [631, 394, 0], [676, 457, 0]]]
        self.pontos['orelha_esquerda'] =  [[[334, 647, 0], [339, 679, 0], [328, 735, 0], [380, 691, 0], [416, 665, 0], [442, 655, 0]], [[334, 601, 0], [367, 644, 0], [369, 644, 0], [391, 662, 0], [414, 662, 0], [442, 669, 0]], [[352, 611, 0], [375, 615, 0], [398, 623, 0], [418, 638, 0], [431, 644, 0], [451, 644, 0]]]
        self.pontos['orelha_direita'] = [[[589, 668, 0], [592, 701, 0], [709, 677, 0], [630, 760, 0], [691, 647, 0], [663, 618, 0]], [[564, 664, 0], [650, 618, 0], [618, 630, 0], [593, 647, 0], [573, 655, 0], [663, 621, 0]]]
        self.pontos['braco'] = [[[430, 350, 0], [380, 319, 0], [346, 355, 0], [327, 389, 0], [306, 408, 0], [275, 403, 0]], [[425, 306, 0], [398, 309, 0], [350, 287, 0], [342, 324, 0], [306, 357, 0], [324, 351, 0]]]
        self.pontos['pescoco'] = [[[373, 232, 0], [417, 223, 0], [426, 244, 0], [436, 234, 0], [404, 358, 0], [452, 401, 0]], [[474, 223, 0], [479, 263, 0], [481, 306, 0], [483, 341, 0], [485, 366, 0], [486, 392, 0]], [[547, 151, 0], [544, 278, 0], [543, 305, 0], [543, 335, 0], [545, 371, 0], [541, 392, 0]], [[611, 225, 0], [576, 233, 0], [574, 230, 0], [580, 225, 0], [596, 369, 0], [545, 395, 0]]]
if __name__ == '__main__':
    git = github()
    git.inicializa()
    glutMainLoop()