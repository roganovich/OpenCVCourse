import cv2 as cv

file = 'images/1.jpg'
img = cv.imread(file)
cv.imshow('Test Image', img)
cv.waitKey(0)
