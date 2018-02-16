# -*- coding: UTF-8 -*-

import numpy as np
import cv2
import sys
import os

if __name__ == "__main__":
	#Please input name file for analisys in current directory or full path
	fileName = input("Please input file's name for analisys in current directory or full path - ")
	img = cv2.imread(fileName)
	fileExtends = input("Please input extends for saving files - png, jpeg, bmp and so on")
	if img is not None:
		#File was create. Processing is starting.
		print("Файл задан. Начинаем обработку")
		cv2.imshow("Starting image", img)

		#Change colors to gray's shade and grow down sharpness
		print("Меняем цвет на оттенки серого и уменьшаем резкость")
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (3, 3), 0)
		cv2.imwrite("gray."+fileExtends, gray)
		print("Result operation is saved image with name -  gray.png")
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
		print("Result image name is output.png")
		cv2.imshow("Output image", image)

		cv2.waitKey(0);
		cv2.destroyAllWindows();
	else:
		#Not correct input filename or full path to your file
		print("Не верно задан путь или имя файла")

	os.system("pause")
