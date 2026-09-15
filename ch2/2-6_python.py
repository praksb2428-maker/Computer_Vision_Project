import cv2 as cv
import sys

img = cv.imread('ch2/girl_laughing.jpg')

if img is None:
    sys.exit("Could not read the image.")
# 네모 박스
cv.rectangle(img, (830, 30), (1000, 200), (0, 0, 255), 2)
# 글자
cv.putText(img, 'blue', (830, 24), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv.imshow('Draw', img)
cv.waitKey()
cv.destroyAllWindows()
