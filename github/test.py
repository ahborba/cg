from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import matplotlib.pyplot as plt,numpy as np, math

ctrl_points = [    [        [-1.3, -1.5, 0 ] , [-0.5, -1.7, 0] , [0.5, -1.7, 0] , [1.3, -1.5 , 0]        ],    [        [-2.3, -0.5, 0 ] , [-0.5, -0.5, 0] , [0.5, -0.5, 0] , [2.3, -0.5 , 0]        ],    [        [-2.3,  0.5, 0 ] , [-0.5,  0.5, 0] , [0.5,  0.5, 0] , [2.3,  0.5 , 0]        ],    [        [-1.3,  1.5, 0 ] , [-0.5,  1.7, 0] , [0.5,  1.7, 0] , [1.3,  1.5 , 0]        ]]
def reshape(w,h):
    glViewport(0, 0,  w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if w <= h:
        glOrtho(-5.0, 5.0, -5.0*float(h)/float(w),5.0*float(h)/float(w), -5.0, 5.0)
    else:
        glOrtho(-5.0*float(w)/float(h),5.0*float(w)/float(h), -5.0, 5.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def mat():
    glPointSize(5)
    glColor3f(1, 1, 0)
    glBegin(GL_POINTS)
    for lista in ctrl_points:
        for ponto in lista:
            glVertex3fv(ponto)
    glEnd()




def display():
    glClearColor(0.0,0.0,0.0,0.0)
    glMap2d(GL_MAP2_VERTEX_3,0, 1, 1, 0,ctrl_points)
    glEnable(GL_MAP2_VERTEX_3)
    glEnable(GL_AUTO_NORMAL)
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    glShadeModel(GL_FLAT)
    glPushMatrix()
    # glRotatef(85.0,1.0,1.0,1.0)
    glEvalMesh2(GL_FILL,0,20,0,20)
    glPopMatrix()
    mat()
    glFlush()



    




def main():
    glutInit()
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow('testando...')
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__':
    main()