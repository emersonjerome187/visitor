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



def screenshot_relative(anchor_path, rel_x, rel_y, width, height, crt=0.65):
	anchor = pyautogui.locateOnScreen(anchor_path, confidence=crt)
	img = ImageGrab.grab()
	try:
		assert(hasattr(anchor, "left"))
		try:
			selection = img.crop((anchor.left+rel_x, anchor.top+rel_y, anchor.left+rel_x+width, anchor.top+rel_y+height))
		except:
			return "crop error"

		return selection
	except:
		return "not found"

def move_to_area_hc(x, y, width, height, seconds):
	hc = HumanClicker()
	hc.move((x+random.randint(0, width), y+random.randint(0, height)), seconds)

def move_to_area_relative(anchor_path, rel_x, rel_y, width, height, click, crt=0.65):
	try:
		anchor = pyautogui.locateOnScreen(anchor_path, confidence=crt)
		assert(hasattr(anchor, "left"))
		reached = False
		while not reached:
			ax = anchor.left + rel_x
			ay = anchor.top + rel_y
			time.sleep(random.randint(50, 500)/1000)
			move_to_area(ax, ay, width, height, 10, random.randint(1, 2))
			time.sleep(random.randint(50, 500)/1000)
			x, y = pyautogui.position()
			if x > ax and x < ax+width and y > ay and y < ay+height:
				reached = True
		if click:
			pyautogui.mouseDown()
			time.sleep(random.randint(20, 100)/1000)
			pyautogui.mouseUp()
		return "success"
	except:
		return "not found"
	 
def browser_open_url(url):
	move_to_area_relative("visitor_lib/home_chrome.png", 9, 11, 15, 15, True)
	time.sleep(2)
	move_to_area_relative("visitor_lib/home_chrome.png", 111, 8, 59, 13, True)
	for x in range(0, 50):
		pyautogui.press('backspace')
	try:
		pyautogui.write(url, interval = 0.01)
		pyautogui.press('enter')
	except:
		pass



def solve_captcha_buster(scroll=0):

	start = True
	ta_reps = 0
	reps = 0
	while True:
		
		if start:
			time.sleep(6)
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
				reached = False
				while not reached:
					ax = imnotarobot.left + 7
					ay = imnotarobot.top + 6
					time.sleep(random.randint(50, 500)/1000)
					move_to_area(ax, ay, 219, 63, 10, random.randint(1, 2))
					time.sleep(random.randint(50, 500)/1000)
					x, y = pyautogui.position()
					if x > ax and x < ax+219 and y > ay and y < ay+63:
						reached = True
				pyautogui.mouseDown()
				time.sleep(random.randint(20, 100)/1000)
				pyautogui.mouseUp()
				time.sleep(4)
				if scroll != 0:
					pyautogui.scroll(scroll)
					time.sleep(2)
			except:
				return 0
			start = False

			time.sleep(5)

		# move_to_area_relative("visitor_lib/buster.png", -5, 0, 30, 26, True)

		move_to_area_relative("visitor_lib/retry.png", 99, 11, 21, 22, True)
		time.sleep(6)

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
			if(reps < 7):
				reps += 1
				ta = move_to_area_relative("visitor_lib/try_again.png", 124, 200, 22, 20, True)
				time.sleep(5)
				if ta == 'success' and ta_reps < 3:
					ta_reps += 1
					start = True
					reps -= 1
				else:
					time.sleep(6)
					move_to_area_relative("visitor_lib/retry.png", 3, 8, 23, 24, True)
				continue
			else:
				return 0
		

		return 1

