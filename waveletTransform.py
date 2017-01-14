# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 22:34:45 2016

@author: groot
"""

import numpy as np
import pywt
import cv2
import math
import matplotlib.pyplot as plt
from collections import Counter


def wavelet(img, mode = 'haar', level = 1):
    imArray = cv2.imread(img)
    
    imArray = cv2.cvtColor(imArray, cv2.COLOR_RGB2GRAY)
    
    cv2.imshow("Test", imArray)
    
    imArray = np.float32(imArray)
    imArray /= 255;
    
    coeffs = pywt.wavedec2(imArray, mode, level = level)
    
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0;
    
    imArray_H = pywt.waverec2(coeffs_H, mode);
    imArray_H *= 255;
    imArray_H = np.uint8(imArray_H)

    x,y = imArray_H.shape
    
    test = imArray_H.ravel()
    
    unique2, counts2 = zip(*Counter(test).items())
    
    elements = []
    for i in range(0, 255):
        elements.append(i)
    
    #convert to lists
    unique3 = list(unique2)
    counts3 = list(counts2)
    
    #print counts3
    #print unique3
    
    for element in elements:
        #Check if unique3 does not contain element
        if element not in unique3:
            #Insert element to unique
            unique3.insert(element, element)
            #Insert 0 to element position
            counts3.insert(element, 0)
    
    #print zip(*Counter(test).items())

    #print counts3
    #print unique3    
    
    sumLower = 0
    sumUpper = 0
    sumMiddle = 0
    suma = np.zeros(256)
    
    for i in range(len(counts3)):
        suma[i] = math.log10(counts3[i] + 1)
        if i <= 25:
            sumLower += suma[i]
        if i >= 240:
            sumUpper += suma[i]
        else:
            sumMiddle += suma[i]
        #print suma[i]
    
    sumTotal = sumLower + sumMiddle + sumUpper
    sumLowerString = "Bottom 10% = " + str(sumLower)
    #print sumLowerString    
    
    sumUpperString = "Upper 10% = " + str(sumUpper)
    #print sumUpperString
    
    sumMiddleString = "Middle 80% = " + str(sumMiddle)
    #print sumMiddleString
    
    #print "Total ", sumLower + sumMiddle + sumUpper
    sumTotalString = "Total = " + str(sumTotal)
    
    plt.bar(range(len(suma)), suma, 1)   
    plt.xlabel("Frequency")
    
    plt.text(40, 4, sumLowerString, fontsize = 15)
    plt.text(40, 3.8, sumMiddleString, fontsize = 15)
    plt.text(40, 3.6, sumUpperString, fontsize = 15)
    plt.text(40, 3.4, sumTotalString, fontsize = 15)

    plt.xlim(-50, 300)
    plt.savefig(img)
    plt.show()
    
    #print range(x)
    """
    dataZ = np.zeros(imArray_H.shape)  
    print dataZ
    
    for i in range(x):
        for j in range(y):       
            #print imArray_H[i][j]
            dataZ[i][j] = math.log10(np.absolute(imArray_H[i][j] + 1))
            
            #print dataZ[i][j]
            
    print np.min(drek)
    print np.max(drek)
    
        
    
    plt.hist(dataZ.ravel(), 256, [-0.1, 2.5])
    plt.show()
    """
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
wavelet("img1Blurred17.jpg", 'db1', 2)