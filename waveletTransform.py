# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:34:45 2016

@author: root
"""

import numpy as np
import pywt
import cv2


def wavelet(img, mode = 'haar', level = 1):
    imArray = cv2.imread(img)
    
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
    
    imArray = np.float32(imArray)
    imArray /= 255;
    
    coeffs = pywt.wavedec2(imArray, mode, level = level)
    
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;
    
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)
    
    print imArray_H
    
    cv2.imshow('image', imArray_H)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
wavelet("img1.jpg", 'db1', 3)