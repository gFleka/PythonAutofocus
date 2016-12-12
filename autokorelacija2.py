# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 23:00:07 2016

@author: root
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

auto_dataset = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg", "6.jpg", "7.jpg", "8.jpg", "9.jpg"]


for img_name in auto_dataset:
    img = cv2.imread(img_name, 0)
    rows,cols = img.shape
    
    
    M = np.float32([[1, 0, 30], [0, 1, 30]])
    
    dst = cv2.warpAffine(img, M, (cols,rows))
    
    correlation_index_mat = np.corrcoef(img,dst)[1,0]
    ci=np.average(correlation_index_mat)
    print "Korelacijski Index: " + str(ci)
