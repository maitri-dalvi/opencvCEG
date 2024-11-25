import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

blank[200:300, 300:400] = 0, 255,0   #200:300, 300:400 --> pixels
cv.imshow("Green", blank)


cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

cv.waitKey(0)