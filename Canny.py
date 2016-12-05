# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 00:01:34 2016

@author: root
"""

import cv2
import numpy
from matplotlib import pyplot as plt

image = cv2.imread('img1.jpg', 0)
imageBlur = cv2.imread('img1Blur5_5_0.jpg', 0)

imageCanny = cv2.Canny(image, 100, 200)
imageBlurCanny = cv2.Canny(imageBlur, 100, 200)

normalCountCanny = [(imageCanny == 0).sum(), (imageCanny == 255).sum()]
blurCountCanny = [(imageBlurCanny == 0).sum(), (imageBlurCanny == 255).sum()]

#dNormalCountCanny = dict(((j, i), imageCanny[i][j]) for i in range(len(imageCanny))
#    for j in range(len(imageCanny[0])) if i<j)

#plt.hist(dNormalCountCanny.keys(), weight=dNormalCountCanny.values(), bins = range(50))
#plt.show()

plt.hist(normalCountCanny, bins = 20, label = 'Original')
plt.hist(blurCountCanny, bins = 20, label = 'Blurred')

plt.legend(loc = 'upper right')
plt.savefig('canny_hist.jpg')
plt.show()

plt.subplot(221), plt.imshow(image, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(imageCanny, cmap = 'gray')
plt.title('Canny Normalni'), plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(imageBlur, cmap = 'gray')
plt.title('Blurred'), plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(imageBlurCanny, cmap = 'gray')
plt.title('Canny Blurred'), plt.xticks([]), plt.yticks([])


plt.savefig('canny.jpg',)
plt.show()
