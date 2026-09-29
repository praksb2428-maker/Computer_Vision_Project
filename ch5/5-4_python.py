import cv2 as cv
import numpy as np


img1=cv.imread('C:\\Users\\Administer\\Desktop\\computer-vision-practice\\ch5\\child.png') # 교통 표지판을 모델 영상으로 사용
gray1=cv.cvtColor(img1,cv.COLOR_BGR2GRAY)
img2=cv.imread('C:\\Users\\Administer\\Desktop\\computer-vision-practice\\ch5\\road.jpg')			     # 장면 영상
gray2=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

mask1=np.zeros(gray1.shape,dtype=np.uint8)
cv.rectangle(mask1,(3,3),(236,42),255,-1)       # 어린이 보호 구역 문구
cv.rectangle(mask1,(5,72),(66,141),255,-1)      # 파란색 삼각형
cv.rectangle(mask1,(62,70),(122,137),255,-1)    # 30 표지

sift=cv.SIFT_create()
kp1,des1=sift.detectAndCompute(gray1,mask1)
kp2,des2=sift.detectAndCompute(gray2,None)

flann_matcher=cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
knn_match=flann_matcher.knnMatch(des1,des2,2)	# 최근접 2개

T=0.85
good_match=[]
for nearest1,nearest2 in knn_match:
    if (nearest1.distance/nearest2.distance)<T:
        good_match.append(nearest1)

points2=np.float32([kp2[gm.trainIdx].pt for gm in good_match])

h1,w1=img1.shape[0],img1.shape[1] 		# 첫 번째 영상의 크기
h2,w2=img2.shape[0],img2.shape[1] 		# 두 번째 영상의 크기

near=np.abs(points2[:,None,:]-points2[None,:,:])
near=(near[:,:,0]<35)&(near[:,:,1]<70)           # 가까이 모인 특징점 선택
selected=np.where(near[np.argmax(np.sum(near,axis=1))])[0]
good_match=[good_match[i] for i in selected]
points2=points2[selected]

x,y,w,h=cv.boundingRect(points2)
cv.rectangle(img2,(max(x-20,0),max(y-5,0)),(min(x+w+20,w2-1),min(y+h+25,h2-1)),(0,255,0),4)

img_match=np.empty((max(h1,h2),w1+w2,3),dtype=np.uint8)
cv.drawMatches(img1,kp1,img2,kp2,good_match,img_match,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
   
cv.imshow('Matches and Sign',img_match)

k=cv.waitKey()
cv.destroyAllWindows()
