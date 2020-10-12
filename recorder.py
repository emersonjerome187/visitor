from pynput import keyboard
from pynput import mouse
import sys
import time
import pyperclip
import random
import pyautogui
import textwrap
import os
import Xlib.display

pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])

points = []
xp = 0
yp = 0
top_left = True
exit = False
relative_points_step = 0
relative_points = [0,0]
image = 0
pre_path = "visitor_lib/"
path = ""
ocr_var = 0

pre_path = input("enter resource path: ")

def on_press(key):

	global xp
	global yp
	global points
	global top_left

	global image
	global relative_points
	global relative_points_step
	global path
	global pre_path
	global ocr_var

	if key == keyboard.Key.ctrl:
		#x, y, image, properties
		points.append([xp, yp, "", False])
		top_left = not top_left
		print(str(xp) + ", " + str(yp))
		if(top_left):
			print('')
	if key == keyboard.Key.alt:
		if relative_points_step == 0:
			path = input("search image: ")
			print("searching for image")
			try:
				print(pre_path + path)
				image = pyautogui.locateOnScreen(pre_path + path, confidence=0.6)
				assert hasattr(image, "left")
				if hasattr(image, "left"):
					print("image found")
					relative_points_step += 1
					ocr = input("screenshot y/n: ")
					if ocr == 'y':
						ocr_var = input("varible name: ")
					ocr = 0
			except:
				print("image not found")
				relative_points_step = 0
			


		elif relative_points_step == 1:
			relative_points[0] = [xp - image.left, yp - image.top]
			print(relative_points[0])
			relative_points_step += 1
		elif relative_points_step == 2:
			relative_points[1] = [xp - image.left, yp - image.top]
			print(relative_points[1])
			relative_points_step = 0


			#x, y, image, properties
			points.append([0, 0, pre_path+path, {
				"x": str(relative_points[0][0]),
				"y": str(relative_points[0][1]),
				"width": str(abs(relative_points[1][0] - relative_points[0][0])),
				"height": str(abs(relative_points[1][1] - relative_points[0][1])),
				"ocr_var_name": ocr_var
			}])
			ocr_var = 0
			print('')
			print(points[len(points)-1])
			print('')


		

def on_release(key):
	if key == keyboard.Key.esc:
		# Stop listener
		global exit
		exit = True
		script = ""
		prev_click = []
		first = True
		global points
		if(len(points)%2 != 0):
			points.append([10, 10, "", False])
		for x in points:
			if x[2] == "":
				if first:
					prev_click = x
				else:
					script += "move_to_area(" + str(prev_click[0]) + ", " + str(prev_click[1]) + ", " + str(x[0]-prev_click[0]) + ", " + str(x[1]-prev_click[1]) + ", 20, random.randint(4, 12))\n"
					script += "pyautogui.mouseDown()\ntime.sleep(random.randint(20, 100)/1000)\n" + "pyautogui.mouseUp()\n\n"
				first = not first
			else:
				if x[3]['ocr_var_name'] == 0:
					script +=  'visitor_lib.move_to_area_relative("' + x[2] + '", ' + x[3]['x'] + ', ' + x[3]['y'] + ', ' + x[3]['width'] + ', ' + x[3]['height'] + ', True)\n\n'
				else:
					script +=  x[3]['ocr_var_name'] + ' = visitor_lib.screenshot_relative("' + x[2] + '", ' + x[3]['x'] + ', ' + x[3]['y'] + ', ' + x[3]['width'] + ', ' + x[3]['height'] + ')\n'
		print(script)
		pyperclip.copy(script);
		return False

def on_move(x, y):
	global xp
	global yp
	xp = x
	yp = y

listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

mouse_listener = mouse.Listener(
    on_move=on_move)
mouse_listener.start()

while(not exit):
	time.sleep(1)