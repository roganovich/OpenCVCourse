import cv2 as cv
import numpy as np

#ValueError: could not broadcast input array from shape (3,) into shape (300,300,1)
window = np.zeros((300,300, 3), dtype='uint8')
#cv.imshow('New Window', window)

#green background
window[10:100, 90:150] = 0,255,0
#cv.imshow('New Window Green', window)

cv.rectangle(window, (window.shape[1]//2,window.shape[0]//2), (290,290), (0,0,255), thickness=2)
#cv.imshow('New Window Rectangle', window)

cv.circle(window, (window.shape[1]//2,window.shape[0]//2), 40, (0,2,100), thickness=-1)
#cv.imshow('New Window Circle', window)

cv.line(window, (50,50), (window.shape[1]//2,window.shape[0]//2),  (0,2,100), thickness=3)
#cv.imshow('New Window Circle', window)

cv.line(window, (150,50), (window.shape[1]//2,window.shape[0]//2),  (0,2,100), thickness=3)
#cv.imshow('New Window Circle', window)

cv.putText(window, "Hello Roman", (10,150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow('Text', window)

cv.waitKey(0)