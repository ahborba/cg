from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
ctrl_points = [[[-1.5, -1.5, 4.0], [-0.5, -1.5, 2.0], [0.5, -1.5, -1.0],[1.5, -1.5, 2.0]], [[-1.5, -0.5, 1.0],[-0.5, -0.5, 3.0], [0.5, -0.5, 0.0],[1.5, -0.5, -1.0]], [[-1.5, 0.5, 4.0],[-0.5, 0.5, 0.0], [0.5, 0.5, 3.0],[1.5, 0.5, 4.0]], [[-1.5, 1.5, -2.0],[-0.5, 1.5, -2.0], [0.5, 1.5, 0.0],[1.5, 1.5, -1.0]]]


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


def display():
    glPushMatrix()
    glRotatef(85.0,1.0,1.0,1.0)
    glEvalMesh2(GL_FILL,0,20,0,20)
    glPopMatrix()
    glFlush()



def init():
    glClearColor(0.0,0.0,0.0,0.0)
    glEnable(GL_DEPTH_TEST)
    glMap2f(GL_MAP2_VERTEX_3,0, 1, 0, 4,ctrl_points)
    glEnable(GL_MAP2_VERTEX_3)
    glEnable(GL_AUTO_NORMAL);
    glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_FLAT)




def main():
    glutInit()
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow('testando...')
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__':
    main()