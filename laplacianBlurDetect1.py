# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/jura611/.spyder2/.temp.py
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

from imutils import paths

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()
    

#image = cv2.imread('img1.jpg')

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required=True,
                help="Dir of images")

args = vars(ap.parse_args())

for imagePath in paths.list_images(args["images"]):
#cv2.destroyAllWindows()

    image = cv2.imread(imagePath)
    
    #res = cv2.resize(image, (960, 540))
    
    #cv2.imshow('resized', res);
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(image, (5, 5), 0)

    fmOriginal = variance_of_laplacian(gray)
    fmBlur = variance_of_laplacian(blur)
    
    text = "Img"

    cv2.putText(image, "{}: {:.2f}".format(text, fmOriginal), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                
    cv2.putText(blur, "{}: {:.2f}".format(text, fmBlur), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)


    cv2.imshow('Original', image)
    cv2.imshow('Blurred', blur)

    cv2.imwrite(imagePath + 'Detected.jpg' , image)
    cv2.imwrite(imagePath + 'DetectedBlur.jpg', blur)
    cv2.waitKey(0)

