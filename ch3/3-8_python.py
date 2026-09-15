import cv2 as cv

img = cv.imread("ch3/rose.png")
start = None


def mouse(event, x, y, flags, param):
    global start

    if event == cv.EVENT_LBUTTONDOWN:
        start = (x, y)

    elif event == cv.EVENT_LBUTTONUP:
        x1, x2 = sorted([start[0], x])
        y1, y2 = sorted([start[1], y])

        patch = img[y1:y2, x1:x2]

        result = img.copy()
        cv.rectangle(result, (x1, y1), (x2, y2), (255, 0, 0), 3)
        cv.imshow("Original", result)

        methods = [
            ("Resize nearest", cv.INTER_NEAREST),
            ("Resize bilinear", cv.INTER_LINEAR),
            ("Resize bicubic", cv.INTER_CUBIC)
        ]

        for name, method in methods:
            resized = cv.resize(patch, None, fx=5, fy=5,
                                interpolation=method)
            cv.imshow(name, resized)


cv.imshow("Original", img)
cv.setMouseCallback("Original", mouse)

cv.waitKey()
cv.destroyAllWindows()