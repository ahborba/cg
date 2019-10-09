import numpy as np
import cv2

pontos = []





def escrever_letra():
    print('Insira o tamanho da imagem: ')
    row = int(input('linhas: '))
    col = int(input('colunas: '))

    img = np.zeros((row, col, 3), np.uint8)
    linhas = [((int(col/2),int(row*0.1),1),(int(col*0.1),int(row*0.9),1)),((int(col/2),int(row*0.1),1),(int(col*0.9),int(row*0.9),1))]
    white = np.array([255, 255, 255], dtype=np.uint8)
    linha_horizontal = []
    pontos_diag = []
    for linha in linhas:
        p0 = linha[0]
        p1 = linha[1]
        x0, y0, x1, y1 = p0[0], p0[1], p1[0], p1[1]
        pontos_diag = bresenham_line(x0, y0, x1, y1)

        for ponto in pontos:
            x = ponto[1]
            y = ponto[0]
            img[x, y] = white
        pontos.append(pontos_diag)
        pontos_diag.clear()
    x0 = (linha_horizontal[0])[0]
    y = (linha_horizontal[0])[1]
    x1 = (linha_horizontal[1])[0]
    linhas.append((x0,y,1))
    linhas.append((x1,y,1)) 
    for x in range(x0, x1):
        img[y, x] = white
        pontos.append((x,y))
    return img

def get_linhas():
    return linhas

