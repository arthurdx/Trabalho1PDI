#QUESTÃO 1

import cv2
import numpy as np
from matplotlib import pyplot as plt
#bugfix imshow google colab
#from google.colab.patches import cv2_imshow

def crop(img, xImg, yImg, wImg, hImg):
      croppedImg = img[yImg:yImg + hImg, xImg:xImg + wImg]
      return croppedImg

def paste(src, dst, x, y):
  dst[y:y + src.shape[0], x:x + src.shape[1]] = src
  return dst

img = cv2.imread('imgs/messi.png')
#cv2_imshow(img)
croppedImg = crop(img, 336, 287, 55, 170)
#cv2_imshow(croppedImg)
newImg = paste(croppedImg, img, 20,40)
#run on google colab / executar no google colab
#cv2_imshow(newImg)

#run locally / executar localmente
cv2.imshow('Result', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()