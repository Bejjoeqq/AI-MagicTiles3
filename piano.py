from PIL import ImageGrab, ImageOps
import numpy as np
from pynput.keyboard import Controller
import time,cv2

key = Controller()
y1=650
y2=655
box = ((670,y1,680,y2),(810,y1,820,y2),(950,y1,960,y2),(1090,y1,1100,y2))

def img():
	image = []
	for x in box:
		image.append(ImageGrab.grab(x))

	# grayImage = []
	# for x in image:
	# 	grayImage.append(ImageOps.autocontrast(x))

	arr = []
	for x in image:
		arr.append(np.array(x))

	for x in arr:
		print(x.sum(),end="   ")
	print("")
	return arr
def main():
	while True:
		box = img()
		if box[0].sum()<10000:
			key.press("d")
			# time.sleep(0.1)
			key.release("d")
			print("d")
		if box[1].sum()<10000:
			key.press("f")
			# time.sleep(0.1)
			key.release("f")
			print("f")
		if box[2].sum()<10000:
			key.press("j")
			# time.sleep(0.1)
			key.release("j")
			print("j")
		if box[3].sum()<10000:
			key.press("k")
			# time.sleep(0.1)
			key.release("k")
			print("k")
if __name__ == '__main__':
	main()