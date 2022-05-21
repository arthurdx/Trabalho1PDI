import cv2
import numpy as np 
from matplotlib import pyplot as plt

def aplicar(image, filter):
    copy = image.copy()
    aux   = image.copy()

    if(filter == "Mean"):
        copy = cv2.blur(image, (5, 5))
    elif(filter == "Gaussian"):
        copy = cv2.GaussianBlur(image, (5, 5), 0)
    elif(filter == "Median"):
        copy = cv2.medianBlur(image, 5)
    elif(filter == "Sobel"):
        copy = cv2.cvtColor(copy, cv2.COLOR_RGB2GRAY)
        copyH = cv2.Sobel(copy, 5, 1, 0)
        copyV = cv2.Sobel(copy, 5, 0, 1)
        copy = copyH + copyV
    elif(filter == "Laplacian"):
        aux = cv2.cvtColor(aux, cv2.COLOR_RGB2GRAY)
        copy = cv2.cvtColor(copy, cv2.COLOR_RGB2GRAY)
        copy = cv2.Laplacian(copy, cv2.CV_64F, 5)
        copy = copy + aux
        copy = cv2.convertScaleAbs(copy)
    
    return copy

filters = ["Mean", "Gaussian", "Median", "Sobel", "Laplacian"]

natureza = cv2.imread('imgs/messi.png')
natureza = cv2.cvtColor(natureza, cv2.COLOR_BGR2RGB)

altura, largura, _ = natureza.shape
resultado = np.zeros([largura, altura])

plt.imshow(natureza), plt.title("ORIGINAL"), plt.xticks([]), plt.yticks([])

for x in range(1, 6):
    resultado = aplicar(natureza, filters[x-1])

    if(filters[x-1] == "Laplacian" or filters[x-1] == "Sobel"):
        plt.figure(), plt.imshow(resultado, cmap='gray'), plt.title(filters[x-1]), plt.xticks([]), plt.yticks([])
    else:
        plt.figure(), plt.imshow(resultado), plt.title(filters[x-1]), plt.xticks([]), plt.yticks([])

plt.show()