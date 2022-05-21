import cv2
from matplotlib import pyplot as plt
#imshow bugfix google colab
#from google.colab.patches import cv2_imshow

src = cv2.imread('imgs/imgex6.png')

src = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

dst = cv2.equalizeHist(src)
plt.subplot(2, 2, 1), plt.imshow(src), plt.title('original')#, plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(dst), plt.title("equalizado")#, plt.xlim([0, 256]), plt.xticks([]), plt.yticks([])
plt.show()
#run on google colab
#cv2_imshow(src)
#cv2_imshow(dst)