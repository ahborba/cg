import numpy as np
import cv2
import os,sys
from tabulate import tabulate
from matplotlib import pyplot as plt
from scipy import stats
try:
    objeto = sys.argv[1]
except:
    print("Insira o nome do objeto desejado e tente novamente.")
    exit()

def binary(img):
    # gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    # img = cv2.imread('gradient.png',0)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    plt.imshow(thresh1,'gray')
    # plt.show()
    return thresh1

def fourier(img):
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    return magnitude_spectrum
    # plt.show()


def pre_processing(files,target):
    classes = [[]] * 10
    for f_name,f_class in files:
        original = cv2.imread(target+f_name,0)
        img_bin  = binary(original)
        f_img = fourier(img_bin)
        images = [(original,'original'),(img_bin,'binary  '),(f_img,'fourier  ')]
        data_list = []
        for img,name in images:
            data = None
            hist = cv2.calcHist([img],[0],None,[256],[0,256])
            
            mean = np.float32(np.mean(hist))
            std  = np.float32(np.std(hist))
            mode = np.float32(np.argmax(hist))
            skew = np.float32(stats.skew(hist)[0])
            kurt = np.float32(stats.kurtosis(hist)[0])
            
            data = ([name,mean,std,mode,skew,kurt])
            data_list.append(data)
            # print('class: '+str(f_class),mean,std,mode,skew,kurt,sep='\t')
        classes[f_class].append(data_list)
    i = 0
    for cl in classes:
        print('\n\n\nDataset: ',i)
        # print('\t\tmean\t\tstd\t\tmode\t\tskew\t\tkurt')
        mean = []
        std = []
        mode = []
        skew = []
        kurt = []
        for class_values in classes:
            
            for op in class_values:
                table = []
                for v in op:
                    table.append(v)

                print('\t',tabulate(table,headers=['operation','mean','std','mode','skew','kurt']))
                
        


        i+=1   



    