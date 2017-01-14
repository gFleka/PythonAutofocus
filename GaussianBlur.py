# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:46:01 2016

@author: root
"""

import cv2

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()
    
def blurring(sizeOfKernel, howManyTimes, inputImg, sigMax):
    for x in range(howManyTimes):
        inputImg = cv2.GaussianBlur(inputImg, sizeOfKernel, sigMax)
    return inputImg

image = cv2.imread("img5.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


for x in range(1, 19, 2):
    blur = blurring((x, x), 1, gray, 0)

    name = "img1Blurred" + str(x) + ".jpg"
    print name
    
    cv2.imwrite(name, blur)
                
    cv2.imshow('Blurred', blur)
    cv2.imshow('Original', image)
    
    cv2.waitKey(0)
    

