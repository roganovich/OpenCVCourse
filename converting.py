import cv2 as cv

file = 'images/1.jpg'
img = cv.imread(file)
cv.imshow('Test Image', img)

#изменяем цветовую палитку изображения
#gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('GRAY Image', gray)

#размытие
#blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
#cv.imshow('blur Image', blur)

#краевой каскад/ инверсия границ
#cany = cv.Canny(img, 125,175)
#cv.imshow('cany Image', cany)

#расширение изображения
#dilated = cv.dilate(cany, (7,7), iterations=1)
#cv.imshow('dilated Image', dilated)

#эрозия
#eroded = cv.erode(cany, (3,3), iterations=1)
#cv.imshow('eroded Image', eroded)

resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resize Image', resize)


crooped = img[50:200, 200:400]
cv.imshow('crooped Image', crooped)



cv.waitKey(0)
