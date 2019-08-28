import numpy as np
import cv2

def bresenham_line(x0, y0, x1, y1):
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
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy
    
linhas = [((206,2),(10,510)),((206,2),(510,510))]
rows = 512
cols = 512
white = [255,255,255]
img = np.zeros((rows, cols, 1), dtype = "uint8")

for linha in linhas:
    p0 = linha[0]
    p1 = linha[1]
    x0,y0,x1,y1 = p0[0],p0[1],p1[0],p1[1]
    pontos = bresenham_line(x0,y0,x1,y1)
    for ponto in pontos:
        x = ponto[0]
        y = ponto[1]
        print(img[x,y])
        img[x,y] = white
    