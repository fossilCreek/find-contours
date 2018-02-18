# -*- coding: UTF-8 -*-

import numpy as np
import cv2, sys, os, re

supportExtends = ['jpg', 'png', 'bpm']
contoursColors = {"green":(0, 255, 0), "blue":(0, 0, 255), "red":(255, 0, 0)}

def isCorrectFileExtends(str):
	if str == '':
		return False
	else:
		if str in supportExtends:
			return True
		return False

if __name__ == "__main__":
	fileName = input("Please input file's name for analisys in current directory or full path - ")
	fileExtends = input("Please input extends for saving files without '.' : png, jpeg, bmp and so on - ").lower()
	setupColor = input("Please input colors for drawing contours - ").lower()
	isShowImages = input("Do you want show images on screen? ").lower()
	img = cv2.imread(fileName)
	if (img is not None) and (isCorrectFileExtends(fileExtends) ) and (setupColor in contoursColors.keys()) :
		print("\nFile was selected. Processing is starting.\n")

		print("Change colors to gray's shade and grow down sharpness")
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (3, 3), 0)
		cv2.imwrite("gray.{}".format(fileExtends), gray)
		print('Result operation is saved image with name -  gray.{} \n'.format(fileExtends) )

		print("Response figure's edge")
		edged = cv2.Canny(gray, 10, 250)
		print("Result operation is saved image with name - edged.{} \n".format(fileExtends))
		cv2.imwrite("edged.{}".format(fileExtends), edged)

		print("Closed witespace in contours")
		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
		closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
		print("Saving image name is closed.png\n")
		cv2.imwrite("closed.{}".format(fileExtends), closed)

		print("Drawing contours on starting image")
		cnts = cv2.findContours(closed.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]

		image = img.copy()
		for c in cnts:
			cv2.drawContours(image, cnts, -1, (0, 255, 0), 4)
		cv2.imwrite("result.{}".format(fileExtends), image)
		print("Result image name is result.{}\n".format(fileExtends))

		if (isShowImages == 'true')
			cv2.imshow("Starting image", img)
			cv2.imshow("Gray image", gray)
			cv2.imshow("Edge image", edged)
			cv2.imshow("Closed image", closed)
			cv2.imshow("Output image", image)

			print("If you want close all windows press key - 'q' ")
			if (cv2.waitKey(1) & 0xFF == ord('q') ):
				cv2.destroyAllWindows();
	elif (img is None):
		print("Not correct input filename or full path to your file - {}".format(fileName))
	elif (not isCorrectFileExtends(fileExtends)):
		print("Not correct file extends - {}".format(fileExtends))
	elif (not (setupColor in contoursColors.keys()) ):
		print("Not support color to select contours")
	os.system("pause")
