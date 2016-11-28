# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:46:01 2016

@author: root
"""

import cv2

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()
    


image = cv2.imread("img1.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



blur = cv2.GaussianBlur(image, (5, 5), 0)


fmOriginal = variance_of_laplacian(gray)
fmBlur = variance_of_laplacian(blur)

text = "Img"

cv2.putText(image, "{}: {:.2f}".format(text, fmOriginal), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            
cv2.putText(blur, "{}: {:.2f}".format(text, fmBlur), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)            
#cv2.imwrite('img1Blur5_5_1.jpg', blur)
            
cv2.imshow('Blurred', blur)
cv2.imshow('Original', image)

cv2.waitKey(0)