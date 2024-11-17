import cv2 as cv


img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img)


def rescaleFrame(frame, scale=0.2):
    
    width = int(frame.shape[1] * scale)   #frame.shape[1] -> width
    height = int(frame.shape[0] * scale)   #frame.shape[0] -> height
    dimensions = (width,height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

frame_resized = rescaleFrame(img)
cv.imshow('Image', frame_resized)

capture= cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized= rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()