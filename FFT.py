# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:20:55 2016

@author: root
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('img4.jpgDetected.jpg', 0)
imageBlur = cv2.imread('img4.jpgDetectedBlur.jpg', 0)

f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)

fBlur = np.fft.fft2(imageBlur)
fshiftBlur = np.fft.fftshift(fBlur)

magnitude_spectrum = 20 * np.log(np.abs(fshift))
#print magnitude_spectrum

magnitude_spectrumBlur = 20 * np.log(np.abs(fshiftBlur))
#print magnitude_spectrumBlur




plt.subplot(221), plt.imshow(image, cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(222), plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitudni spektar'), plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(imageBlur, cmap = 'gray')
plt.title('Blurred'), plt.xticks([]), plt.yticks([])

plt.subplot(224), plt.imshow(magnitude_spectrumBlur, cmap = 'gray')
plt.title('Magnitudni spektar Blurred'), plt.xticks([]), plt.yticks([])

plt.savefig('magnitudni_spektar4.jpg',)
plt.show()
