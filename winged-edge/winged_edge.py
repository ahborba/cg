import sys
from sintetizar_poligono import criar_obj
try:
    objeto = sys.argv[1]
except:
    print("Insira o nome do objeto desejado e tente novamente.")
    exit()

vertex_dict = {}
face_dict = {}
edge_dict = {}

vertex_file = open('./malhas/{}/vertex.csv'.format(objeto))
face_file = open('./malhas/{}/face.csv'.format(objeto))
edge_file = open('./malhas/{}/edge.csv'.format(objeto))


def read_vertex():
    cont = 0
    for linha in vertex_file:
        linha = linha.strip('\n')
        el = linha.split(',')
        posicao = list(map(int, el[0:3]))
        del(el[0:3])
        vertex_dict['v'+str(cont)] = [posicao, el]
        cont += 1
    print(vertex_dict)
    vertex_file.close()


def read_edge():
    cont = 0
    for linha in edge_file:
        linha = linha.strip('\n')
        el = linha.split(',')
        vertex = el[0:2]
        faces = el[2:4]
        del(el[0:4])
        edge_dict['e'+str(cont)] = [vertex, faces, el]
        cont += 1
    print(edge_dict)
    edge_file.close()


def read_face():
    cont = 0
    for linha in face_file:
        linha = linha.strip('\n')
        face = linha.split(',')
        face_dict['f'+str(cont)] = face
        cont += 1
    print(face_dict)
    face_file.close()


def get_index_list():
    index_list = []
    for edge_a, edge_b, edge_c in list(face_dict.values()):
        vertex_list = []
        for vertex in [edge_dict[edge_a][0], edge_dict[edge_b][0], edge_dict[edge_c][0]]:
            for v in vertex:
                if not (int(v.strip('v')) in vertex_list):
                    vertex_list.append(int(v.strip('v')))
        index_list.append(vertex_list)
    return index_list


def vertice():
    op = input(
        '1)Vertices conectados\n2)Faces dependentes\n3)3 vertices, descobrir face\n>>> ')
    if op == '1':
        vertex = input('Vertice\n>>> ')
        vertex_list = []
        for edge in vertex_dict[vertex][1]:
            v_list = edge_dict[edge][0]
            for v in v_list:
                if not(v in vertex_list):
                    vertex_list.append(v)
        vertex_list.remove(vertex)
        print(vertex_list)
    elif op == '2':
        face_list = []
        vertex = input('Vertice\n>>> ')
        for edge in vertex_dict[vertex][1]:
            for f in edge_dict[edge][1]:
                if not(f in face_list):
                    face_list.append(f)
        print(face_list)
    else:
        vertex_list = []
        vertex_list.append(input('1º vertice\n>>> '))
        vertex_list.append(input('2º vertice\n>>> '))
        vertex_list.append(input('3º vertice\n>>> '))
        fl = []
        for vertex in vertex_list:
            face_list = []
            for edge in vertex_dict[vertex][1]:
                face_list.extend(edge_dict[edge][1])
            fl.append(face_list)
        f_set = list(set(fl[0]) & set(fl[1]) & set(fl[2]))
        if len(f_set)==1:
            print(f_set[0])
        else:
            print('não existe face')



def face():
    op = input('1)vertices pertencentes\n2)Arestas pertencentes\n>>> ')
    face = input('Face\n>>> ')
    vertex_list = []
    if op == '1':
        for edge in face_dict[face]:
            for vertex in edge_dict[edge][0]:
                if not (vertex in vertex_list):
                    vertex_list.append(vertex)
        print(vertex_list)
    else:
        print(face_dict[face])


def aresta():
    print('vertices pertencentes a uma aresta')
    edge = input('Aresta\n>>> ')
    print(edge_dict[edge][0])


def main():
    read_vertex()
    read_edge()
    read_face()

    try:
        while True:
            txt = input('1)Display\n2)Consulta\n>>> ')
            if txt == '1':
                print('Display')
                vertex_list = [x[0] for x in list(vertex_dict.values())]
                index_list = get_index_list()
                criar_obj(vertex_list, index_list)
            elif txt == '2':
                print('Consulta')
                txt = input('1)vertice\n2)face\n3)aresta\n>>> ')
                if txt == '1':
                    vertice()
                elif txt == '2':
                    face()
                else:
                    aresta()
            if txt == 'sair':
                break
    except:
        pass
    print(index_list)
    print(vertex_list)


if __name__ == "__main__":
    main()
