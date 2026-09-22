import cv2 as cv 

img=cv.imread('ch4/apples.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) # 컬러 영상에서 흑백으로 전환

# 허프 변환으로 반지름 50~120인 원 검출
apples=cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,200,param1=150,param2=20,minRadius=50,maxRadius=120)

for i in apples[0]: 
    cv.circle(img,(int(i[0]),int(i[1])),int(i[2]),(255,0,0),2) # 검출된 원을 파란색으로 그리고 두깨는 2로 설정

cv.imshow('Apple detection',img)  

cv.waitKey()
cv.destroyAllWindows()