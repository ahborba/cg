from pre_process import pre_processing
from keras.utils import plot_model
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from k import NN
import cv2
import os


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
    files = list_files('./pre_processing/'+target)
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
    pre_processing(['./train/','./val/'])
    x,y = load_data('./train/')
    k = NN(x,y,20)
    x = k.normalize(x)
    k.add_layer(50,tf.nn.relu)
    k.add_layer(50,tf.nn.relu)
    k.add_layer(10,tf.nn.softmax)
    h = k.train()
    x_val,y_val = load_data('./val/')
    predictions = [ np.argmax(yi) for yi in np.array(k.predict(x_val))]
    print(k.confusion_matrix(y_val,predictions))
    loss, acc = k.evaluate(x_val,y_val)
    print('loss: ',loss)
    print('acc: ',acc*100,'%')
    # Plot training & validation accuracy values
    plt.plot(h.history['acc'])
    # plt.plot(h2.history['acc'])
    plt.title('Model accuracy')
    plt.ylabel('Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()
if __name__ == "__main__":
    main()
