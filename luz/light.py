from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

cos = math.cos
pi = math.pi
sin = math.sin
sqrt = math.sqrt
dx=dy=dz=0


class light:

    def __init__(self):
        self.pontos = {}
        self.w = 512
        self.h = 512
        self.sides = 50
        self.objects = []
        self.light_sources = []
        glutInit()
        glutInitWindowSize(self.w, self.h)
        glutCreateWindow('Github')
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glClearColor(0, 0, 0, 0)
        glEnable(GL_DEPTH_TEST)
        glutKeyboardFunc(self.keyboard)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glOrtho(0.0, self.w, 0.0, self.h, 0.0, 1.0)
        glClearColor(0, 0, 0, 0)

    def keyboard(self, arg, arg1, arg2):
        letra = arg.decode('utf8')
            
        if letra=='d':
            dx += .01
        elif letra =='a':
            dx  -= .01
        elif letra =='w':
            dy += .01
        elif letra == 's':
            dy -= .01
        elif letra == 'i':
            dz += .1
        elif letra =='k':
            dz -= .1
        elif letra =='+':
            pass
        elif letra =='-':
            pass
        
    def draw_light(self):
        glPushMatrix()
        glTranslate(dx,dy,dz)
        for light_source in self.light_sources:
            pass
        glPopMatrix()
        

 


    def draw_object(self, vertex, index,name):
        for face in index:
            v_l = [vertex[f] for f in face]
            glBegin(GL_QUADS)
            glColor3b(255,0,0)
            for v in v_l:
                glVertex3fv(v)
            glEnd()

    def fundo_branco(self):
        glColor3f(255, 255, 255)
        glBegin(GL_QUADS)  
        glVertex2f(-self.w, self.h)  # Coordinates for the bottom left point
        glVertex2f(self.w, self.h)  # Coordinates for the bottom right point
        glVertex2f(self.w, -self.h)  # Coordinates for the top right point
        glVertex2f(-self.w,-self.h)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
    
    def display(self):
        glBegin(GL_QUADS)  
        glColor3f(255, 255, 255)
        glVertex2f(-1000, 1000)
        glVertex2f(1000, 1000)
        glVertex2f(1000, -1000)
        glVertex2f(-1000,-1000)
        glEnd()
        # for obj in self.objects:
        #     self.draw_object(*obj)
        glFlush()

    def add_object(self, vertex_list, index_list,name):
        self.objects.append((vertex_list, index_list,name))

    def add_light_source(self, light_source):
        self.light_sources.append(light_source)

    def main_loop(self):
        glutMainLoop()
