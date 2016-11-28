# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:20:55 2016

@author: root
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('img1.jpg', 0)

f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.subplot(121), plt.imshow(image, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitudni spektar'), plt.xticks([]), plt.yticks([])

plt.show()
