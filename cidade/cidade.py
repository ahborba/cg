from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math,os,random,numpy as np

cos = math.cos
pi = math.pi
sin = math.sin
sqrt = math.sqrt
w = 500
h = 500
depth = 500
fov = 0
full = False
def normalize(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm
       
class cidade:



    def __init__(self):
        self.pontos = {}
        self.camera_position = np.array([0,0,250],dtype=np.float64)
        self.camera_direction= np.array([0,0,249],dtype=np.float64)
        self.camera_up = np.array([0,1,0])
        self.last_x = int(w/2)
        self.last_y = int(h/2)
        self.yaw = self.last_x
        self.pitch = self.last_y
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
        # glutSetCursor(GLUT_CURSOR_NONE)
        glOrtho(-w, w, -h, h, -depth, depth)
        glClearColor(0, 0, 0, 0)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutPassiveMotionFunc(self.motion)
        glutDisplayFunc(self.display)
        glutWarpPointer(int(w/2),int(h/2))
        glutKeyboardFunc(self.keyboard)
        
        

    def keyboard(self, key, x, y):
        key = key.decode('utf8').lower()
        speed = 0.1
        if key == chr(27):
            # os.system('clear')
            sys.exit()
        elif key == 'w':
            self.camera_position += speed * self.camera_direction
        elif key == 'a':
            self.camera_position += np.cross(self.camera_direction,self.camera_up) * speed

        elif key == 's':
            self.camera_position -= speed * self.camera_direction
        elif key == 'd':
            self.camera_position -= np.cross(self.camera_direction,self.camera_up) * speed    
    
        self.camera()

   

    def motion(self, x, y):
        sensitivity = 0.1
        x = (w/2)-x
        y = (h/2)-y
        dx = (x - self.last_x) * sensitivity
        dy = (y - self.last_y) * sensitivity
        self.last_x , self.last_y = x,y
        self.yaw += dx
        self.pitch +=dy
        if self.yaw > 89:
            self.yaw = 89
        if self.pitch< -89:
            self.pitch = -89
        
        self.camera_direction[0] = cos(np.radians(self.yaw)) * cos(np.radians(self.pitch))
        self.camera_direction[1] = sin(np.radians(self.pitch))
        self.camera_direction[2] = sin(np.radians(self.yaw)) * cos(np.radians(self.pitch))
        self.camera_direction = normalize(self.camera_direction)
        glutWarpPointer(int(w/2),int(h/2))
        self.camera()

    def mouse(self, tp1, tp2, x, y):
        print("mouse_click: ", x, y, sep=" ", end="\n")

    def camera(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(np.radians(45), 1080/720, 1, 100)
        gluLookAt(*self.camera_position,*(self.camera_position+self.camera_direction),*self.camera_up)
        glutPostRedisplay()
        # os.system('clear')



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
