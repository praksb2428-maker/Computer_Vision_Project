import cv2 as cv
import sys

img = cv.imread('ch2/girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')


# 이미지 창에서 마우스 이벤트가 발생할 때 실행되는 콜백 함수
def draw(event, x, y, flags, param):

    # 마우스 왼쪽 버튼을 클릭한 경우
    if event == cv.EVENT_LBUTTONDOWN:
        # 클릭한 위치부터 가로·세로 200픽셀 크기의 빨간색 사각형 그리기
        cv.rectangle(
            img,        # 도형을 그릴 이미지
            (x, y),
            (x + 200, y + 200),
            (0, 0, 255)
            2)

    # 마우스 오른쪽 버튼을 클릭한 경우
    elif event == cv.EVENT_RBUTTONDOWN:
        # 클릭한 위치를 중심으로 파란색 원 그리기
        cv.circle(
            img,
            (x, y),
            50,
            (255, 0, 0),
            2)

    # 도형이 추가된 이미지를 창에 다시 표시
    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
