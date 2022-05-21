import cv2
import numpy as np
#from google.colab.patches import cv2_imshow

img = cv2.imread('imgs/hoyeon.png')
canvas = np.zeros((300, 300, 3), dtype = 'uint8')
font = cv2.FONT_HERSHEY_PLAIN
org = (40,40)
# ScalingFont
fontScale = 2

color = (255, 255, 255)

thickness = 2 

img2 = cv2.putText(canvas, 'SIM', org, font, fontScale, color,
                  thickness, cv2.LINE_AA)
h, w, _ = img.shape
canvas = cv2.resize(canvas,(w, h))
final = cv2.addWeighted(img, 1, canvas, 0.5, 0)
#run locally / executar localmenteW
cv2.imshow("final", final)
cv2.waitKey()

#run on google colab / executar no google colab
#cv2_imshow(final)