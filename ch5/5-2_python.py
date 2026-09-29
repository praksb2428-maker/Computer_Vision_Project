import cv2 as cv

img=cv.imread('C:\\Users\\Administer\\Desktop\\computer-vision-practice\\ch5\\mot_color70.jpg') # 영상 읽기
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

sift=cv.SIFT_create() # SIFT 객체 생성
kp,des=sift.detectAndCompute(gray,None) # 특징점과 기술자 추출

# 검출된 특징점을 영상 위에 표시
gray=cv.drawKeypoints(gray,kp,None,flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('sift', gray)

k=cv.waitKey()
cv.destroyAllWindows()