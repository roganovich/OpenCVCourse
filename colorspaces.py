#открываем изображение
import cv2 as cv
import matplotlib.pyplot as plt


file = 'images/4.jpg'
img = cv.imread(file)
#cv.imshow('Test Image', img)

#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow("GRAY", gray)

#hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#cv.imshow("hsv", hsv)

#lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
#cv.imshow("hsv", lab)

#cv.waitKey(0)

plt.imshow(img)
plt.show()