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
firstMouse = True
def normalize(v):
    norm=np.linalg.norm(v, ord=1)
    if norm==0:
        norm=np.finfo(v.dtype).eps
    return v/norm
       
class cidade:



    def __init__(self):
        self.pontos = {}
        self.camera_pos = np.array([0,0.5,0.25],dtype=np.float64)
        self.camera_front= np.array([-0.1,0,.1],dtype=np.float64)
        self.camera_up = np.array([0,1,0])
        self.last_x = int(w/2)
        self.last_y = int(h/2)
        self.x ,self.y = self.last_x,self.last_y
        self.yaw = 0
        self.pitch = 0
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
        # glutIdleFunc(self.camera)
        glViewport(0, 0, w, h)
        # glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LEQUAL)
        glClearDepth(1.0)
        glMatrixMode(GL_PROJECTION)
        # glutSetCursor(GLUT_CURSOR_NONE)
        glOrtho(-w/2, w/2, -h/2, h/2, -depth, depth)
        glClearColor(0, 0, 0, 0)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutPassiveMotionFunc(self.motion)
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)
        # glCullFace(GL_FRONT_AND_BACK)
        
        

    def keyboard(self, key, x, y):
        global firstMouse
        key = key.decode('utf8').lower()
        speed = 0.1
        if key == chr(27):
            # os.system('clear')
            sys.exit()
        elif key == 'w':
            self.camera_pos += speed * self.camera_front
        elif key == 'a':
            self.camera_pos -= np.cross(self.camera_front,self.camera_up) * speed
        elif key == 's':
            self.camera_pos -= speed * self.camera_front
        elif key == 'd':
            self.camera_pos += np.cross(self.camera_front,self.camera_up) * speed 
        elif key == 'q':
            glutWarpPointer(int(w/2),int(h/2))
            firstMouse=True


        # elif key =='l':
        #     self.yaw+=1
        #     self.camera_front[0] = cos(np.radians(self.yaw)) * cos(np.radians(self.pitch))
        #     self.camera_front[1] = sin(np.radians(self.pitch))
        #     self.camera_front[2] = sin(np.radians(self.yaw)) * cos(np.radians(self.pitch))
        #     self.camera_front = normalize(self.camera_front)
        # elif key =='k':
        #     self.pitch+=1   
        #     self.camera_front[0] = cos(np.radians(self.yaw)) * cos(np.radians(self.pitch))
        #     self.camera_front[1] = sin(np.radians(self.pitch))
        #     self.camera_front[2] = sin(np.radians(self.yaw)) * cos(np.radians(self.pitch))
        #     self.camera_front = normalize(self.camera_front)
        self.camera()

   

    def motion(self, x, y):
        global firstMouse
        print(x,y)
        sensitivity = 0.5
        # x = x-(w/2)
        # y = (h/2)-y
        if firstMouse:
            self.last_x = x
            self.last_y = y
            firstMouse = False
        dx = (x - self.last_x) 
        dy = (self.last_y - y) 
        
        self.last_x , self.last_y = x,y

        dx *= sensitivity
        dy *= sensitivity
        
        # if x>512:
        #     self.yaw +=1*s
        # elif 512 < 0:
        #     self.yaw -=1*s

        # if y > 512 :
        #     self.pitch-=1*s
        # elif y < 512 :
        #     self.pitch+=1*s
        # glutWarpPointer(int(w/2),int(h/2))
        self.yaw += dx
        self.pitch -=dy
        # if self.yaw > 180:
        #     self.yaw = 180
        # elif self.yaw < -180:
        #     self.yaw = -180
        # if self.pitch < -180:
        #     self.pitch = -180
        # elif self.pitch > 180:
        #     self.pitch = 180
        
        self.camera_front[0] = cos(np.radians(self.yaw)) * cos(np.radians(self.pitch))
        self.camera_front[1] = sin(np.radians(self.pitch))
        self.camera_front[2] = sin(np.radians(self.yaw)) * cos(np.radians(self.pitch))
        # self.camera_front = normalize(self.camera_front)
        # glutWarpPointer(int(w/2),int(h/2))
        self.camera()

    def mouse(self, tp1, tp2, x, y):
        return
        x = x-(w/2)
        y = (h/2)-y
        print("mouse_click: ", x, y, sep=" ", end="\n")

    def camera(self):
        # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # glMatrixMode(GL_PROJECTION)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(0.45,1, 1, 100)
        self.camera_pos[1]=.5
        print('-------------------------------------')
        print('cameraPos:',self.camera_pos)
        print('cameraFront:',self.camera_front)
        print('cameraTarget:',self.camera_front+self.camera_pos)
        print('cameraUp',self.camera_up)
        print('-------------------------------------')
        # glLoadIdentity()
        gluLookAt(*self.camera_pos,*(self.camera_pos+self.camera_front),*self.camera_up)
        glutPostRedisplay()
        # os.system('clear')



    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.cube1()
        # self.cube2()
        self.axis()
        self.casa()
        glFlush()
        glutSwapBuffers()

    
    def telhado(self):
        glBegin(GL_TRIANGLES)
        glColor4f(0.21,0.0,0.0,1.0)
        for x,y,z in self.pontos['telhado']:
            glVertex3f(x,y,z)
        glEnd()
        glBegin(GL_QUADS)
        glColor4f(0.21,0.0,0.0,1.0)
        for x,y,z in self.pontos['forro']:
            glVertex3f(x,y,z)
        glEnd()
    
    def paredes(self):
        glBegin(GL_QUADS)
        glColor4f(0.42,0.26,0.17,1.0)
        # Estrutura da casa
        for x,y,z in self.pontos['casa']:
            glVertex3f(x,y,z)
        glEnd()

    def porta(self):
        # Porta
        glBegin(GL_QUADS)
        glColor4f(0.0,0.0,0.0,1.0)
        for x,y,z in self.pontos['contorno_porta']:
            glVertex3f(x,y,z)
        glEnd()
        glBegin(GL_QUADS)
        glColor4f(0.82,0.24,0.15,1.0)
        for x,y,z in self.pontos['porta']:
            glVertex3f(x,y,z)
        glEnd()
        glBegin(GL_QUADS)
        glColor4f(0.21,0.0,0.0,1.0)
        for x,y,z in self.pontos['macaneta']:
            glVertex3f(x,y,z)
        glEnd()
    def janela(self):
        glBegin(GL_QUADS)
        glColor4f(0.38,0.62,0.76,1.0)
        for x,y,z in self.pontos['janela_direita_frente']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['janela_esquerda_frente']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['janela_direita']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['janela_esquerda']:
            glVertex3f(x,y,z)
        

        glColor4f(0.0,0.0,0.0,1.0)
        for x,y,z in self.pontos['grade_janela_direita_frente_1']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['grade_janela_direita_frente_2']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['grade_janela_esquerda_frente_1']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['grade_janela_esquerda_frente_2']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['grade_janela_direita_1']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['grade_janela_direita_2']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['grade_janela_esquerda_1']:
            glVertex3f(x,y,z)
        for x,y,z in self.pontos['grade_janela_esquerda_2']:
            glVertex3f(x,y,z)
        glEnd()

    def casa(self):
        self.telhado()
        self.paredes()
        self.porta()
        self.janela()
        

    def inicializa(self):
        self.pontos['casa']=[[-0.55, 0.25, 0.0],[0.55, 0.25, 0.0],[0.55, 0.75, 0.0],[-0.55, 0.75, 0.0],[-0.55, 0.25, 0.60],[0.55, 0.25, 0.60],[0.55, 0.75, 0.60],[-0.55, 0.75, 0.60],[-0.55, 0.25, 0.0], [-0.55, 0.25, 0.60], [-0.55, 0.75, 0.60], [-0.55, 0.75, 0.0],[0.55, 0.25, 0.60], [0.55, 0.25, 0.0], [0.55, 0.75, 0.0], [0.55, 0.75, 0.60],[-0.55, 0.75, 0.0], [0.55, 0.75, 0.0], [-0.55, 0.75, 0.60], [0.55, 0.75, 0.60]]
        self.pontos['telhado']=[[-0.80,0.75, 0.0], [0.80,0.75, 0.0], [0.05,1.0,0.25],[0.80,0.75, 0.0], [0.80,0.75, 0.60], [0.05,1.0,0.25],[-0.80,0.75, 0.60], [0.80,0.75, 0.60], [0.05,1.0,0.25],[-0.80,0.75, 0.0], [-0.80,0.75, 0.60], [0.05,1.0,0.25]]
        self.pontos['forro'] = [[-0.80,0.75, 0.0], [0.80,0.75,0.60], [-0.80,0.75,0.60], [0.80,0.75, 0.0]]     
        self.pontos['porta'] = [[-0.10,0.25,0.0],[0.10,0.25,0.0],[0.10,0.57,0.0],[-0.10,0.57,0.0]]
        self.pontos['macaneta'] = [[-0.08,0.40,0.0],[-0.06,0.40,0.0],[-0.06,0.42,0.0],[-0.08,0.42,0.0]]       
        self.pontos['contorno_porta'] = [[-0.11,0.25,0.0],[0.11,0.25,0.0],[0.11,0.58,0.0],[-0.11,0.58,0.0]]
        self.pontos['janela_direita_frente'] = [[0.20,0.4,0.0], [0.20,0.58,0.0], [0.40,0.58,0.0], [0.40,0.4,0.0]]
        self.pontos['grade_janela_direita_frente_1'] = [[0.29,0.4,0.0], [0.29,0.58,0.0], [0.31,0.58,0.0], [0.31,0.4,0.0]]
        self.pontos['grade_janela_direita_frente_2'] = [[0.20,0.48,0.0], [0.20,0.50,0.0], [0.40,0.50,0.0], [0.40,0.48,0.0]]
        self.pontos['janela_esquerda_frente'] = [[-0.20,0.4,0.0], [-0.20,0.58,0.0], [-0.40,0.58,0.0], [-0.40,0.4,0.0]]
        self.pontos['grade_janela_esquerda_frente_1'] = [[-0.29,0.4,0.0], [-0.29,0.58,0.0], [-0.31,0.58,0.0], [-0.31,0.4,0.0]]
        self.pontos['grade_janela_esquerda_frente_2'] = [[-0.20,0.48,0.0], [-0.20,0.50,0.0], [-0.40,0.50,0.0], [-0.40,0.48,0.0]]
        self.pontos['janela_direita'] = [[0.55,0.4,0.2],[0.55,0.4,0.4],[0.55,0.6,0.4],[0.55,0.6,0.2]]
        self.pontos['grade_janela_direita_1'] = [[0.55,0.4,0.29],[0.55,0.4,0.31],[0.55,0.6,0.31],[0.55,0.6,0.29]]
        self.pontos['grade_janela_direita_2'] = [[0.55,0.49,0.2],[0.55,0.49,0.4],[0.55,0.51,0.4],[0.55,0.51,0.2]]
        self.pontos['janela_esquerda'] = [[-0.55,0.4,0.2],[-0.55,0.4,0.4],[-0.55,0.6,0.4],[-0.55,0.6,0.2]]
        self.pontos['grade_janela_esquerda_1'] = [[-0.55,0.4,0.29],[-0.55,0.4,0.31],[-0.55,0.6,0.31],[-0.55,0.6,0.29]]
        self.pontos['grade_janela_esquerda_2'] = [[-0.55,0.49,0.2],[-0.55,0.49,0.4],[-0.55,0.51,0.4],[-0.55,0.51,0.2]]

        glutWarpPointer(int(w/2),int(h/2))
        if full:
            glutFullScreenToggle()
        self.camera()
        self.axis()
        self.cube1()


    def axis(self):
        vertex = (((0.1,0,0),(255,0,0)),((0,0.1,0),(0,255,0)),((0,0,0.1),(0,0,255)))
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


    def cube1(self):
        vertex = ((-0.25, 0.25, -0.25), (0.25, 0.25, -0.25), (-0.25, -0.25, -0.25), (0.25, -0.25, -0.25),
                  (-0.25, 0.25, 0.25), (0.25, 0.25, 0.25), (-0.25, -0.25, 0.25), (0.25, -0.25, 0.25))
        edges = ((0, 1, 3, 2), (1,5,7,3), (5,5,6,7),
                 (4,0,2,6),( 2,3,7,6), (4,5,1,0))
        glColor3f(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        for edge in edges:
            glBegin(GL_QUADS)
            for v in edge:
                glVertex3fv(vertex[v])
            glEnd()

    def cube2(self):
        vertex = ((0.3, 0.6, 0.3), (0.6, 0.6, 0.3), (0.3, 0.3, 0.3), (0.6, 0.3, 0.3),
                  (0.3, 0.6, 0.6), (0.6, 0.6, 0.6), (0.3, 0.3, 0.6), (0.6, 0.3, 0.6))
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
