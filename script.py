# -*- coding: UTF-8 -*-

import numpy as np
import cv2, sys, os, re

supportExtends = ['.jpg', '.png', '.bpm']
contoursColors = {"green":(0, 255, 0), "blue":(0, 0, 255), "red":(255, 0, 0)}

def isCorrectFileExtends(str):
	if str == '':
		return false
	else:
		pass


if __name__ == "__main__":
	fileName = input("Please input file's name for analisys in current directory or full path - ")
	fileExtends = input("Please input extends for saving files: png, jpeg, bmp and so on - ")
	setupColor = input("Please input colors for drawing contours - ").lower()
	img = cv2.imread(fileName)
	if (img is not None) and (isCorrectFileExtends(fileExtends) ) and (setupColor in contoursColors) :
		print("File was selected. Processing is starting.")
		cv2.imshow("Starting image", img)

		print("Change colors to gray's shade and grow down sharpness")
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (3, 3), 0)
		cv2.imwrite("gray."+fileExtends, gray)
		print('Result operation is saved image with name -  gray.{}'.format(fileExtends) )
		cv2.imshow("Gray image", gray)
		# response figure's edge

		print("Распознаем края изображения")
		edged = cv2.Canny(gray, 10, 250)
		print("Result operation is saved image with name - edged.png")
		cv2.imwrite("edged.png", edged)
		cv2.imshow("Edge image", edged)

		# создайте и примените закрытие Using closed witespace in contours
		print("Применяем закрытие пробелов в контуре")
		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
		closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
		print("Saving image name is closed.png")
		cv2.imwrite("closed."+fileExtends, closed)
		cv2.imshow("Closed image", closed)

		print("Drawing contours on starting image")
		cnts = cv2.findContours(closed.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]

		image = img.copy()

		for c in cnts:
			cv2.drawContours(image, cnts, -1, (0, 255, 0), 4)
		cv2.imwrite("output."+fileExtends, image)
		print("Result image name is result.png")
		cv2.imshow("Output image", image)

		cv2.waitKey(0);
		cv2.destroyAllWindows();
	elif (img is None):
		print("Not correct input filename or full path to your file")
	elif (isCorrectFileExtends(fileExtends)):
		print("Not correct file extends - {}".format(fileExtends))

	os.system("pause")
