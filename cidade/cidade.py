from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import random
cos = math.cos
pi = math.pi
sin = math.sin
sqrt = math.sqrt
w=500
h=500
depth=500
d = 10
class cidade:


    def __init__(self):
        self.pontos = {}
        self.x=0
        self.y=1
        self.z=0
        self.dir_x=0
        self.dir_y=0
        self.dir_z=0
        self.ang_x=0
        self.ang_y=0
        self.ang_z=0
        self.init_glut()
        self.teste ,self.print= False,False


    def init_glut(self):
        glutInit()
        glutInitWindowSize(w,h)
        glutCreateWindow('Cidade')
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA )
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutSpecialFunc(self.special)
        glutKeyboardFunc(self.keyboard)
        glViewport(0,0,w,h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-w,w,-h,h,-depth,depth)
        # glMatrixMode(GL_MODELVIEW)
        glClearColor(0, 0, 0, 0)


    def keyboard(self,key,x,y):
        key = key.decode('utf8').lower()
        if key == chr(27):
            sys.exit()
        elif key =='w':
            self.z +=d
        elif key =='s':
            self.z-=d
        elif key =='a':
            self.x +=d
        elif key =='d':
            self.x-=d
        self.camera()


    def special(self,key,x,y):
        if key == GLUT_KEY_LEFT:
            self.ang_y -=0.05
            self.dir_x = sin(self.ang_y)
            self.dir_z = -cos(self.ang_y)
        elif key == GLUT_KEY_RIGHT:
            self.ang_y+=0.05
            self.dir_x = sin(self.ang_y)
            self.dir_z = -cos(self.ang_y)
        elif key == GLUT_KEY_UP:
            self.x +=self.dir_x*d
            self.y +=self.dir_y*d
            self.z +=self.dir_z*d
        elif key == GLUT_KEY_DOWN:
            self.x -=self.dir_x*d
            self.y -=self.dir_y*d
            self.z -=self.dir_z*d
        self.camera(x,y)
    
    def cube(self):
        vertex = ((-50,50,-50),(50,50,-50),(-50,-50,-50),(50,-50,-50),(-50,50,50),(50,50,50),(-50,-50,50),(50,-50,50))
        edges = ((0,1),(1,3),(3,2),(2,0),(3,7),(7,5),(5,1),(5,4),(4,0),(4,6),(6,7),(6,2))
        glBegin(GL_LINES)
        glColor3f(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        for edge in edges:
            for v in edge:
                glVertex3fv(vertex[v])
        glEnd()
    def motion(self,x,y):
        self.camera(x,y)



    def mouse(self,tp1,tp2,x,y):
        print("mouse_click: ",x,y,sep=" ",end="\n")


    ''' x , y , z = posicao da camera
        x+dir_x , y+dir_y , z+dir_z = direcao em que a camera está olhando
        0 , 1 , 0 = não sei'''
    def camera(self,x=0,y=0):
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # gluLookAt(1, 1, 1, 0, 0, 0, 0, 1, 0)
        # gluLookAt(self.x, self.y, self.z,0,0,0 , 0, 1, 0)
        print('x: ',self.x,'\ny: ',self.y,'\nz: ',self.z)
        gluLookAt(self.x, self.y, self.z,self.x+self.dir_x,self.y+self.dir_y,self.dir_z+self.z, 0, 1, 0)


    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # self.fundo()
        # if self.x != 0:
        # self.casa()
        # self.telhado()
        self.cube()
        glFlush()



    def inicializa(self):
        self.camera()
        self.cube()
        self.pontos['casa']=[]
        self.pontos['telhado']=[]
        


if __name__ == '__main__':
    git = cidade()
    git.inicializa()
    glutMainLoop()