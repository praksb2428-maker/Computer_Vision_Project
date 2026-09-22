import cv2 as cv 
import numpy as np

img = cv.imread('ch4/soccer.jpg')  # 영상 읽기
if img is None:  # 이미지가 제대로 로드되지 않은 경우
    raise FileNotFoundError("Image file 'ch4/soccer.jpg' not found. Please check the file path.")

img_show = np.copy(img)  # 붓 칠을 디스플레이할 목적의 영상

mask=np.zeros((img.shape[0],img.shape[1]),np.uint8) 
mask[:,:]=cv.GC_PR_BGD		# 모든 화소를 배경일 것 같음으로 초기화

BrushSiz=9				# 붓의 크기
LColor,RColor=(255,0,0),(0,0,255)	# 파란색(물체)과 빨간색(배경)

def painting(event,x,y,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:   
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)	# 왼쪽 버튼 클릭하면 파란색
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1)
    elif event==cv.EVENT_RBUTTONDOWN: 
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)	# 오른쪽 버튼 클릭하면 빨간색
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_LBUTTON:
        cv.circle(img_show,(x,y),BrushSiz,LColor,-1)# 왼쪽 버튼 클릭하고 이동하면 파란색
        cv.circle(mask,(x,y),BrushSiz,cv.GC_FGD,-1)
    elif event==cv.EVENT_MOUSEMOVE and flags==cv.EVENT_FLAG_RBUTTON:
        cv.circle(img_show,(x,y),BrushSiz,RColor,-1)	# 오른쪽 버튼 클릭하고 이동하면 빨간색
        cv.circle(mask,(x,y),BrushSiz,cv.GC_BGD,-1)

    cv.imshow('Painting',img_show)
    
cv.namedWindow('Painting')
cv.imshow('Painting', img_show)  # 초기 이미지를 먼저 디스플레이
cv.setMouseCallback('Painting',painting)

while(True):				# 붓 칠을 끝내려면 'q' 키를 누름
    if cv.waitKey(1)==ord('q'): 
        break

# 여기부터 GrabCut 적용하는 코드
background=np.zeros((1,65),np.float64)	# 배경 히스토그램 0으로 초기화
foreground=np.zeros((1,65),np.float64)	# 물체 히스토그램 0으로 초기화q

cv.grabCut(img,mask,None,background,foreground,1,cv.GC_INIT_WITH_MASK) # 1의 의미는 GrabCut을 반복하는 횟수입니다.
mask2=np.where((mask==cv.GC_BGD)|(mask==cv.GC_PR_BGD),0,1).astype('uint8')
grab=img*mask2[:,:,np.newaxis]
cv.imshow('Grab cut image',grab)  

cv.waitKey()
cv.destroyAllWindows()


# 1 에서 5로 변경을 하였을 때 빨간 선과 파란선으로 지정한 영역의 분리가 더 잘 되는 것을 확인 할 수 있습니다.