from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

cos = math.cos
pi = math.pi
sin = math.sin



class github:


    def __init__(self):
        pass
        # self.pontos = {}
        # self.w = 1024
        # self.h = 1024
        # self.sides = 50
        # self.keybindings = {chr(27): exit}
        # glutInit()
        # glutInitWindowSize(self.w, self.h)
        # self.git = glutCreateWindow('Github')
        # glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        # glClearColor(0, 0, 0, 0)
        # glutReshapeFunc(self.reshape)
        # glutKeyboardFunc(self.keyboard)
        # glutDisplayFunc(self.display)
        # glutIdleFunc(self.display)
        # glutMouseFunc(self.mouse)
        # glOrtho(0.0, self.w, 0.0, self.h, 0.0, 1.0)

    
    
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

    def bezier(self):
        controlPoints = [[[-1.5, -1.5, 4.0], [-0.5, -1.5, 2.0],[0.5, -1.5, -1.0], [1.5, -1.5, 2.0]],[[-1.5, -0.5, 1.0], [-0.5, -0.5, 3.0],[0.5, -0.5, 0.0], [1.5, -0.5, -1.0]],[[-1.5, 0.5, 4.0], [-0.5, 0.5, 0.0],[0.5, 0.5, 3.0], [1.5, 0.5, 4.0]],[[-1.5, 1.5, -2.0], [-0.5, 1.5, -2.0],[0.5, 1.5, 0.0], [1.5, 1.5, -1.0]]]
        glClearColor(0, 0, 0, 0)
        glMap2f(GL_MAP2_VERTEX_3, 0, 1, 3,1,1,1, 4, controlPoints)
        glEnable(GL_MAP2_VERTEX_3)
        glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix ()
        glRotatef(85.0, 1.0, 1.0, 1.0)
        for j in range(0,8):
            glBegin(GL_LINE_STRIP)
            glColor3f(255, 255, 255)
            for i in range(0,30):
                glEvalCoord2f(float(i/30.0), float(j/8.0))
            glEnd()
            glBegin(GL_LINE_STRIP)
            for i in range(0,30):
                glEvalCoord2f(float(j/8.0), float(i/30.0))
            glEnd()
        glPopMatrix ()
        


    def display(self):
        self.bezier()
        glFlush()

if __name__ == '__main__':
    git = github()
    glutInit()
    git.display()
    glutMainLoop()