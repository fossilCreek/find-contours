# -*- coding: UTF-8 -*-

import numpy as np
import cv2
import sys
import os

if __name__ == "__main__":
	#Please input name file for analisys in current directory or full path
	fileName = input("Введите имя файла для анализа в текущей директори скрипта или полный путь к файлу - ")
	img = cv2.imread(fileName)
	fileExtends = input("")
	if img is not None:
		print("Файл задан. Начинаем обработку")
		cv2.imshow("Start image", img)

		print("Меняем цвет на оттенки серого и уменьшаем резкость")
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (3, 3), 0)
		cv2.imwrite("gray.png", gray)
		print("Saving images - gray.png")
		cv2.imshow("Gray image", gray)

		print("Распознаем края изображения")
		edged = cv2.Canny(gray, 10, 250)
		print("Сохраням изображение - edged.png")
		cv2.imwrite("edged.png", edged)
		cv2.imshow("Edge image", edged)

		# создайте и примените закрытие
		print("Применяем закрытие пробелов в контуре")
		kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
		closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

		print("Сохраням изображение - closed.png")
		cv2.imwrite("closed.png", closed)
		cv2.imshow("Closed image", closed)

		cnts = cv2.findContours(closed.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[1]

		image = img.copy()

		for c in cnts:
			cv2.drawContours(image, cnts, -1, (0, 255, 0), 4)
		cv2.imwrite("output.png", image)
		print("Результат работы - output.png")
		cv2.imshow("Output image", image)

		cv2.waitKey(0);
		cv2.destroyAllWindows();
	else:
		print("Не верно задан путь или имя файла")

	os.system("pause")
