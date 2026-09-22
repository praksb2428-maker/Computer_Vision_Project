import cv2 as cv
import numpy as np

img=cv.imread('soccer.jpg')	 # 영상 읽기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY) # 컬러영상을 흑백으로 변환
canny=cv.Canny(gray,100,200) # 임계값 100과 200으로 에지 검출

contour,hierarchy=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE) # Canny 영상에서 윤곽선 검출

lcontour=[]   
for i in range(len(contour)):
    if contour[i].shape[0]>200:	# 길이가 100보다 크면
        lcontour.append(contour[i])
    
cv.drawContours(img,lcontour,-1,(0,255,0),3) # 모든 윤관석을 초록색으로 두깨는 3으로 그림
             
cv.imshow('Original with contours',img)    
cv.imshow('Canny',canny)    

cv.waitKey()
cv.destroyAllWindows()