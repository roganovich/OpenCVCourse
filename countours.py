import cv2 as cv
import numpy as np

file = 'images/3.jpg'
img = cv.imread(file)

#cv.imshow('Test Image', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#cv.imshow("GRAY", gray)
#canny = cv.Canny(img, 125,125)

ret, tresh = cv.threshold(gray, 125,255, cv.THRESH_BINARY)
#cv.imshow("Tresh",tresh)

# RETR_EXTERNAL - внешние контуры
# RETR_LIST - все контуры
# RETR_TREE -
# CHAIN_APPROX_SIMPLE -
# CHAIN_APPROX_NONE -
countours, hierarchies = cv.findContours(tresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(countours)} countor(s) found!')

# наложить контуры от одного изображения на другое
cv.drawContours(blank, countours, -1, (0,0,255), 1)
cv.imshow("Countours", blank)

cv.waitKey(0)
