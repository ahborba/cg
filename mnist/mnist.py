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


def fourier(name):
    img = cv2.imread(name, 0)

    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)

    magnitude_spectrum = 20 * \
        np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()


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
    pre_processing(files, target)
