import matplotlib.pyplot as plt,numpy as np, math
def func(x,y,a,b):
    d2r = math.pi/180.0
    vet_x = []
    vet_y = []
    for i in range(0,360):
        rad = i*d2r
        vet_x.append(math.cos(rad)*a + x)
        vet_y.append(math.sin(rad)*b + y)
    plt.plot(vet_x,vet_y)