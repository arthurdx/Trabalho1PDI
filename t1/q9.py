import cv2
import numpy as np
import time

#only locally/só pode ser executado localmente

def onChange(value):
    pass


ESCAPE_KEY_ASCII = 27
img = cv2.imread("imgs/th.png", 0)
copyimg = img.copy()
windowTitle = 'Threshold'
cv2.namedWindow(windowTitle)
prevThreshold = 0
updateThreshold = False
timeCounter = 0

# criar trackbar
cv2.createTrackbar("Threshold", windowTitle, 0, 255, onChange)


while True:
    newThreshold = cv2.getTrackbarPos("Threshold", windowTitle)
    # valor de contraste alterado
    if newThreshold != prevThreshold:
        updateThreshold = True
        timeCounter = time.time()
        prevThreshold = newThreshold

    if updateThreshold == True and time.time() - timeCounter > 1:

        limiar, copyimg = cv2.threshold(
            img, newThreshold, 255, cv2.THRESH_BINARY)

        updateThreshold = False

    cv2.imshow(windowTitle, copyimg)

    keyPressed = cv2.waitKey(1) & 0xFF
    if keyPressed == ESCAPE_KEY_ASCII:
        break

cv2.destroyAllWindows()