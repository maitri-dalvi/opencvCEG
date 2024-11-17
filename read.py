import cv2 as cv

# img = cv.imread('Photos/cat_large.jpg')

# cv.imshow('Cat', img)

capture= cv.videoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

cv.waitKey(0)