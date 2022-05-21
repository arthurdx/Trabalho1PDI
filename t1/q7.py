import cv2
import numpy as np
from matplotlib import pyplot as plt 




def compareImage(s1):
  s1 = s1.copy()
  h, w, _ = s1.shape
  s2 = cv2.imread('imgs/honya6040.png')
  d1 = cv2.imread('imgs/messi.png')
  d2 = cv2.imread('imgs/imgex6.png')
  d3 = cv2.imread('imgs/suspeito.png')
  s2 = cv2.resize(s2, (w, h))
  d1 = cv2.resize(d1, (w, h))
  d2 = cv2.resize(d2, (w, h))
  d3 = cv2.resize(d3, (w, h))

  
  hsvS1 =  cv2.cvtColor(s1, cv2.COLOR_BGR2HSV)
  hsvS2 =  cv2.cvtColor(s2, cv2.COLOR_BGR2HSV)
  hsvD1 =  cv2.cvtColor(d1, cv2.COLOR_BGR2HSV)
  hsvD2 =  cv2.cvtColor(d2, cv2.COLOR_BGR2HSV)
  hsvD3 =  cv2.cvtColor(d3, cv2.COLOR_BGR2HSV)

  hsvHalfDown = hsvS1[hsvS1.shape[0]//2:,:]
  h_bins = 50
  s_bins = 60
  histSize = [h_bins, s_bins]
  # hue varies from 0 to 179, saturation from 0 to 255
  h_ranges = [0, 180]
  s_ranges = [0, 256]
  ranges = h_ranges + s_ranges # concat lists
  # Use the 0-th and 1-st channels
  channels = [0, 1]
    
  histS1 = cv2.calcHist([hsvS1], channels, None, histSize, ranges, accumulate=False)
  cv2.normalize(histS1, histS1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

  histHalfDown = cv2.calcHist([hsvHalfDown], channels, None, histSize, ranges, accumulate=False)
  cv2.normalize(histHalfDown, histHalfDown, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

  histS2 = cv2.calcHist([hsvS2], channels, None, histSize, ranges, accumulate=False)
  cv2.normalize(histS2, histS2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

  histD2 = cv2.calcHist([hsvD2], channels, None, histSize, ranges, accumulate=False)
  cv2.normalize(histD2, histD2, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

  histD1 = cv2.calcHist([hsvD1], channels, None, histSize, ranges, accumulate=False)
  cv2.normalize(histD1, histD1, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

  histD3 = cv2.calcHist([hsvD3], channels, None, histSize, ranges, accumulate=False)
  cv2.normalize(histD3, histD3, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)


  distS2 = 0
  distD1 = 0
  distD2 = 0
  distD3 = 0
  for compare_method in range(4):
    s1S1 = cv2.compareHist(histS1, histS1, compare_method)
    s1Half = cv2.compareHist(histS1, histHalfDown, compare_method)
    s1S2 = cv2.compareHist(histS1, histS2, compare_method)
    s1D1 = cv2.compareHist(histS1, histD1, compare_method)
    s1D2 = cv2.compareHist(histS1, histD2, compare_method)
    s1D3 = cv2.compareHist(histS1, histD3, compare_method)
    plt.figure()
    plt.suptitle(compare_method)
    plt.subplot(2, 5, 1), plt.imshow(s1, cmap='gray'), plt.title("%.5f" % (s1S1)), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 2), plt.imshow(s2, cmap='gray'), plt.title("%.5f" % (s1S2)), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 3), plt.imshow(d1, cmap='gray'), plt.title("%.5f" % (s1D1)), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 4), plt.imshow(d2, cmap='gray'), plt.title("%.5f" % (s1D2)), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 5, 5), plt.imshow(d3, cmap='gray'), plt.title("%.5f" % (s1D3)), plt.xticks([]), plt.yticks([])

    distS2 += np.square(s1S2)
    distD1 += np.square(s1D1)
    distD2 += np.square(s1D2)
    distD3 += np.square(s1D3)

  distS2 = np.sqrt(distS2)
  distS2 = np.sqrt(distD1)
  distS2 = np.sqrt(distD2)
  distS2 = np.sqrt(distD3)
  dists = []
  dists.append(distS2)
  dists.append(distD1)
  dists.append(distD2)
  dists.append(distD3)

  return dists.index(min(dists))



s1 = cv2.imread('imgs/honya5050.png')

menor = compareImage(s1)
if menor == 0:
  print('s2 é a imagem mais proxima')
elif menor == 1:
  print('d1 é a imagem mais proxima')
elif menor == 2:
  print('d2 é a imagem mais proxima')
else:
  print('d3 é a imagem mais proxima')
plt.show()