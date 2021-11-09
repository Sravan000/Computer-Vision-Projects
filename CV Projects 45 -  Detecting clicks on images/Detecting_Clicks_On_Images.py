# Simple Detect 

# import cv2
# def mousePoints(event,x,y,flags,params):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(x,y)
#
# img = cv2.imread('Resources/cards.jpg')
# cv2.imshow("Original Image ", img)
# cv2.setMouseCallback("Original Image ", mousePoints)
# cv2.waitKey(0)


# WARP PRESPECTIVE IMPLEMANTAION WITH MOUSE CLICKS

import cv2
import numpy as np

circles_val = np.zeros((4,2),np.int)
count = 0

def mousePoints(event,x,y,flags,params):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:

        circles_val[count] = x,y
        count = count + 1
        print(circles_val)



img = cv2.imread('cards.jpg')
while True:


    if count == 4:
        width, height = 250,350
        pts1 = np.float32([circles_val[0],circles_val[1],circles_val[2],circles_val[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("Output Image ", imgOutput)


    for x in range (0,4):
        cv2.circle(img,(circles_val[x][0],circles_val[x][1]),3,(0,255,0),cv2.FILLED)

    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    cv2.waitKey(1)
