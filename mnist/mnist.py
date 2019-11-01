import numpy as np
import cv2
import os
import sys
from matplotlib import pyplot as plt
from pre_processing import pre_processing
try:
    target = sys.argv[1]
    target = './'+target if not target.startswith('./') else target
    target = target+'/' if not target.endswith('/') else target
except:
    print("Insira o nome do objeto desejado e tente novamente.")
    exit()
files = []


def fourier(img):
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * \
        np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
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
    list_files(target)
    for f_name,f_class in files:
        original = cv2.imread(target+f_name,0)
        shape = pre_processing(original)
        f = fourier(shape)
        # plt.subplot(121),plt.imshow(original,'gray')
        plt.subplot(121),plt.imshow(shape, cmap='gray')
        plt.subplot(122),plt.imshow(f, cmap='gray')
        plt.show()
        # input()
                # characteristic_extraction()
        
