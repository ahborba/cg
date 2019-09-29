pontos = []
condicao = True
while condicao:
    x = float(input('x'))
    if x ==0:
        condicao=False
    y = float(input('y'))
    pontos.append([x,y,0])
print(pontos)