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
            img,                    # 도형을 그릴 이미지
            (x, y),                 # 사각형의 왼쪽 위 좌표
            (x + 200, y + 200),     # 사각형의 오른쪽 아래 좌표
            (0, 0, 255),            # 선 색상: 빨간색(BGR 순서)
            2                       # 선의 두께
        )

    # 마우스 오른쪽 버튼을 클릭한 경우
    elif event == cv.EVENT_RBUTTONDOWN:
        # 클릭한 위치를 중심으로 파란색 원 그리기
        cv.circle(
            img,                    # 원을 그릴 이미지
            (x, y),                 # 원의 중심 좌표
            50,                     # 원의 반지름
            (255, 0, 0),            # 선 색상: 파란색(BGR 순서)
            2                       # 선의 두께
        )

    # 도형이 추가된 이미지를 창에 다시 표시
    cv.imshow('Drawing', img)


cv.namedWindow('Drawing')
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)

while True:
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()