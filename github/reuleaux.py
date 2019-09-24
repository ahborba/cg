import matplotlib.pyplot as plt, math,numpy as np
cos = math.cos
sin = math.sin
pi = math.pi
floor = math.floor
n = 3
vet_x = []
vet_y = []
for t in range(0,100):
    x = 2 * cos(pi/2*n) * cos(0.5 * ( t + (pi/n)*(  2 * floor( (n * t)/(2*pi)) + 1  ))) - cos((pi/n)*( 2 * floor((n*t)/(2*pi)) + 1 ))
    y = 2 * cos(pi/2*n) * sin(0.5 * ( t + (pi/n)*(  2 * floor( (n * t)/(2*pi)) + 1  ))) - sin((pi/n)*( 2 * floor((n*t)/(2*pi)) + 1 ))
    vet_x.append(x)
    vet_x.append(t)
    vet_y.append(y)
    vet_y.append(t)
    plt.plot(vet_x,vet_y)
    plt.show()
    
plt.plot(vet_x,vet_y)
plt.show()