from pg import *

def get_vertex_list(objeto):
    v_list =[]
    with  open('./dados/vertex-{}.csv'.format(objeto)) as vertex_file:
        for linha in vertex_file:
            linha = linha.strip('\n')
            l = linha.split(',')
            v_list.append(list(map(float, l)))
            
    return v_list
        

def get_index_list(objeto):
    i_list =[]
    with  open('./dados/index-{}.csv'.format(objeto)) as vertex_file:
        for linha in vertex_file:
            linha = linha.strip('\n')
            l = linha.split(',')
            face = []
            for i in l:
                face.append(int(i))
            i_list.append(face)
    return i_list




def main():
    l = light()
    for obj in ['1','2']:
        vertex_list = get_vertex_list(obj)
        index_list = get_index_list(obj)
        print(obj)
        print(vertex_list)
        print(index_list)
        l.add_object(vertex_list,index_list)
    l.main_loop()
        

if __name__ == "__main__":
    main()
