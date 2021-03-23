import cv2 as cv
import numpy as np

window = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(window.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(window.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)
#внутриннее пересечение
#bitwise_and = cv.bitwise_and(circle, rectangle)
#cv.imshow("bitwise_and", bitwise_and)

#внешнее пересечение
#bitwise_or = cv.bitwise_or(rectangle, circle)
#cv.imshow("bitwise", bitwise_or)

#все что за пересечением
#bitwise_xor = cv.bitwise_xor(rectangle, circle)
#cv.imshow("bitwise_xor", bitwise_xor)

#все что не пересекает
bitwise_not = cv.bitwise_not(rectangle, circle)
cv.imshow("bitwise_not", bitwise_not)

cv.waitKey(0)
