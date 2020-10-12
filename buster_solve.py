from bezmouse import *
import pyautogui
import time
import random


def solve_captcha_buster():
	try:
		imnotarobot = pyautogui.locateOnScreen("img/imnotarobot.png", confidence=0.6)
		assert hasattr(imnotarobot, "left")
	except:
		pass
	if not hasattr(imnotarobot, "left"):
		try:
			imnotarobot=pyautogui.locateOnScreen("img/imnotarobotd.png", confidence=0.6)
			assert hasattr(imnotarobot, "left")
		except:
			pass
	try:
		assert hasattr(imnotarobot, "left")
	except:
		return 0
	move_to_area(imnotarobot.left, imnotarobot.top, imnotarobot.width, imnotarobot.height, 20, random.randint(4, 12))
	move_to_area(imnotarobot.left, imnotarobot.top, imnotarobot.width, imnotarobot.height, 20, random.randint(4, 12))
	pyautogui.mouseDown()
	time.sleep(random.randint(20, 100)/1000)
	pyautogui.mouseUp()
	time.sleep(3)
	try:
		buster = pyautogui.locateOnScreen("img/buster.png", confidence=0.6)
		assert hasattr(buster, "left")
		move_to_area(buster.left, buster.top, buster.width, buster.height, 20, random.randint(4, 12))
		move_to_area(buster.left, buster.top, buster.width, buster.height, 20, random.randint(4, 12))
		pyautogui.mouseDown()
		time.sleep(random.randint(20, 100)/1000)
		pyautogui.mouseUp()
	except:
		pass
	time.sleep(6)
	try:
		greencheck = pyautogui.locateOnScreen("img/greencheck.png", confidence=0.6)
		assert hasattr(greencheck, "left")
	except:
		pass
	if not hasattr(greencheck, "left"):
		try:
			greencheck=pyautogui.locateOnScreen("img/greenchecko.png", confidence=0.6)
			assert hasattr(greencheck, "left")
		except:
			pass
	try:
		assert hasattr(greencheck, "left")
	except:
		return 0

	return 1


print(solve_captcha_buster())

while(True):
	pass


