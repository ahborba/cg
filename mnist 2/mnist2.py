import cv2
import os,sys
import numpy as np
try:
    target = sys.argv[1]
    target = './'+target if not target.startswith('./') else target
    target = target+'/' if not target.endswith('/') else target
except:
    print("Insira o nome do objeto desejado e tente novamente.")
    exit()


files = []


def hot_encode(n):
    encode = [0]*10
    encode[n]=1
    return encode

def list_files():
    for p, _, f in os.walk(os.path.abspath(target)):
        i = 0
        for file_name in f:
            i += 1
            file_name = str(file_name)
            f = file_name.split('_')[1]
            file_class = int(f.split('.jpeg')[0].split('class=')[1])
            files.append((file_name, file_class))
# Converte as imagens p/ entrada de uma rede neural.
def read_data():
    x,y =[],[]
    for f_name,f_class in files:
        xi,yi = [],[]
        img = cv2.imread(target+f_name,0)
        w,h = img.shape
        for line in img:
            xi.append(line[:])
        x.append(xi)
        yi = hot_encode(f_class)
        y.append(yi)
    return (x,y)

def main():
    list_files()
    x,y = read_data()

if __name__ == "__main__":
    main()
