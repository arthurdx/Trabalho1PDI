import cv2
import numpy as np
#imshow bugfix google colab
#from google.colab.patches import cv2_imshow

#carregamos as duas imagens / loading two images
anya = cv2.imread("imgs/anya2.png")
hoyeon = cv2.imread("imgs/hoyeon.png")

#fazendo com que ambas imagens tenham
#as mesmas dimenções / making sure
#both imagem have equal dimensions
h, w, _ = anya.shape
hoyeon = cv2.resize(hoyeon, (w, h))

honya = cv2.addWeighted(anya, 0.5, hoyeon, 0.5, 0)

hHonya, wHonya, _ = honya.shape

honya = cv2.GaussianBlur(honya,(5,5),0)
honya = cv2.resize(honya, (int(wHonya * 0.40), int(hHonya * 0.40)))
cv2.imwrite("imgs/honya.png", honya)

#run on google colab / executar no google colab
#cv2_imshow(honya)

#run locally / executar localmente
cv2.imshow("Honya", honya)
cv2.waitKey(0)
cv2.destroyAllWindows()