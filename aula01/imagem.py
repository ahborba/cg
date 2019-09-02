import numpy as np
class Imagem:

    def __init__(self,lin,col):
        self.lin = lin
        self.col = col
        self.mat = np.zeros((lin,col,3),np.uint8)
        self.linha_horizontal = []
        self.branco = np.array([255,255,255],np.uint8)
        
    def bresenham_line(self,x0, y0, x1, y1):
        pontos = []
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2*dy - dx
        y = 0

        for x in range(dx + 1):
            pontos.append((x0 + x*xx + y*yx, y0 + x*xy + y*yy,1))
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy

        return pontos

    def desenhar(self,linhas):
        self.mat = np.zeros((self.lin,self.col,3),np.uint8)
        for linha in linhas:
            p0 = linha[0]
            p1 = linha[1]
            x0,y0,x1,y1 = p0[0],p0[1],p1[0],p1[1]
            pontos = self.bresenham_line(x0,y0,x1,y1)
            for ponto in pontos:
                x = ponto[0]
                y = ponto[1]
                if x >=self.lin or y >= self.col or x <0 or y < 0:
                    continue
                self.mat[y,x] = self.branco
    
    def criar_letra(self,linhas):
        for linha in linhas:
            p0 = linha[0]
            p1 = linha[1]
            x0,y0,x1,y1 = p0[0],p0[1],p1[0],p1[1]
            pontos = self.bresenham_line(x0,y0,x1,y1)
            self.linha_horizontal.append(pontos[int(len(pontos)*0.55)])

            for ponto in pontos:
                x = ponto[0]
                y = ponto[1]
                self.mat[y,x] = self.branco

        p0 = self.linha_horizontal[0]
        p1 = self.linha_horizontal[1]
        x0 = p0[0]
        x1 = p1[0]
        y = p0[1]
        linhas.append((p0,p1))
        for x in range(x0,x1):
            self.mat[y,x] = self.branco
        return linhas
    def get_matriz(self):
        return self.mat