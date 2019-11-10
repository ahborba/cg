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

def binary(img):
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    return thresh1


def crop_image(img):
    global shape_up,shape_down,shape_left,shape_right
    up,right,left,down = 28,0,28,0
    for i in range(0,img.shape[0]):
        for j in range(0,img.shape[1]):
            if img[i][j] == 0 :
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


def pre_processing(folders):
    for f in folders:
        files = list_files(f)
        for f_name, f_class in files:
            img = cv2.imread(f+f_name,0)
            img = binary(img)
            img = crop_image(img)
            cv2.imwrite('./pre_processing/'+f+f_name,img)
