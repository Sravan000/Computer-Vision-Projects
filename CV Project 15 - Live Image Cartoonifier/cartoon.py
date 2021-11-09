# we'll try to apply different fikters to an image and finally convert it somewhere like a cartooinsh image
# importing necessary files
import cv2
import numpy as np
#Reading image 
img = cv2.imread("v.jpeg")
from skimage import io
while True: 
    cv2.imshow("img",img)
    #Converting to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("imagee",img)
    #Detecting edges of the input image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    cv2.imshow("edges",edges)
    #Cartoonifying the image
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
	cv2.imshow("Cartoon",cartoon)
    cv2.waitKey(1)