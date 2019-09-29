from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
from transformacao import *

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
        self.ctrlPoints = [[100,100,0],[130,200,0],[170,200,0],[200,100,0]]
        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_FLAT)
        glMap1f(GL_MAP1_VERTEX_3, 1, 0, self.ctrlPoints)
        glEnable(GL_MAP1_VERTEX_3)
        self.indice=0
        self.linha=0
        self.rotacao = False
        self.teste ,self.print= False,False
        self.operacao = 'orelha_direita'
        self.alpha = 0
        self.transf = Transformacao(self.w,self.h)

    def transformacao_rotacao(self):
        self.alpha=1
        if self.alpha >= 360:
            self.alpha = 0
        self.transformacao('rotacao')
        


    def transformacao_centro(self,op,mat,dx=0,dy=0):
        if op =='translacao':
            mat = self.transf.translacao(mat,dx,dy)
        elif op =='escala':
            mat  =self.transf.escala(mat,dx,dy)
        elif op =='rotacao':
            mat  =self.transf.rotacao(mat,self.alpha)
        return mat

    def transformacao_bezier(self,op,mat,dx,dy):
        nova_mat = []
        for linha in mat:
            if op =='translacao':
                nova_mat.append(self.transf.translacao(linha,dx,dy))
            elif op =='escala':
                print(op)
                nova_mat.append(self.transf.escala(linha,dx,dy))
            elif op =='rotacao':
                nova_mat.append(self.transf.rotacao(linha,self.alpha))
        return nova_mat


    def transformacao(self,op,dx=0,dy=0):
        self.pontos['fundo_preto'] =  self.transformacao_centro(op,self.pontos['fundo_preto'],dx,dy)
        self.pontos['cabeca'] = self.transformacao_bezier(op,self.pontos['cabeca'] ,dx,dy)
        self.pontos['orelha_esquerda'] = self.transformacao_bezier(op,self.pontos['orelha_esquerda'] ,dx,dy)
        self.pontos['orelha_direita'] = self.transformacao_bezier(op,self.pontos['orelha_direita'] ,dx,dy)
        self.pontos['braco'] = self.transformacao_bezier(op,self.pontos['braco'] ,dx,dy)
        self.pontos['pescoco'] = self.transformacao_bezier(op,self.pontos['pescoco'] ,dx,dy)
    
    def keyboard(self,arg,arg1,arg2):
        letra = arg.decode('utf8')
        dx = 0
        dy = 0
        translacao = False
        escala = False
        if letra=='d':
            dx, translacao = 10, True
        elif letra =='a':
            dx, translacao = -10, True
        elif letra =='w':
            dy, translacao = 10, True
        elif letra == 's':
            dy, translacao = -10, True
        
        if letra =='+':
            dx,dy,escala=1.1,1.1,True
        elif letra =='-':
            dx,dy,escala=.9,.9,True
        
        if letra == 'r':
            if self.rotacao:
                self.rotacao = False
            else:
                self.rotacao = True


        if translacao:
            self.transformacao('translacao',dx,dy)
        elif escala:
            self.transformacao('escala',dx,dy)
        
            


    
    
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
        




    def circle(self,circulo):
        x = circulo[0][0]
        y = circulo[0][1]
        raio = circulo[1][0]-x
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
        glVertex2f(-self.w, self.h)  # Coordinates for the bottom left point
        glVertex2f(self.w, self.h)  # Coordinates for the bottom right point
        glVertex2f(self.w, -self.h)  # Coordinates for the top right point
        glVertex2f(-self.w,-self.h)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
    


    def display(self):
        # fundo branco
        self.fundo_branco()
        # fundo preto
        self.circle(self.pontos['fundo_preto'])
        self.bezier(self.pontos['cabeca'],'cabeca')
        self.bezier(self.pontos['orelha_esquerda'],'orelha_esquerda')
        self.bezier(self.pontos['orelha_direita'],'orelha_direita')
        self.bezier(self.pontos['braco'],'braco')
        self.bezier(self.pontos['pescoco'],'pescoco')
        if self.rotacao:
            self.transformacao_rotacao()
        # self.teste_bezier(*self.pontos['bezier'])
        glFlush()


    def inicializa(self):
        self.pontos['fundo_preto'] = [[0,0,0],[0.79296875,0,0]] # adiciona o fundo preto
        self.pontos['cabeca']= [[[-0.302734375, 0.2421875, 0], [-0.1640625, 0.3671875, 0], [0.091796875, 0.36328125, 0], [0.232421875, 0.294921875, 0], [0.296875, 0.224609375, 0]], [[-0.390625, 0.158203125, 0], [0.041015625, 0.166015625, 0], [-0.14453125, 0.1171875, 0], [0.197265625, 0.146484375, 0], [0.37109375, 0.125, 0]], [[-0.404296875, 0.005859375, 0], [-0.12109375, 0.033203125, 0], [0.044921875, -0.03125, 0], [0.21484375, -0.060546875, 0], [0.373046875, -0.0078125, 0]], [[-0.341796875, -0.130859375, 0], [-0.23828125, -0.263671875, 0], [0.056640625, -0.28515625, 0], [0.232421875, -0.23046875, 0], [0.3203125, -0.107421875, 0]]]
        self.pontos['orelha_esquerda']= [[[-0.34765625, 0.263671875, 0], [-0.337890625, 0.326171875, 0], [-0.359375, 0.435546875, 0], [-0.2578125, 0.349609375, 0], [-0.1875, 0.298828125, 0], [-0.13671875, 0.279296875, 0]], [[-0.34765625, 0.173828125, 0], [-0.283203125, 0.2578125, 0], [-0.279296875, 0.2578125, 0], [-0.236328125, 0.29296875, 0], [-0.19140625, 0.29296875, 0], [-0.13671875, 0.306640625, 0]], [[-0.3125, 0.193359375, 0], [-0.267578125, 0.201171875, 0], [-0.22265625, 0.216796875, 0], [-0.18359375, 0.24609375, 0], [-0.158203125, 0.2578125, 0], [-0.119140625, 0.2578125, 0]]]
        self.pontos['orelha_direita']= [[[0.150390625, 0.3046875, 0], [0.15625, 0.369140625, 0], [0.384765625, 0.322265625, 0], [0.23046875, 0.484375, 0], [0.349609375, 0.263671875, 0], [0.294921875, 0.20703125, 0]], [[0.1015625, 0.296875, 0], [0.26953125, 0.20703125, 0], [0.20703125, 0.23046875, 0], [0.158203125, 0.263671875, 0], [0.119140625, 0.279296875, 0], [0.294921875, 0.212890625, 0]]]
        self.pontos['braco']= [[[-0.16015625, -0.31640625, 0], [-0.2578125, -0.376953125, 0], [-0.32421875, -0.306640625, 0], [-0.361328125, -0.240234375, 0], [-0.40234375, -0.203125, 0], [-0.462890625, -0.212890625, 0]], [[-0.169921875, -0.40234375, 0], [-0.22265625, -0.396484375, 0], [-0.31640625, -0.439453125, 0], [-0.33203125, -0.3671875, 0], [-0.40234375, -0.302734375, 0], [-0.3671875, -0.314453125, 0]]]
        self.pontos['pescoco']= [[[-0.271484375, -0.546875, 0], [-0.185546875, -0.564453125, 0], [-0.16796875, -0.5234375, 0], [-0.1484375, -0.54296875, 0], [-0.2109375, -0.30078125, 0], [-0.1171875, -0.216796875, 0]], [[-0.07421875, -0.564453125, 0], [-0.064453125, -0.486328125, 0], [-0.060546875, -0.40234375, 0], [-0.056640625, -0.333984375, 0], [-0.052734375, -0.28515625, 0], [-0.05078125, -0.234375, 0]], [[0.068359375, -0.705078125, 0], [0.0625, -0.45703125, 0], [0.060546875, -0.404296875, 0], [0.060546875, -0.345703125, 0], [0.064453125, -0.275390625, 0], [0.056640625, -0.234375, 0]], [[0.193359375, -0.560546875, 0], [0.125, -0.544921875, 0], [0.12109375, -0.55078125, 0], [0.1328125, -0.560546875, 0], [0.1640625, -0.279296875, 0], [0.064453125, -0.228515625, 0]]]

if __name__ == '__main__':
    git = github()
    git.inicializa()
    glutMainLoop()