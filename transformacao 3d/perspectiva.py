import numpy as np
from glumpy import app, gl, glm, gloo

d = 2
def perspectiva(lista):
    l = []
    for v in lista:
        X,Y,Z=v[0],v[1],v[2]
        x= (X * d) / (Z + d)
        y = (Y * d) / (Z + d)
        l.append([x,y])
    return l

def multiplica(mat,pts):
    mat = np.array(mat)
    l = []
    for p in pts:
        x,y,z = p
        p = list((np.array([x,y,z,1])@mat)[0:3])
        l.append(p)
    return l


vertex = """
attribute vec2 position;
attribute vec4 color;
varying vec4 v_color;
void main()
{
    gl_Position = vec4(position, 0.0, 1.0);
    v_color = color;
}
"""
fragment = """
varying vec4 v_color;
void main()
{
    gl_FragColor = v_color;
}
"""

window = app.Window(width=512, height=512, color=(255, 255, 255, 1))
app.use('glfw')

@window.event
def on_init():
    gl.glEnable(gl.GL_DEPTH_TEST)
@window.event
def on_draw(dt):    
    window.clear()
    cube.draw(gl.GL_LINE_LOOP,triangulos)

@window.event
def on_key_press(symbol, modifiers):
    global pontos,cube
    shift = True if modifiers == 1 else False
    letra = ''
    if symbol!=-1:
        letra = chr(symbol)
    mat = np.eye(4, dtype=np.float32)
    if letra =='W':
        glm.translate(mat, 0, 0.1, 0)
    elif letra == 'S':
        glm.translate(mat, 0, -0.1, 0)
    elif letra=='D':
        glm.translate(mat, 0.1,0, 0)
    elif letra =='A':
        glm.translate(mat, -0.1, 0, 0)
    elif letra =='N':
        glm.translate(mat,0,0,0.1)
    elif letra =='M':
        glm.translate(mat,0,0,-0.1)
    elif letra =='-':
        glm.scale(mat, 0.9, 0.9, 0.9)
    elif letra == '=':
        glm.scale(mat, 1.1, 1.1, 1.1)
    elif letra =='Z':
        alpha = -0.8 if shift else 0.8
        glm.rotate(mat, alpha, 0, 0, 1)
    elif letra =='X':
        alpha = -0.8 if shift else 0.8
        glm.rotate(mat, alpha, 0, 1, 0)
    elif letra =='Y':
        alpha = -0.8 if shift else 0.8
        glm.rotate(mat, alpha, 1, 0, 0)
    pontos=multiplica(mat,pontos)
    pts_perspectiva = perspectiva(pontos)
    cube['position'] = pts_perspectiva
    # window.clear()
    cube.draw(gl.GL_LINE_LOOP,triangulos)

v1 = [-0.5,0.5,-0.5]
v2 = [0.5,0.5,-0.5]
v3 = [-0.5,-0.5,-0.5]
v4 = [0.5,-0.5,-0.5]
v5 = [-0.5,0.5,0.5]
v6 = [0.5,0.5,0.5]
v7 = [-0.5,-0.5,0.5]
v8 = [0.5,-0.5,0.5]
pontos = np.array([v1,v2,v3,v4,v5,v6,v7,v8])
# , 3,7,5, 5,1,3
triangulos = np.array([0,1,3, 3,2,0, 0,4,5, 5,1,0, 0,4,6, 6,2,0, 0,2,2, 2,6,7, 7,3,2, 0,0,2, 2,2,3, 3,7,5, 5,1,3, 3,2,2, 2,2,0], dtype=np.uint32)
triangulos = triangulos.view(gloo.IndexBuffer)
pontos = pontos.view(gloo.VertexBuffer)
cube = gloo.Program(vertex, fragment)
       
pts_perspectiva = perspectiva(pontos)# gl.glEnable(gl.GL_LINE_SMOOTH)
cube['position'] = pts_perspectiva
cube['color'] = [[1, 0, 1, 1],[0, 1, 0, 1],[0,0,0,1],[0, 1, 0, 1],[0, 0, 1, 1],[0,0,0,1],[0, 0, 1, 1],[0,0,0,1],[1, 0,0, 1],[0,0,0,1],[1, 0, 0, 1],[0,0,0,1],[0,1, 1, 1],[0,0,0,1]]
print('as teclas \'w, a, s, d\' transladam o cubo')
print('as teclas \'x, y, z\' rotacionam o cubo. Utilizando alguma destas teclas com shift pressionado, o cubo rotaciona no sentido oposto')
print('as teclas \'- + \' realizam a escala do cubo.')
app.run(framerate=60)
