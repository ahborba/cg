import matplotlib.pyplot as plt


def DrawEllipse(xC, yC, a, b):
    # regiao 1
    x, y, P, delta_p, delta_pe, delta_ps, delta_pse, delta_2pe, delta_2ps, delta_2pse = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    x = 0
    y = b
    P = (b**2)+(((a**2)*(1-4*b)-2)/4)
    delta_pe = 3*(b**2)
    delta_2pe = 2*(b**2)
    delta_pse = delta_pe - (2*(a**2))*(b-1)
    delta_2pse = delta_2pe + 2*(a**2)
    while delta_pse < (2*(a**2) + 3*(b**2)):
        if P < 0:
            P += delta_pe
            delta_pe += delta_2pe
            delta_pse += delta_2pe
        else:
            P += delta_pse
            delta_pe += delta_2pe
            delta_pse += delta_2pse
            y -= 1
        x += 1
        print(x,y)
        plt.scatter(x, y)
    # regiao 2
    P = P - ((a**2)*((4*y)-3)+(b**2)*((4*x)+3)+2)/4
    delta_ps = (a**2)*(3-(2*y))
    delta_pse = 2*(b**2)+3*(a**2)
    delta_2ps = 2 * (a**2)
    while y > 0:
        if P > 0:
            P += delta_pe
            delta_pe += delta_2ps
            delta_pse += delta_2ps
        else:
            P += delta_pse
            delta_pe += delta_2ps
            delta_pse += delta_2pse
            x += 1
        y -= 1
        print(x,y)
        plt.scatter(x, y)


if __name__ == "__main__":
    plt.ylabel('some numbers')
    DrawEllipse(100, 100, 50, 20)
    DrawEllipse(100, 100, -50, -20)
    plt.scatter(-500,-500)
    plt.show()
