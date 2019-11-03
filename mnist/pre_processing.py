import numpy as np
import cv2
import os,sys
from tabulate import tabulate
from matplotlib import pyplot as plt
from scipy import stats

shape_up = 28
shape_down =0
shape_left =28
shape_right=0

def binary(img):
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    # plt.imshow(thresh1,'gray')
    # plt.show()
    return thresh1

def fourier(img):
    dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

    plt.imshow(img, cmap = 'gray')
    # plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.show()
    
    return magnitude_spectrum


def get_shape(img):
    global shape_up,shape_down,shape_left,shape_right
    up,right,left,down = 28,0,28,0
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if img[i][j] == 0:
                if j > right:
                    if j > shape_right:
                        shape_right= j
                    right=j
                elif j < left:
                    if j < shape_left:
                        shape_left= j
                    left = j
                if i < up:
                    if i < shape_up:
                        shape_up= i
                    up = i
                elif i > down:
                    if i > shape_down:
                        shape_down= i
                    down = i
    if (left + 24) > 27:
        left = 27-24
    if (up+24)>27:
        up = 27-24

    return img[up:up+23,left:left+23]



    # down = up +24
    # right = left + 24


    # if down > 27:
    #     down = 27
    #     up = down-24
    # if right > 27:
    #     left = 3
    #     right=27
    # return img[up:down,left:right]
    

def pre_processing(img):
    binary_img = binary(img)
    return get_shape(binary_img)
        
        

def statistics(img):
    hist = cv2.calcHist([img],[0],None,[784],[0,784])
    std  = np.float32(np.std(hist))
    kurt = np.float32(stats.kurtosis(hist)[0])
    return(std,kurt)


def divide_matrix(mat):
    w,h = mat.shape
    center_w,center_h = int(w/2),int(h/2)
    m11 = mat[0:center_w,0:center_h]
    m12 = mat[center_w:w,0:center_h]
    m21 = mat[0:center_w,center_h:h]
    m22 = mat[center_w:w,center_h:h]
    return [m11,m12,m21,m22]