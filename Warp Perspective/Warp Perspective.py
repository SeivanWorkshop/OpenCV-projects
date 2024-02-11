# C:/Users/Seivan's Workshop/Desktop/text1.jpg



import cv2 as cv
import numpy as np


img = cv.imread("C:/Users/Seivan's Workshop/Desktop/text1.jpg")

width = 640
height = 480

pts1 = np.float32([ [88,221], [407,222], [80,371], [424,374] ])

pts2 = np.float32([ [0,0], [width,0], [0,height], [width,height] ])

matrix = cv.getPerspectiveTransform(pts1, pts2)

out_img = cv.warpPerspective(img, matrix, (width,height))



cv.imshow("original_img",img)
cv.imshow("warpped_img", out_img)
cv.waitKey(0)


