import cv2
import numpy as np
from matplotlib import pyplot as plt
#imshow bugfix google colab
#from google.colab.patches import cv2_imshow

img = cv2.imread("imgs/hoyeon.png", 0)
imgc = cv2.imread("imgs/anya.png")

plt.subplot(2, 2, 1), plt.imshow(img, cmap="gray"), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.hist(img.ravel(), 256, [0, 256]), plt.title("PRETO E BRANCO"), plt.xlim([0, 256]), plt.xticks([]), plt.yticks([])


#histograma da imagem preta e branca // b&y histogram
plt.hist(img.ravel(), 256, [0, 256])
#histograma das imagens coloridas // colored image histogram
color = ('b','g','r')

plt.subplot(2, 2, 2), plt.imshow(imgc), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.title("COLORIDA"), plt.xticks([]), plt.yticks([])

for x, col in enumerate(color):
  histc = cv2.calcHist([imgc], [x], None, [256], [0,256])
  plt.plot(histc, color = col)
  plt.xlim([0, 256])

#run locally // executar localmente
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


#run on google colab // executar no google colab
#plt.show()