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
        # glutIdleFunc(self.display)
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
        glutWarpPointer(250,250)
        glutKeyboardFunc(self.keyboard)
        

    def keyboard(self, key, x, y):
        key = key.decode('utf8').lower()
        if key == chr(27):
            os.system('clear')
            sys.exit()
        elif key == 'w':
            self.z -= d
            self.axis_x=False
        elif key == 's':
            self.z += d
            self.axis_x=False
        elif key == 'a':
            self.x -= d
            self.axis_x=True
        elif key == 'd':
            self.x += d
            self.axis_x=True
        self.camera(x,y)

    def special(self, key, x, y):
        d = 0.5
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
        self.camera(x, y)

    

    def motion(self, x, y):
        self.camera(x, y)

    def mouse(self, tp1, tp2, x, y):
        print("mouse_click: ", x, y, sep=" ", end="\n")

    ''' x , y , z = posicao da camera
        x+dir_x , y+dir_y , z+dir_z = direcao em que a camera está olhando
        0 , 1 , 0 = não sei'''
    def camera(self, x=0, y=0):
        # global fov
        self.dir_x = (w/2)-x
        self.dir_y = (h/2)-y
        # glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # gluLookAt(1, 1, 1, 0, 0, 0, 0, 1, 0)

        gluPerspective(.5, 1080/720, 1, 100)
        
        # gluPerspective(1,1,1,1,1)
        if self.axis_x:
            gluLookAt(self.x, self.y ,self.z,self.dir_x,self.dir_y,0 , 0, 1, 0)
        else:
            gluLookAt(self.x, self.y ,self.z,self.dir_x,self.dir_y,0 , 1, 0, 0)
        glutPostRedisplay()
        os.system('clear')
        print('x: ', self.x, '\ny: ', self.y, '\nz: ', self.z,'\n\ndir x: ',self.dir_x,'\ndir y: ',self.dir_y,'\n\nfov: ',fov)

        
        # gluLookAt(self.x, self.y, self.z, self.x+self.dir_x,self.y+self.dir_y, self.dir_z+self.z, 0, 1, 0)
    



    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.cube()
        self.point()
        self.axis()
        glFlush()
        # glutSwapBuffers()

        

    def inicializa(self):
        if full:
            glutFullScreenToggle()
        self.camera()
        self.axis()
        self.cube()
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

    def cube(self):
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

if __name__ == '__main__':
    git = cidade()
    git.inicializa()
    glutMainLoop()
