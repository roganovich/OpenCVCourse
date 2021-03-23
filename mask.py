import cv2 as cv
import numpy as np

file = 'images/1.jpg'
img = cv.imread(file)
cv.imshow('Test Image', img)

#ValueError: could not broadcast input array from shape (3,) into shape (300,300,1)
window = np.zeros(img.shape[:2], dtype='uint8')

#mask = cv.circle(window, (420,100), 50, 255, thickness=-1)
mask = cv.rectangle(window, (200,200), (300,300),  255, thickness=-1)
cv.imshow('mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

cv.waitKey(0)