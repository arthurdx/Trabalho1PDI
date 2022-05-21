import cv2
import numpy as np
#bugfix no imshow para google colab
#from google.colab.patches import cv2_imshow

def split_color(img):
  b, g, r = cv2.split(img)
  blue_img = np.zeros(img.shape)
  blue_img[:,:,0] = b
  green_img = np.zeros(img.shape)
  green_img[:,:,1] = g
  red_img = np.zeros(img.shape)
  red_img[:,:,2] = r
  return blue_img, green_img, red_img

img = cv2.imread('imgs/messi.png')
b_img, g_img, r_img = split_color(img)
total_b = 0
total_g = 0
total_r = 0
for x in range(0, img.shape[0]):
  for y in range(0, img.shape[1]):
      total_b = total_b + b_img[x, y]
      total_g = total_g + g_img[x, y]
      total_r = total_r + r_img[x, y]
media_b = total_b/(img.shape[0]*img.shape[1])
media_g = total_g/(img.shape[0]*img.shape[1])
media_r = total_r/(img.shape[0]*img.shape[1])
colors = np.array([media_b[0], media_g[1], media_r[2]])
if np.argmax(colors) == 0:
  print('Esta imagem é mais azul / This image is bluer')
  predcolor = 'blue'
elif np.argmax(colors) == 1:
  print('Esta imagem é mais verde / This image is greener')
  predcolor = 'green'
else:
  print('Esta imagem é mais vermelha / This image is redder')
  predcolor = 'red'
cv2.imshow(predcolor, img)
cv2.waitKey(0)
cv2.destroyAllWindows()
