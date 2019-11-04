import numpy as np
import cv2
import os
import sys
from matplotlib import pyplot as plt
from pre_processing import pre_processing
sys.settrace 
try:
    target = sys.argv[1]
    target = './'+target if not target.startswith('./') else target
    target = target+'/' if not target.endswith('/') else target
except:
    print("Insira o nome do objeto desejado e tente novamente.")
    exit()
files = []
error = False
def binary(img):
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    # plt.imshow(thresh1,'gray')
    # plt.show()
    return thresh1
fant = None
cont = 0
def fourier(img):
    global fant,cont
    if cont == 0:
        fant = img
        cont+=1
        # print('first')
    try:
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
        # plt.subplot(121),plt.imshow(fant, cmap = 'gray')
        # plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
        # plt.show()
    except Exception as e:
        return img
        
    fant = magnitude_spectrum
    return magnitude_spectrum

def list_files(path):
    for p, _, f in os.walk(os.path.abspath(path)):
        i = 0
        for file_name in f:
            i += 1
            file_name = str(file_name)
            f = file_name.split('_')[1]
            file_class = int(f.split('.jpeg')[0].split('class=')[1])
            files.append((file_name, file_class))


if __name__ == "__main__":
    count = 0
    list_files(target)
    for f_name,f_class in files:
        count+=1
        original = cv2.imread(target+f_name,0)
        shape = pre_processing(original)
        f=shape
        if f.shape[1]==0:
            input('aoieo')
            print(f_name)
        
        f = fourier(shape)
        w,h = f.shape
        # plt.subplot(121),plt.imshow(shape, cmap = 'gray')
        # plt.subplot(122),plt.imshow(f, cmap = 'gray')
        # plt.show()
        
       
        for i in range(0,w):
            for j in range(0,h):
                print(f[i][j],end=',')
                
                
        print(f_class)
       
        # input()
        # plt.subplot(121),plt.imshow(original,'gray')
        # plt.subplot(121),plt.imshow(shape, cmap='gray')
        # plt.subplot(122),plt.imshow(f, cmap='gray')
        # plt.show()
        # input()
                # characteristic_extraction()
        
