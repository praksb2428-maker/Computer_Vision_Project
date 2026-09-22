import cv2 as cv

img=cv.imread('ch4/soccer.jpg')	# 영상 읽기

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

canny1=cv.Canny(gray,50,150)	# Tlow=50, Thigh=150으로 설정
canny2=cv.Canny(gray,100,200)	# Tlow=100, Thigh=200으로 설정

cv.imshow('Original',gray) # 흑백 원본 영상 출력
cv.imshow('Canny1',canny1) # 임계값으로 출력한 에지 영상 출력
cv.imshow('Canny2',canny2)

cv.waitKey()
cv.destroyAllWindows()