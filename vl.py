from bezmouse import *
# from pyclick import HumanClicker
import pyautogui
import time
import random
# from tesserocr import image_to_text
# try:
#     from PIL import Image
# except ImportError:
#     import Image
import pyscreenshot as ImageGrab



# def ocr_relative(anchor_path, rel_x, rel_y, width, height):
# 	anchor = pyautogui.locateOnScreen(anchor_path, confidence=0.6)
# 	img = ImageGrab.grab()
# 	try:
# 		assert(hasattr(anchor, "left"))
# 		try:
# 			selection = img.crop((anchor.left+rel_x, anchor.top+rel_y, anchor.left+rel_x+width, anchor.top+rel_y+height))
# 		except:
# 			return "crop error"

# 		return image_to_text(selection)
# 	except:
# 		return "not found"

# def move_to_area_hc(x, y, width, height, seconds):
# 	hc = HumanClicker()
# 	hc.move((x+random.randint(0, width), y+random.randint(0, height)), seconds)

def move_to_area_relative(anchor_path, rel_x, rel_y, width, height, click):
	anchor = pyautogui.locateOnScreen(anchor_path, confidence=0.6)
	try:
		assert(hasattr(anchor, "left"))
		time.sleep(random.randint(50, 500)/1000)
		move_to_area(anchor.left + rel_x, anchor.top + rel_y, width, height, 20, random.randint(3, 9))
		time.sleep(random.randint(50, 500)/1000)
		move_to_area(anchor.left + rel_x, anchor.top + rel_y, width, height, 20, random.randint(4, 12))
		time.sleep(random.randint(50, 500)/1000)
		if click:
			pyautogui.mouseDown()
			time.sleep(random.randint(20, 100)/1000)
			pyautogui.mouseUp()
		return "success"
	except:
		return "not found"
	 
def browser_open_url(url):
	move_to_area_relative("visitor_lib/home.png", 5, 3, 20, 19, True)
	time.sleep(2)
	move_to_area_relative("visitor_lib/home.png", 772, 4, 259, 16, True)
	for x in range(0, 50):
		pyautogui.press('backspace')
	pyautogui.write(url, interval = 0.1)
	pyautogui.press('enter')



def solve_captcha_buster():

	reps = 0
	while True:
		imnotarobot = "[]"
		try:
			imnotarobot = pyautogui.locateOnScreen("visitor_lib/imnotarobot.png", confidence=0.6)
			assert hasattr(imnotarobot, "left")
		except:
			pass
		if not hasattr(imnotarobot, "left"):
			try:
				imnotarobot=pyautogui.locateOnScreen("visitor_lib/imnotarobotd.png", confidence=0.6)
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
			buster = pyautogui.locateOnScreen("visitor_lib/buster.png", confidence=0.6)
			assert hasattr(buster, "left")
			move_to_area(buster.left, buster.top, buster.width, buster.height, 20, random.randint(4, 12))
			move_to_area(buster.left, buster.top, buster.width, buster.height, 20, random.randint(4, 12))
			pyautogui.mouseDown()
			time.sleep(random.randint(20, 100)/1000)
			pyautogui.mouseUp()
		except:
			pass
		time.sleep(6)

		ta = move_to_area_relative("visitor_lib/try_again.png", 124, 203, 20, 17, True)
		if ta == 'success' and reps < 3:
			reps += 1
			continue

		try:
			greencheck = pyautogui.locateOnScreen("visitor_lib/greencheck.png", confidence=0.6)
			assert hasattr(greencheck, "left")
		except:
			pass
		if not hasattr(greencheck, "left"):
			try:
				greencheck=pyautogui.locateOnScreen("visitor_lib/greenchecko.png", confidence=0.6)
				assert hasattr(greencheck, "left")
			except:
				pass
		try:
			assert hasattr(greencheck, "left")
		except:
			return 0

		return 1

