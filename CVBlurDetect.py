import cv2
import numpy as np
import time

varijanca=np.empty(10)
for i in range(0,10):

	img = cv2.imread('C:/Users/Nino/Documents/GitHub/PythonAutofocus/'+str(i+1)+'.jpg',0)

	"""Dio za histogram i detekciju promjene"""
	hist,bins = np.histogram(img.ravel(),256,[0,256])
	print "Slika redni broj:"+str(i)
	varijanca[i] = np.var(hist)
	print varijanca[i]
imgMin=np.where(np.min(varijanca))
print imgMin[0][0]
img = cv2.imread('C:/Users/Nino/Documents/GitHub/PythonAutofocus/'+str(imgMin[0][0]+1)+'.jpg',0)
cv2.imshow('Best Focus',img)
input("Press Enter to continue...")



