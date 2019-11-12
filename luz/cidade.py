from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math,os,random,numpy as np,pygame

cos = math.cos
pi = math.pi
sin = math.sin
sqrt = math.sqrt
w = 1024
h = 1024
depth = 1024
fov = 0
full = False
r = random.randint
firstMouse = True

dx = 0
def normalize(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm
       
class light:

    def __init__(self):
        self.pontos = {}
        self.objects = []
        self.teste, self.print = False, False
        glutInit()
        glutInitWindowSize(w, h)
        glutCreateWindow('Cidade')
        glMatrixMode(GL_PROJECTION)
        # glOrtho(-w/2, w/2, -h/2, h/2, -depth, depth)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)
        glutIdleFunc(self.display)
        glEnable(GL_DEPTH_TEST)

    def keyboard(self, key, x, y):
        key = key.decode('utf8').lower()
        print(key)

    def display(self):
        global dx
        dx+=0.01
        glDepthMask(GL_TRUE)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glRotate(0.1,0,1,0)
        # self.cube1()
        # self.cube2()
        for o in self.objects:
            self.draw_object(*o)
        # glTranslate(0.0001,0,0)
        glFlush()



    def cube1(self):
        vertex = ((25, 50, 25), (50, 50, 25), (25, 25, 25), (50, 25, 25),
                  (25, 50, 50), (50, 50, 50), (25, 25, 50), (50, 25, 50))
        edges = ((0, 1, 3, 2), (1,5,7,3), (5,5,6,7),
                 (4,0,2,6),( 2,3,7,6), (4,5,1,0))
        glColor3f(r(0, 255), r(0, 255), r(0, 255))
        for edge in edges:
            glBegin(GL_QUADS)
            for v in edge:
                glVertex3fv(vertex[v])
            glEnd()

    def cube2(self):
        vertex = ((30, 60, 30), (60, 60, 30), (30, 30, 30), (60, 30, 30),
                  (30, 60, 60), (60, 60, 60), (30, 30, 60), (60, 30, 60))
        edges = ((0, 1), (1, 3), (3, 2), (2, 0), (3, 7), (7, 5),
                 (5, 1), (5, 4), (4, 0), (4, 6), (6, 7), (6, 2))
        glBegin(GL_LINES)
        glColor3f(r(0, 255), r(0, 255), r(0, 255))
        for edge in edges:
            for v in edge:
                glVertex3fv(vertex[v])
        glEnd()

    def draw_object(self,vertex,index):
        for face in index:
            glBegin(GL_QUADS)
            glColor3f(r(0, 255), r(0, 255), r(0, 255))
            for i in face:
                glVertex3fv(vertex[i])
            glEnd()
    def add_object(self,vertex,index):
        self.objects.append((vertex,index))
    def main_loop(self):
        glutMainLoop()

