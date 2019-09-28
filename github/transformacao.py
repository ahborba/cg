from imagem import Imagem
import math
import numpy as np
import cv2


class Transformacao:
    def __init__(self):
        self.mat_escala = [[],[],[]]
        self.mat_translacao = [[],[],[]]

    def rotacao(self,linhas,alpha):
        mat_rotacao = np.array([[np.cos(np.deg2rad(alpha)),np.sin(np.deg2rad(alpha)),0],[-np.sin(np.deg2rad(alpha)),np.cos(np.deg2rad(alpha)),0],[0,0,1]])
        return self.multiplicar_matriz(linhas,mat_rotacao)

    def translacao(self,linhas,dx,dy):
        mat_translacao = np.array([[1,0,0],[0,1,0],[dx,dy,1]])
        return self.multiplicar_matriz(linhas,mat_translacao)
    def escala(self,linhas,dx,dy):
        mat_escala = np.array([[dx,0,0],[0,dy,0],[0,0,1]])
        return self.multiplicar_matriz(linhas,mat_escala)


    def multiplicar_matriz(self,linhas,mat):
        linhas_antes = linhas[:]
        linhas.clear()
        lin0 = True
        valor_antigo = None
        for linha in linhas_antes:
            p0 = linha[0]
            p1 = linha[1]
            pt0 = np.array(list(p0))
            pt1 = np.array(list(p1))
            pt0 = pt0@mat
            pt1 = pt1@mat
            linhas.append((tuple(pt0.astype(int)),tuple(pt1.astype(int))))
        return linhas

if __name__ == "__main__":
    print('Qual o tamanho de imagem desejado?')
    lin = int(input('linhas: '))
    col = int(input('colunas: '))
    img = Imagem(lin,col)
    t = Transformacao()
    linhas = [((int(col/2),int(lin*0.1),1),(int(col*0.1),int(lin*0.9),1)),((int(col/2),int(lin*0.1),1),(int(col*0.9),int(lin*0.9),1))]
    linhas = img.criar_letra(linhas)
    mat_inicial = img.mat
    cv2.imwrite('./A.jpg', img.mat)
    print('\nQual operacao deseja realizar? \n\ttranslacao\n\tescala\n\trotacao')
    while True:
        op = input('>>')
        if op == 'sair':
            break
        if op == 'reiniciar':
            print('\treiniciado...')
            img.mat = mat_inicial
        if op=='linhas':
            print(linhas)


        if op =='rotacao_tudo':  
            print('insira o angulo da rotacao: ')
            alpha = int(input('alpha: '))
            linhas = t.rotacao(linhas,alpha)   
        elif op == 'translacao':
            print('insira o dx e dy da operacao de ',op)
            dx = int(input('dx: '))
            dy = int(input('dy: '))
            linhas = t.translacao(linhas,dx,dy)
        if op=='rotacao_ancora':
            x = ((linhas[0])[0])[0]
            y = ((linhas[0])[0])[1]
            dx = -x
            dy = -y
            linhas = t.translacao(linhas,dx,dy)
            print('insira o angulo da rotacao: ')
            alpha = int(input('alpha: '))
            linhas = t.rotacao(linhas,alpha)
            linhas = t.translacao(linhas,x,y)
            
            
        elif op == 'escala':
            print('insira o dx e dy da operacao de ',op)
            dx = float(input('dx: '))
            dy = float(input('dy: '))
            linhas = t.escala(linhas,dx,dy)
        
        img.desenhar(linhas)
        cv2.imwrite(('./imagem.jpg'), img.get_matriz())