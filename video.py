#уменьшаем изображение
import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

file = 'video/1.mp4'

capture = cv.VideoCapture('./video/1.mp4')
while True:
    isTrue, frame = capture.read()
    rescale_frame = rescaleFrame(frame, 0.2)
    cv.imshow('Video', rescale_frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
