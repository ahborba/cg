import cv2
import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from k import NN
# from neural_network import neural_network

def hot_encode(n):
    encode = [0]*10
    encode[n]=1
    return encode

def list_files(target):
    files = []
    for p, _, f in os.walk(os.path.abspath(target)):
        i = 0
        for file_name in f:
            i += 1
            file_name = str(file_name)
            f = file_name.split('_')[1]
            file_class = int(f.split('.jpeg')[0].split('class=')[1])
            files.append((file_name, file_class))
    return files

# Converte as imagens p/ entrada de uma rede neural.
def load_data(target):
    files = list_files(target)
    x,y = [],[]
    for f_name,f_class in files:
        img = cv2.imread(target+f_name,0)
        xi = []
        for l in img:
            for c in l:
                xi.append(c)
        xi = np.array(xi)
        
        x.append(xi)
        y.append(f_class)
    x= np.array(x)
    y= np.array(y)
    return (x,y)

def main():
    x,y = load_data('./train/')
    k = NN(x,y,50)
    x = k.normalize(x)
    k.add_layer(50,tf.nn.relu)
    k.add_layer(50,tf.nn.relu)
    k.add_layer(10,tf.nn.softmax)
    x_val,y_val = load_data('./test/')
    h=k.train((x_val,y_val))
    loss, acc = k.evaluate(x_val,y_val)
    predictions = [ np.argmax(yi) for yi in np.array(k.predict(x_val))]
    m=k.confusion_matrix(y_val,predictions)
    m = m.dot(100)
    for l in m:
        print(*l,sep=',',end=',\n')
    print(*m,sep=',')
    print('loss: ',loss)
    print('acc: ',acc*100)
    plt.plot(h.history['acc'])
    plt.plot(h.history['val_acc'])
    plt.title('Rede Neural - Acurácia do modelo')
    plt.ylabel('Acurácia')
    plt.xlabel('Epoca')
    plt.legend(['Treinamento','Validação'], loc='upper left')
    plt.show()
if __name__ == "__main__":
    main()
