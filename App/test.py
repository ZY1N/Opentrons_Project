import cv2
import numpy as np

def drawBasicGrid(img, pxstep, midX, midY):
    x = pxstep
    y = pxstep
    #Draw all x lines
    while x < img.shape[1]:
        cv2.line(img, (x, 0), (x, img.shape[0]), color=(0, 0, 0), thickness=2)
        x += pxstep

    while y < img.shape[0]:
        cv2.line(img, (0, y), (img.shape[1], y), color=(0, 0, 0),thickness=2)
        y += pxstep


def betacameraphotos():

	img1 = cv2.imread("opencv_frame_0.png", cv2.IMREAD_GRAYSCALE)
	img2 = cv2.imread("opencv_frame_1.png", cv2.IMREAD_GRAYSCALE)
	img3 = cv2.imread("opencv_frame_2.png", cv2.IMREAD_GRAYSCALE)
	#value of pixel goes from 0 black to 255 white, 2 numbers are required
	#first one is below 200 is white, and 255 is black 
	_, threshold1 = cv2.threshold(img1, 120, 255, cv2.THRESH_BINARY) 


	_, threshold2 = cv2.threshold(img2, 120, 255, cv2.THRESH_BINARY)

	_, threshold3 = cv2.threshold(img3, 120, 255, cv2.THRESH_BINARY)

	drawBasicGrid(threshold1, 30, 300, 300)
	drawBasicGrid(threshold2, 30, 300, 300)
	drawBasicGrid(threshold3, 30, 300, 300)

	cv2.imwrite('petri1.png',threshold1)
	cv2.imwrite('petri2.png',threshold2)
	cv2.imwrite('petri3.png',threshold3)


	#img1 = cv2.imread('petri1.png', cv2.IMREAD_GRAYSCALE)
	#img2 = cv2.imread('petri2.png', cv2.IMREAD_GRAYSCALE)
	#img3 = cv2.imread('petri3.png', cv2.IMREAD_GRAYSCALE)

	#threshold1.savefig('test_changed.png')


	#cv2.imshow("img1", img1)
	#cv2.imshow("img2", img2)
	#cv2.imshow("img3", img3)
	#cv2.imshow("img1", threshold1)
	#cv2.imshow("img2", threshold2)
	#cv2.imshow("img3", threshold3)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
#betacameraphotos()
