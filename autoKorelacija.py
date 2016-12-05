# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:00:07 2016

@author: root
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img1.jpg', 0)
rows,cols = img.shape


M = np.float32([[1, 0, 5], [0, 1, 5]])

dst = cv2.warpAffine(img, M, (cols,rows))

#cor = signal.correlate2d(img, dst)

#print cor

image_product = np.fft.fft2(img) * np.fft.fft2(dst).conj()
#print image_product

cc_img = np.fft.fftshift(np.fft.ifft2(image_product))

#print cc_img

fig = plt.figure(figsize=(8, 2))
ax1 = plt.subplot(1, 3, 1)
ax2 = plt.subplot(1, 3, 2)
ax3 = plt.subplot(1, 3, 3)

ax1.imshow(img)
ax1.set_axis_off()
ax1.set_title('Original')

ax2.imshow(dst)
ax2.set_axis_off()
ax2.set_title('Moved')

ax3.imshow(cc_img.real)
ax3.set_axis_off()
ax3.set_title('Cross-Korelacija')

plt.show()

print cc_img.real


#cv2.imshow('img', dst)
#cv2.waitKey(0)