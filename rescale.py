#уменьшаем изображение
import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

file = 'images/2.jpg'

img = cv.imread(file)
img2 = rescaleFrame(img, 2.25)

cv.imshow('Rescale Image', img2)
cv.waitKey(0)
