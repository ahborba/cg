import numpy as np
from glumpy import app, gl, glm, gloo

window = app.Window(width=1024, height=1024,color=(0.30, 0.30, 0.35, 1.00))
vertex = """uniform mat4   u_view;          // View matrix
            uniform mat4   u_projection;    // Projection matrix
            attribute vec3 a_position;      // Vertex position
            void main(){
                gl_Position = u_projection * u_view *  vec4(a_position,1.0);
           }"""
fragment = """void main(){
                gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);
            }"""

index_list = None
obj = None
vertex_list = None

def multiplica(mat,pts):
    mat = np.array(mat)
    l = []
    for p in pts:
        if type(p)!=list:
            p = p[0]
        x,y,z = p
        p = list((np.array([x,y,z,1])@mat)[0:3])
        l.append(p)
    return l



def criar_obj(v_list,i_list):
    global vertex_list,index_list,obj
    vertex_list = np.zeros(len(v_list),[("a_position", np.float32, 3)])
    vertex_list['a_position'] = v_list
    vertex_list= vertex_list.view(gloo.VertexBuffer)
    index_list = np.array(i_list,dtype=np.uint32)
    index_list=index_list.view(gloo.IndexBuffer)
    obj= gloo.Program(vertex, fragment)
    obj.bind(vertex_list)
    obj['u_view'] = glm.translation(0, 0, -5)
    


@window.event
def on_key_press(symbol, modifiers):
    global vertex_list,index_list,obj
    shift = True if modifiers == 1 else False
    letra = ''
    if symbol==65307:
        print('fechou')
        try:
            window.close()
        except:
            print('janela fechada')
        finally:
            return
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
    vertex_list=multiplica(mat,vertex_list)
    obj['a_position'] = vertex_list
    # window.clear()
    obj.draw(gl.GL_TRIANGLES,index_list)

@window.event
def on_draw(dt):
    window.clear()
    obj.draw(gl.GL_TRIANGLES,index_list)
    
@window.event
def on_resize(width, height):
    global obj
    obj['u_projection'] = glm.perspective(45.0, width / float(height), 2.0, 100.0)
@window.event
def on_init():
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glPolygonMode(gl.GL_FRONT_AND_BACK, gl.GL_LINE)

def run():
    app.run()