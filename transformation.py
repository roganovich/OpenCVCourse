#открываем изображение
import cv2 as cv
import numpy as np

file = 'images/2.jpg'
img = cv.imread(file)
cv.imshow('Test Image', img)

#Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

#подвинем картинку внутри блока
#translated = translate(img, -20, 20)
#cv.imshow("Translated", translated)

#rotation - вращение
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    # по центру
    if rotPoint is None:
        rotPoin = (width//2, height//2)

    rootMath = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)
    return cv.warpAffine(img, rootMath, dimentions)


#ratated = rotate(img, 45)
#cv.imshow("Ratated", ratated)
#0 - vertical
#1 - horisontal
flip = cv.flip(img, 0)
cv.imshow("flip", flip)

cv.waitKey(0)
