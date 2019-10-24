from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math,os,random

cos = math.cos
pi = math.pi
sin = math.sin
sqrt = math.sqrt
w = 500
h = 500
depth = 500
d = 5
fov = 0
full = True
class cidade:

    def __init__(self):
        self.pontos = {}
        self.x = 0
        self.y = 0
        self.z = 250
        self.axis_x= False
        self.dir_x = 0
        self.dir_y = 0
        self.dir_z = 0
        self.ang_x = 0
        self.ang_y = 0
        self.ang_z = 0
        self.dx = 0
        self.dy = 0
        self.init_glut()
        self.teste, self.print = False, False

    def init_glut(self):
        glutInit()
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)
        glShadeModel(GL_SMOOTH)
        glutInitWindowSize(w, h)
        glutCreateWindow('Cidade')
        # glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)
        glutIdleFunc(self.camera)
        glViewport(0, 0, w, h)
        # glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glClearDepth(1.0)
        glMatrixMode(GL_PROJECTION)
        glutSetCursor(GLUT_CURSOR_NONE)
        glOrtho(-w, w, -h, h, -depth, depth)
        glClearColor(0, 0, 0, 0)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutSpecialFunc(self.special)
        glutDisplayFunc(self.display)
        glutWarpPointer(int(w/2),int(h/2))
        glutKeyboardFunc(self.keyboard)
        

    def keyboard(self, key, x, y):
        key = key.decode('utf8').lower()
        direcao = False
        if key == chr(27):
            os.system('clear')
            sys.exit()
        elif key == 'w':
            self.z -= d
        elif key == 'a':
            self.x -= d
            self.dir_x-=d
        elif key == 's':
            self.z += d
        elif key == 'd':
            self.x += d
            self.dir_x +=d

        self.camera(direcao)

    def special(self, key, x, y):
        d = 1
        if key== GLUT_KEY_LEFT:
            self.ang_y -= 0.05
            self.dir_x = sin(self.ang_y)
            self.dir_z = -cos(self.ang_y)
        elif key == GLUT_KEY_RIGHT:
            self.ang_y += 0.05
            self.dir_x = sin(self.ang_y)
            self.dir_z = -cos(self.ang_y)
        elif key == GLUT_KEY_UP:
            self.x += self.dir_x * d
            self.z += self.dir_z * d
            self.y += self.dir_y * d
        elif key == GLUT_KEY_DOWN:
            self.x -= self.dir_x * d
            self.z -= self.dir_z * d
            self.y -= self.dir_y * d
        self.camera()

    def motion(self, x, y):
        x = (w/2)-x
        y = (h/2)-y
        # esquerda
        if (x - self.dx) > 0 :
            self.ang_y -= 0.01
            self.dir_x = sin(self.ang_y)
            self.dir_z = -cos(self.ang_y)
        else:
            # direita
            self.ang_y += 0.01
            self.dir_x = sin(self.ang_y)
            self.dir_z = -cos(self.ang_y)
        self.dx = x
        self.dy = y
        # self.camera(x, y,True)

    def mouse(self, tp1, tp2, x, y):
        print("mouse_click: ", x, y, sep=" ", end="\n")

    def camera(self, x=0, y=0,girar_camera=False):
        if girar_camera:
            self.dir_x = x
            self.dir_y = y
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(0.5, 1080/720, 1, 100)
        gluLookAt(self.x,0,self.z,self.dir_x,self.dir_y,self.z-0.1,0,1,0)
        #            gluLookAt(self.x, self.y ,self.z,self.dir_x,self.dir_y,0 , 1, 0, 0)
        # gluLookAt(self.x, self.y ,self.z,self.dir_x,self.dir_y,0 , 0, 1, 0)
        glutPostRedisplay()
        os.system('clear')
        print('camera:  ',self.x,self.y,self.z)
        print('direcao:',self.dir_x,self.dir_y,self.dir_z)
        # print('x: ', self.x, '\ny: ', self.y, '\nz: ', self.z,'\n\ndir x: ',self.dir_x,'\ndir y: ',self.dir_y,'\n\nfov: ',fov)



    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.cube1()
        self.cube2()
        self.point()
        self.axis()
        glFlush()
        # glutSwapBuffers()

        

    def inicializa(self):
        if full:
            glutFullScreenToggle()
        self.camera()
        self.axis()
        self.cube1()
        self.pontos['casa'] = []
        self.pontos['telhado'] = []


    def axis(self):
        vertex = (((100,0,0),(255,0,0)),((0,100,0),(0,255,0)),((0,0,100),(0,0,255)))
        # x = red
        # y = green 
        # z = blue
        glBegin(GL_LINES)
        for v,c in vertex:
            r,g,b = c
            glColor3f(r,g,b)
            glVertex3fv((0,0,0))
            glVertex3fv(v)
        glEnd()

    def point (self):
            glPointSize(10)
            glBegin(GL_POINTS)
            glColor3f(255, 0,0)
            # glVertex3fv([0,0,0])
            glVertex3fv([0,0,250])
            glEnd()

    def cube1(self):
        vertex = ((-250, 250, -250), (250, 250, -250), (-250, -250, -250), (250, -250, -250),
                  (-250, 250, 250), (250, 250, 250), (-250, -250, 250), (250, -250, 250))
        edges = ((0, 1), (1, 3), (3, 2), (2, 0), (3, 7), (7, 5),
                 (5, 1), (5, 4), (4, 0), (4, 6), (6, 7), (6, 2))
        glBegin(GL_LINES)
        glColor3f(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        for edge in edges:
            for v in edge:
                glVertex3fv(vertex[v])
        glEnd()

    def cube2(self):
        vertex = ((300, 600, 300), (600, 600, 300), (300, 300, 300), (600, 300, 300),
                  (300, 600, 600), (600, 600, 600), (300, 300, 600), (600, 300, 600))
        edges = ((0, 1), (1, 3), (3, 2), (2, 0), (3, 7), (7, 5),
                 (5, 1), (5, 4), (4, 0), (4, 6), (6, 7), (6, 2))
        glBegin(GL_LINES)
        glColor3f(random.randint(0, 255), random.randint(
            0, 255), random.randint(0, 255))
        for edge in edges:
            for v in edge:
                glVertex3fv(vertex[v])
        glEnd()


if __name__ == '__main__':
    git = cidade()
    git.inicializa()
    glutMainLoop()
