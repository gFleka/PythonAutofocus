import cv2
import numpy as np
import time


for i in range(1,11):

	img = cv2.imread('C:/Users/Nino/Documents/GitHub/PythonAutofocus/'+str(i)+'.jpg',0)

	"""Dio za histogram i detekciju promjene"""
	hist,bins = np.histogram(img.ravel(),256,[0,256])
	print "Slika redni broj:"+str(i)
	print np.var(hist)


