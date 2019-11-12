import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

class light:
    def __init__(self):
        self.objects = []

    def add_object(self,vertex,index):
        self.objects.append((vertex,index))

    def draw_object(self,vertex,index):
        for face in index:
            glBegin(GL_QUADS)
            glColor3f(255,255,255)
            for i in face:
                glVertex3fv(vertex[i])
            glEnd()

    def loop(self):
        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        gluPerspective(0, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0,0.0, -5)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            glRotatef(1, 3, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            for obj in objects:
                draw_object(obj)

            pygame.display.flip()
            pygame.time.wait(10)
