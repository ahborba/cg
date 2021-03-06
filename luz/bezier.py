from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
from transformacao import *

cos = math.cos
pi = math.pi
sin = math.sin
sqrt = math.sqrt


class github:


    def __init__(self):
        self.pontos = {}
        self.w = 1024
        self.h = 1024
        self.sides = 50
        self.keybindings = {chr(27): exit}
        glutInit()
        glutInitWindowSize(self.w, self.h)
        self.git = glutCreateWindow('Github')
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
        glClearColor(0, 0, 0, 0)
        glutReshapeFunc(self.reshape)
        glutKeyboardFunc(self.keyboard)
        glutDisplayFunc(self.display)
        glutIdleFunc(self.display)
        glutMouseFunc(self.mouse)
        # glOrtho(0.0, self.w, 0.0, self.h, 0.0, 1.0)
        self.ctrlPoints = [[100,100,0],[130,200,0],[170,200,0],[200,100,0]]
        glClearColor(0, 0, 0, 0)
        glShadeModel(GL_FLAT)
        glMap1f(GL_MAP1_VERTEX_3, 1, 0, self.ctrlPoints)
        glEnable(GL_MAP1_VERTEX_3)
        self.indice=0
        self.linha=0
        self.rotacao = False
        self.teste ,self.print= False,False
        self.operacao = 'orelha_direita'
        self.alpha = 0
        self.transf = Transformacao(self.w,self.h)

    def transformacao_rotacao(self):
        self.transformacao('rotacao')
        


    def transformacao_centro(self,op,mat,dx=0,dy=0):
        if op =='translacao':
            mat = self.transf.translacao(mat,dx,dy)
        elif op =='escala':
            mat  =self.transf.escala(mat,dx,dy,mat[0][0],mat[0][1])
        elif op == 'rotacao':
            mat = self.transf.rotacao(mat,mat[0][0],mat[0][1])
        return mat

    def transformacao_bezier(self,op,mat,dx,dy,dados):
        if op =='rotacao' or op=='escala':
            dX = self.pontos['fundo_preto'][0][0] 
            dY = self.pontos['fundo_preto'][0][1]

        nova_mat = []
        for linha in mat:
            if op =='translacao':
                nova_mat.append(self.transf.translacao(linha,dx,dy))
            elif op =='escala':
                nova_mat.append(self.transf.escala(linha,dx,dy,dX,dY))
            elif op =='rotacao':
                nova_mat.append(self.transf.rotacao(linha,dX,dY))
        return nova_mat

    def transformacao_lin(self,op,linha,dx,dy,dados):
        if op =='rotacao' or op=='escala':
            dX = self.pontos['fundo_preto'][0][0] 
            dY = self.pontos['fundo_preto'][0][1]


        if op =='translacao':
            return self.transf.translacao(linha,dx,dy)
        elif op =='escala':
            return self.transf.escala(linha,dx,dy,dX,dY)
        else:
            return self.transf.rotacao(linha,dX,dY)
        

    def transformacao_letras(self,op,dx=0,dy=0):
        if op =='rotacao' or op=='escala':
            dX = self.pontos['fundo_preto'][0][0] 
            dY = self.pontos['fundo_preto'][0][1]
        self.pontos['g']=self.transformacao_lin(op,self.pontos['g'],dx,dy,'g')
        self.pontos['i']=self.transformacao_bezier(op,self.pontos['i'],dx,dy,'i')
        self.pontos['t']=self.transformacao_bezier(op,self.pontos['t'],dx,dy,'t')
        self.pontos['h']=self.transformacao_bezier(op,self.pontos['h'],dx,dy,'h')
        self.pontos['u']=self.transformacao_lin(op,self.pontos['u'],dx,dy,'u')
        self.pontos['b']=self.transformacao_lin(op,self.pontos['b'],dx,dy,'b')

        

    def transformacao(self,op,dx=0,dy=0):
        self.pontos['cabeca'] = self.transformacao_bezier(op,self.pontos['cabeca'] ,dx,dy,'cabeca')
        self.pontos['orelha_esquerda'] = self.transformacao_bezier(op,self.pontos['orelha_esquerda'] ,dx,dy,'orelha_esquerda')
        self.pontos['orelha_direita'] = self.transformacao_bezier(op,self.pontos['orelha_direita'] ,dx,dy,'orelha_direita')
        self.pontos['braco'] = self.transformacao_bezier(op,self.pontos['braco'] ,dx,dy,'braco')
        self.pontos['pescoco'] = self.transformacao_bezier(op,self.pontos['pescoco'] ,dx,dy,'pescoco')
        self.pontos['fundo_preto'] =  self.transformacao_centro(op,self.pontos['fundo_preto'],dx,dy)
        self.pontos['tentaculo'] = self.transformacao_bezier(op,self.pontos['tentaculo'],dx,dy,'tentaculo')
        self.transformacao_letras(op,dx,dy)


    def keyboard(self,arg,arg1,arg2):
        letra = arg.decode('utf8')
        dx = 0
        dy = 0
        translacao = False
        escala = False
            
        if letra=='d':
            dx, translacao = 0.01, True
        elif letra =='a':
            dx, translacao = -.01, True
        elif letra =='w':
            dy, translacao = .01, True
        elif letra == 's':
            dy, translacao = -.01, True
        
        if letra =='+':
            dx,dy,escala=1.1,1.1,True
        elif letra =='-':
            dx,dy,escala=.9,.9,True
        elif letra =='q':
            self.inicializa()      
        elif letra == 'r':
            if self.rotacao:
                self.rotacao = False
            else:
                self.rotacao = True
        elif letra =='e':
            if self.print:
                self.print = False
            else:
                self.print = True
        if translacao:
            self.transformacao('translacao',dx,dy)
        elif escala:
            self.transformacao('escala',dx,dy)


    def reshape(self,rsp1,rsp2):
        pass

    def substitui(self,tp2,x,y):
        y = self.h-y
        if tp2==0:
            self.indice = 0
            self.linha =0
            menor = 1025
            j=0
            for pontos in self.pontos[self.operacao]:
                i = 0
                for ponto in pontos:
                    px = ponto[0]
                    py = ponto[1]
                    euclidiana = sqrt((x-px)**2+(y-py)**2)
                    if euclidiana < menor:
                        self.indice = i
                        self.linha=j
                        menor = euclidiana
                    i+=1
                j+=1
        else:
            self.pontos[self.operacao][self.linha][self.indice] = [x,y,0]

    def mouse(self,tp1,tp2,x,y):
        if self.teste:
            self.substitui(tp2,x,y)
        elif tp2==1:
            print('[',x,',',self.h-y,',',0,'],',sep='')
        

    def letra_q(self,letra):
        mat = self.pontos[letra]
        glColor3f(0, 0, 0)
        for linha in mat:
            glBegin(GL_QUADS)  # Begin the sketch
            p0,p1,p2,p3 = linha[0],linha[1],linha[2],linha[3]


            glVertex2f(p0[0],p0[1])
            glVertex2f(p1[0],p1[1])
            glVertex2f(p2[0],p2[1])
            glVertex2f(p3[0],p3[1])
            glEnd()  # Mark the end of drawing


    

    def i (self):
        vet = self.pontos['i'][0]
        glColor3f(0, 0, 0)
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(vet[0][0],vet[0][1])  # Coordinates for the bottom left point
        glVertex2f(vet[1][0],vet[1][1])  # Coordinates for the bottom right point
        glVertex2f(vet[2][0],vet[2][1])  # Coordinates for the top right point
        glVertex2f(vet[3][0],vet[3][1])  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
        self.circle(self.pontos['i'][1])


    def letra(self,l):
        vet = self.pontos[l]
        glColor3f(0, 0,0)
        glBegin(GL_POLYGON)
        p1,p2,p3 =vet[0],vet[1],vet[2]
        glVertex3fv(p1)
        glVertex3fv(p2)
        glVertex3fv(p3)
        # 123,234,345
        glEnd()
        for i in range(3,len(vet)):
            p4 = vet[i]
            glBegin(GL_POLYGON)
            glVertex3fv(p2)
            glVertex3fv(p3)
            glVertex3fv(p4)
            glEnd()
            p2,p3  = p3,p4


    def circle(self,circulo):
        x = circulo[0][0]
        y = circulo[0][1]
        x1 = circulo[1][0]
        y1 = circulo[1][1]
        raio = sqrt(((x-x1)**2)+((y-y1)**2) )
        glColor3f(0, 0, 0)
        glBegin(GL_POLYGON)
        for i in range(100):
            cosine = raio * cos(i*2*pi/self.sides) + x
            sine = raio * sin(i*2*pi/self.sides) + y
            glVertex2f(cosine, sine)
        glEnd()


    def bezier(self,pontos,tipo):
        glClearColor(0.0,0.0,0.0,0.0)
        glColor3f(255, 255, 255)
        glMap2d(GL_MAP2_VERTEX_3,0, 1, 1, 0,pontos)
        glEnable(GL_MAP2_VERTEX_3)
        glMapGrid2f(20, 0.0, 1.0, 20, 0.0, 1.0)
        glPushMatrix()
        glEvalMesh2(GL_FILL,0,20,0,20)
        glPopMatrix()
        if self.print:
            glPointSize(10)
            glBegin(GL_POINTS)
            glColor3f(255, 0,0)
            i = 0
            for lista in pontos:
                if i==1:
                    glColor(0,255,0)
                elif i ==2:
                    glColor(0,0,255)
                elif i ==3:
                    glColor(255,255,0)
                for ponto in lista:
                    glVertex3fv(ponto)
                i+=1
                
            glEnd()

    def ellipse(self,x,y,a=0.015,b=0.012):
        d2r = pi/180.0
        glColor(0,0,0)
        # print('[[',x,',',y,',',0,']',sep='',end=',')
        # print('[',a,',',b,',',0,']],',sep='',end='')
        glBegin(GL_POLYGON)
        for i in range(0,360):
            rad = i*d2r
            glVertex2f(cos(rad)*a+ x,sin(rad)*b + y)
        glEnd()

    def tentaculo(self):
        i = 0
        for t in self.pontos['tentaculo']:
            self.circle(t)
            

    def fundo_branco(self):
        glColor3f(255, 255, 255)
        glBegin(GL_QUADS)  # Begin the sketch
        glVertex2f(-self.w, self.h)  # Coordinates for the bottom left point
        glVertex2f(self.w, self.h)  # Coordinates for the bottom right point
        glVertex2f(self.w, -self.h)  # Coordinates for the top right point
        glVertex2f(-self.w,-self.h)  # Coordinates for the top left point
        glEnd()  # Mark the end of drawing
    


    def display(self):
        # fundo branco
        self.fundo_branco()
        # fundo preto
        self.circle(self.pontos['fundo_preto'])
        self.bezier(self.pontos['cabeca'],'cabeca')
        self.bezier(self.pontos['orelha_esquerda'],'orelha_esquerda')
        self.bezier(self.pontos['orelha_direita'],'orelha_direita')
        self.bezier(self.pontos['braco'],'braco')
        self.bezier(self.pontos['pescoco'],'pescoco')
        self.tentaculo()
        self.letra('g')
        self.i()
        self.letra_q('t')
        self.letra_q('h')
        self.letra('u')
        self.letra('b')
        if self.rotacao:
            self.transformacao_rotacao()
        glFlush()


    def inicializa(self):
        self.pontos['fundo_preto'] = [[0,0,0],[0.590,0,0]] # adiciona o fundo preto
        self.pontos['cabeca']= [[[-0.302734375, 0.2421875, 0], [-0.1640625, 0.3671875, 0], [0.091796875, 0.36328125, 0], [0.232421875, 0.294921875, 0], [0.296875, 0.224609375, 0]], [[-0.390625, 0.158203125, 0], [0.041015625, 0.166015625, 0], [-0.14453125, 0.1171875, 0], [0.197265625, 0.146484375, 0], [0.37109375, 0.125, 0]], [[-0.404296875, 0.005859375, 0], [-0.12109375, 0.033203125, 0], [0.044921875, -0.03125, 0], [0.21484375, -0.060546875, 0], [0.373046875, -0.0078125, 0]], [[-0.341796875, -0.130859375, 0], [-0.23828125, -0.263671875, 0], [0.056640625, -0.28515625, 0], [0.232421875, -0.23046875, 0], [0.3203125, -0.107421875, 0]]]
        self.pontos['orelha_esquerda']= [[[-0.34765625, 0.263671875, 0], [-0.337890625, 0.326171875, 0], [-0.359375, 0.435546875, 0], [-0.2578125, 0.349609375, 0], [-0.1875, 0.298828125, 0], [-0.13671875, 0.279296875, 0]], [[-0.34765625, 0.173828125, 0], [-0.283203125, 0.2578125, 0], [-0.279296875, 0.2578125, 0], [-0.236328125, 0.29296875, 0], [-0.19140625, 0.29296875, 0], [-0.13671875, 0.306640625, 0]], [[-0.3125, 0.193359375, 0], [-0.267578125, 0.201171875, 0], [-0.22265625, 0.216796875, 0], [-0.18359375, 0.24609375, 0], [-0.158203125, 0.2578125, 0], [-0.119140625, 0.2578125, 0]]]
        self.pontos['orelha_direita']= [[[0.150390625, 0.3046875, 0], [0.15625, 0.369140625, 0], [0.384765625, 0.322265625, 0], [0.23046875, 0.484375, 0], [0.349609375, 0.263671875, 0], [0.294921875, 0.20703125, 0]], [[0.1015625, 0.296875, 0], [0.26953125, 0.20703125, 0], [0.20703125, 0.23046875, 0], [0.158203125, 0.263671875, 0], [0.119140625, 0.279296875, 0], [0.294921875, 0.212890625, 0]]]
        self.pontos['braco']= [[[-0.16015625, -0.31640625, 0], [-0.2578125, -0.376953125, 0], [-0.32421875, -0.306640625, 0], [-0.361328125, -0.240234375, 0], [-0.40234375, -0.203125, 0], [-0.462890625, -0.212890625, 0]], [[-0.169921875, -0.40234375, 0], [-0.22265625, -0.396484375, 0], [-0.31640625, -0.439453125, 0], [-0.33203125, -0.3671875, 0], [-0.40234375, -0.302734375, 0], [-0.3671875, -0.314453125, 0]]]
        self.pontos['pescoco']= [[[-0.271484375, -0.546875, 0], [-0.185546875, -0.564453125, 0], [-0.16796875, -0.5234375, 0], [-0.1484375, -0.54296875, 0], [-0.2109375, -0.30078125, 0], [-0.1171875, -0.216796875, 0]], [[-0.07421875, -0.564453125, 0], [-0.064453125, -0.486328125, 0], [-0.060546875, -0.40234375, 0], [-0.056640625, -0.333984375, 0], [-0.052734375, -0.28515625, 0], [-0.05078125, -0.234375, 0]], [[0.068359375, -0.705078125, 0], [0.0625, -0.45703125, 0], [0.060546875, -0.404296875, 0], [0.060546875, -0.345703125, 0], [0.064453125, -0.275390625, 0], [0.056640625, -0.234375, 0]], [[0.193359375, -0.560546875, 0], [0.125, -0.544921875, 0], [0.12109375, -0.55078125, 0], [0.1328125, -0.560546875, 0], [0.1640625, -0.279296875, 0], [0.064453125, -0.228515625, 0]]]
        self.pontos['g']= [[-0.18548632812500015, 0.12132421875000005, 0], [-0.19098632812500013, 0.09983984375000005, 0], [-0.1962929687500001, 0.12330078125000005, 0], [-0.20376953125000016, 0.10063476562500001, 0], [-0.20376953125000016, 0.12474023437500009, 0], [-0.21663867187500005, 0.10108593750000011, 0], [-0.21062304687500008, 0.12613671875000004, 0], [-0.21663867187500005, 0.10108593750000011, 0], [-0.21590820312500011, 0.12675976562500008, 0], [-0.21663867187500005, 0.10108593750000011, 0], [-0.22093554687500014, 0.12691015625000007, 0], [-0.22454492187500005, 0.1011289062500001, 0], [-0.2268437500000001, 0.126673828125, 0], [-0.23047460937500017, 0.10046289062500008, 0], [-0.2335898437500001, 0.1255566406250001, 0], [-0.2353085937500001, 0.09883007812500005, 0], [-0.23954101562500005, 0.12437500000000007, 0], [-0.23625390625000006, 0.09848632812499997, 0], [-0.24671679687500012, 0.12229101562499994, 0], [-0.24074414062500013, 0.09635937499999997, 0], [-0.25438671875, 0.11855273437500008, 0], [-0.24628710937500006, 0.09201953125000002, 0], [-0.26139062500000004, 0.11208593750000001, 0], [-0.24890820312500014, 0.088625, 0], [-0.2689746093750001, 0.10710156249999997, 0], [-0.25109960937500003, 0.08523046875, 0], [-0.2734218750000001, 0.10233203125000007, 0], [-0.25314062500000006, 0.08166406250000006, 0], [-0.2774179687500001, 0.097283203125, 0], [-0.25434375000000004, 0.07841992187500006, 0], [-0.2808125000000001, 0.09113867187499998, 0], [-0.2553320312500001, 0.07650781249999998, 0], [-0.2828964843750001, 0.086498046875, 0], [-0.25657812500000016, 0.07289843749999995, 0], [-0.28465820312500006, 0.08063281250000003, 0], [-0.2574160156250001, 0.06993359375000002, 0], [-0.285796875, 0.07498242187499997, 0], [-0.25829687500000004, 0.06350976562500005, 0], [-0.28663476562500007, 0.06226367187499998, 0], [-0.25915625000000003, 0.05435742187499998, 0], [-0.28657031250000015, 0.04471093750000004, 0], [-0.2586191406250001, 0.043335937500000025, 0], [-0.28652734375000005, 0.03403320312500007, 0], [-0.2568574218750001, 0.03463476562500006, 0], [-0.2847656250000001, 0.025417968749999957, 0], [-0.25455859375000006, 0.02674999999999999, 0], [-0.28302539062500004, 0.01933789062500007, 0], [-0.2540859375, 0.02195898437500004, 0], [-0.28064062500000003, 0.014095703124999909, 0], [-0.25258203125000006, 0.022109375000000035, 0], [-0.2773750000000001, 0.0075000000000000015, 0], [-0.25215234375, 0.021292968750000023, 0], [-0.2737226562500001, 0.0021933593750000334, 0], [-0.2507773437500001, 0.019187500000000073, 0], [-0.27085019531250004, -0.002253906250000052, 0], [-0.249251953125, 0.017447265624999923, 0], [-0.2666757812500001, -0.005433593749999913, 0], [-0.24648046875000004, 0.014246093750000017, 0], [-0.2615195312500001, -0.010160156250000081, 0], [-0.24312890625000003, 0.010830078125000081, 0], [-0.25520312500000003, -0.013726562500000013, 0], [-0.24300000000000008, 0.010550781250000025, 0], [-0.24895117187500002, -0.016498046874999978, 0], [-0.23928320312500015, 0.008574218750000024, 0], [-0.2425488281250002, -0.0187324218750001, 0], [-0.23406250000000015, 0.006554687499999929, 0], [-0.23543750000000005, -0.020042968749999973, 0], [-0.2273593750000001, 0.005093750000000058, 0], [-0.22860546875000018, -0.020623046875000023, 0], [-0.2219882812500001, 0.004212890625000017, 0], [-0.21936718750000014, -0.0202578125, 0], [-0.21631640625000012, 0.004363281250000014, 0], [-0.21283593750000004, -0.019763671875000027, 0], [-0.2094199218750001, 0.005093750000000058, 0], [-0.2062187500000001, -0.018388671875000012, 0], [-0.2052089843750001, 0.006919921875000063, 0], [-0.1996875000000001, -0.016562500000000008, 0], [-0.2033828125000001, 0.009455078124999955, 0], [-0.1940156250000001, -0.015187499999999994, 0], [-0.2033828125000001, 0.009455078124999955, 0], [-0.18864453125000008, -0.012931640625000048, 0], [-0.2033828125000001, 0.009455078124999955, 0], [-0.18355273437500014, -0.010031250000000021, 0], [-0.2033828125000001, 0.009455078124999955, 0], [-0.18093164062500006, -0.006958984375000034, 0], [-0.2033828125000001, 0.009455078124999955, 0], [-0.1802871093750001, -0.0013730468750000092, 0], [-0.2025234375000001, 0.013300781250000055, 0], [-0.17934179687500001, 0.012226562500000033, 0], [-0.2020722656250001, 0.021658203125000046, 0], [-0.17919140625000002, 0.03270117187500004, 0], [-0.20301757812500018, 0.032851562500000035, 0], [-0.17934179687500001, 0.05523828125000002, 0], [-0.20258789062500013, 0.033367187500000055, 0], [-0.20288867187500012, 0.05581835937500007, 0], [-0.2108808593750001, 0.036482421875, 0], [-0.22372851562500004, 0.055667968750000074, 0], [-0.2258339843750001, 0.03858789062500006, 0], [-0.23397656250000018, 0.056033203124999986, 0], [-0.23296679687500008, 0.039318359374999994, 0]]
        self.pontos['i']= [[[-0.16228320312500005, 0.08409179687500005, 0], [-0.1366308593750001, 0.08387695312500003, 0], [-0.1370820312500001, -0.01783007812500001, 0], [-0.16228320312500005, -0.01783007812500001, 0]], [[-0.149349609375, 0.11260156250000003, 0], [-0.13422460937499991, 0.11369726562499999, 0]]]
        self.pontos['t']= [[[-0.10614453125000001, 0.1030625, 0], [-0.08274804687499991, 0.10886328124999994, 0], [-0.07916015624999993, -0.01993554687499996, 0], [-0.10610156249999991, -0.01993554687499996, 0]], [[-0.12275195312499998, 0.08407031250000001, 0], [-0.05984570312499993, 0.08428515625000003, 0], [-0.058814453125, 0.06106054687500001, 0], [-0.12275195312499998, 0.06106054687500001, 0]], [[-0.08059960937499998, 0.0028808593749999854, 0], [-0.05728906249999999, 0.002021484375000101, 0], [-0.05690234375000003, -0.020966796875, 0], [-0.07855859374999995, -0.02077343750000002, 0]]]
        self.pontos['h']= [[[-0.044376953125, 0.12431054687500004, 0], [-0.04474218750000002, -0.018861328124999938, 0], [-0.016447265624999978, -0.018861328124999938, 0], [-0.016447265624999978, 0.12431054687500004, 0]], [[-0.016447265624999978, 0.06733398437499999, 0], [-0.016447265624999978, 0.04133789062499998, 0], [0.03842382812500004, 0.04133789062499998, 0], [0.03842382812500004, 0.06733398437499999, 0]], [[0.03842382812500004, 0.12431054687500004, 0], [0.03842382812500004, -0.018861328124999938, 0], [0.06368945312500013, -0.018861328124999938, 0], [0.06368945312500013, 0.12431054687500004, 0]]]
        self.pontos['u']= [[0.11048242187500007, 0.08443554687500003, 0], [0.08382031250000006, 0.084521484375, 0], [0.11031054687500003, 0.04559179687500008, 0], [0.08465820312500012, 0.04511914062500005, 0], [0.11114843750000009, 0.020626953125000007, 0], [0.08590429687500006, 0.00846679687500001, 0], [0.11162109375000012, 0.009712890625000076, 0], [0.08732226562500006, -0.0009218750000000199, 0], [0.1126738281250001, 0.007242187499999992, 0], [0.08979296875000004, -0.007861328125000013, 0], [0.11353320312500009, 0.005523437500000001, 0], [0.09207031250000003, -0.011750000000000012, 0], [0.11608984375000002, 0.0038261718750000583, 0], [0.0950996093750001, -0.015359374999999927, 0], [0.11647656250000009, 0.003052734375000029, 0], [0.09948242187500005, -0.017550781250000064, 0], [0.11428515625000008, 0.004771484375000018, 0], [0.10450976562500007, -0.019720703125000044, 0], [0.11666992187499996, 0.003353515624999911, 0], [0.11106250000000012, -0.020966796875, 0], [0.12096679687500005, 0.0019140624999999765, 0], [0.11875390625000008, -0.021052734375000076, 0], [0.12625195312500007, 0.0012695312500000076, 0], [0.12683203125, -0.019527343749999954, 0], [0.13185937500000014, 0.002687500000000117, 0], [0.13413671875000002, -0.016111328124999907, 0], [0.13649999999999998, 0.004857421875000096, 0], [0.14105468750000008, -0.012416015625000028, 0], [0.14088281250000004, 0.00904687500000006, 0], [0.14685546875000002, -0.0067226562500000715, 0], [0.14249414062500013, 0.012742187499999941, 0], [0.14496484375, 0.02859765625000004, 0], [0.15132421875000004, -0.005197265624999951, 0], [0.14477148437500012, 0.084521484375, 0], [0.17012304687500004, 0.083962890625, 0], [0.17115429687500008, 0.0007753906250000352, 0], [0.15141015625, -0.005283203124999917, 0], [0.15398828125, -0.008054687499999881, 0], [0.17145507812499997, 0.0007753906250000352, 0], [0.15663085937500001, -0.016390624999999964, 0], [0.17306640625000005, -0.010031250000000021, 0], [0.17439843749999998, -0.01916210937500004, 0], [0.15929492187500008, -0.017916015624999976, 0], [0.16954296875, 0.08424218749999994, 0], [0.14438476562500005, 0.08510156250000005, 0], [0.156265625, -0.015832031250000073, 0], [0.17240039062500004, 0.0002167968750000325, 0], [0.14191406249999997, -0.007281249999999963, 0], [0.14477148437500012, 0.028039062499999927, 0]]
        self.pontos['b']= [[0.19235937500000003, 0.12411718750000006, 0], [0.19235937500000003, -0.012308593750000015, 0], [0.22028906250000002, 0.005416015624999987, 0], [0.19235937500000003, 0.12411718750000006, 0], [0.22028906250000002, 0.12411718750000006, 0], [0.19235937500000003, -0.012308593750000015, 0], [0.22196484375000003, 0.004298828124999984, 0], [0.20002929687500004, -0.016498046874999978, 0], [0.224328125, 0.00240820312500006, 0], [0.20905273437499994, -0.018302734375000046, 0], [0.228990234375, 0.0019140624999999765, 0], [0.22699218750000005, -0.01999999999999999, 0], [0.23754101562500007, 0.0016347656250000307, 0], [0.23809960937500008, -0.020107421875000003, 0], [0.24473828124999997, 0.003052734375000029, 0], [0.24598437499999992, -0.019333984374999974, 0], [0.2505390625, 0.0068554687500000325, 0], [0.25709179687500006, -0.016777343749999923, 0], [0.25281640625, 0.009906249999999945, 0], [0.26156054687499997, -0.014693359374999911, 0], [0.25414843750000005, 0.01332226562499999, 0], [0.26639453125, -0.008849609374999958, 0], [0.24834765625, 0.006017578124999973, 0], [0.27808203125, 0.0025048828124999943, 0], [0.25376171875, 0.013042968750000045, 0], [0.2822500000000001, 0.013214843749999977, 0], [0.257177734375, 0.021207031250000057, 0], [0.28283007812500005, 0.02015429687500008, 0], [0.25784375000000004, 0.027458984374999988, 0], [0.283302734375, 0.033925781249999946, 0], [0.25870312500000003, 0.035537109375000035, 0], [0.28272265625000004, 0.044560546875000044, 0], [0.25795117187500005, 0.04389453125000003, 0], [0.2815839843750001, 0.06041601562500004, 0], [0.2547285156250001, 0.05375585937499999, 0], [0.2770013671875, 0.07027734375, 0], [0.25034570312500004, 0.06022265624999995, 0], [0.271615234375, 0.07816210937500005, 0], [0.24379296875, 0.06402539062500007, 0], [0.26037890625000004, 0.08391992187500001, 0], [0.23726171875000002, 0.06344531250000002, 0], [0.2512265625, 0.08656250000000003, 0], [0.2382070312500001, 0.06391796875000005, 0], [0.24052734375000007, 0.08656250000000003, 0], [0.2303007812500001, 0.062048828125000066, 0], [0.2265625, 0.08065429687500007, 0], [0.22254492187500008, 0.05369140624999996, 0], [0.21897851562500004, 0.07678710937500004, 0], [0.1943144531250001, 0.050726562500000016, 0]]
        self.pontos["tentaculo"]=[[[-0.22009151488564382, -0.3566041425844769, 0], [-0.20909151488564381, -0.3456041425844769, 0]], [[-0.25009151488564385, -0.3566041425844769, 0], [-0.23909151488564384, -0.3456041425844769, 0]], [[-0.2800915148856439, -0.3466041425844769, 0], [-0.26909151488564387, -0.3356041425844769, 0]], [[-0.3100915148856439, -0.3266041425844769, 0], [-0.2990915148856439, -0.3156041425844769, 0]], [[-0.34009151488564393, -0.3066041425844769, 0], [-0.3290915148856439, -0.29560414258447687, 0]], [[-0.37009151488564396, -0.27660414258447685, 0], [-0.35909151488564395, -0.26560414258447684, 0]], [[-0.390091514885644, -0.25660414258447684, 0], [-0.37909151488564397, -0.24560414258447683, 0]]]

if __name__ == '__main__':
    git = github()
    git.inicializa()
    glutMainLoop()