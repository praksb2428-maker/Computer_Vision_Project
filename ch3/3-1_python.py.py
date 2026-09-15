import cv2 as cv
import sys

img=cv.imread('ch3/soccer.jpg')

if img is None:
    sys.exit("Could not read the image.")

cv.imshow('Title', img)
cv.imshow('Red channel', img[0:img.shape[0]//2,0:img.shape[1]//2,2])
cv.imshow('Green channel', img[:img.shape[0]//2,0:img.shape[1]//2,1])
cv.imshow('Blue channel', img[:img.shape[0]//2,0:img.shape[1]//2,0])

cv.imshow('R channel', img[:,:,2])
cv.imshow('G channel', img[:,:,1])
cv.imshow('B channel', img[:,:,0])

cv.waitKey()
cv.destroyAllWindows()