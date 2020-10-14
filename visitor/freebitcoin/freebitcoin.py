from bezmouse import *
import pyautogui
import time
import random
import importlib.machinery
import pyotp
import base64
from io import BytesIO
from os import path
import os
import json
import requests
import pyperclip
import re

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
dbid = os.getenv('DBID')

def freebitcoin():

	login_atmps = 0

	if path.exists('../init.txt'):
		with open('../init.txt', 'r') as infile:
			init = json.load(infile)
	try:
		resp = requests.get(init['supervisor_url']+"/accdata?name="+username+"&get=1")
		secret = json.loads(resp.json()['data'])['fbsecret']
		print(secret)
		if secret == None:
			secret = ""
	except:
		secret = ""

	email_domain = init['email_domain']
	if (dbid%2) == 0:	
		email_domain = init['email_domain2']

	os.environ['XDG_SESSION_TYPE'] = "vlaue"

	while True:

		visitor_lib.browser_open_url('https://freebitco.in/')
		time.sleep(random.randint(8000, 10000)/1000)

		logd = visitor_lib.move_to_area_relative("freebitcoin/power.png", 2, 2, 18, 29, False)

		if logd == 'not found' and login_atmps < 3:
			try:
				totp = pyotp.TOTP(secret)
			except:
				pass
			time.sleep(random.randint(3000, 4000)/1000)
			visitor_lib.move_to_area_relative("freebitcoin/nothanks.png", 6, 5, 73, 17, True)
			visitor_lib.move_to_area_relative("freebitcoin/login_page.png", -2, -1, 52, 24, True)
			time.sleep(random.randint(3000, 4000)/1000)
			visitor_lib.move_to_area_relative("freebitcoin/login.png", -217, -204, 301, 20, True)
			time.sleep(random.randint(1000, 2000)/1000)
			pyautogui.write(username+"@"+email_domain, interval = 0.1)
			pyautogui.press('tab')
			pyautogui.write(password, interval = 0.1)
			pyautogui.press('tab')
			try:
				pyautogui.write(totp.now(), interval = 0.1)
			except:
				pass
			time.sleep(random.randint(1000, 2000)/1000)
			visitor_lib.move_to_area_relative("freebitcoin/login.png", -91, 3, 244, 34, True)
			time.sleep(random.randint(10000, 12000)/1000)
			

			logdin = visitor_lib.move_to_area_relative("freebitcoin/power.png", 2, 2, 18, 29, False)
			if logdin == "not found" and init['register_accounts']:
				for x in range(0, 4):
					visitor_lib.browser_open_url('https://freebitco.in/?op=signup_page')
					time.sleep(random.randint(10000, 12000)/1000)

					visitor_lib.move_to_area_relative("freebitcoin/gotit.png", 14, 18, 108, 23, True, crt=0.7)
					visitor_lib.move_to_area_relative("freebitcoin/signup2.png", 13, -357, 118, 22, True, crt=0.7)
					pyautogui.write(username+"@"+email_domain, interval = 0.1)
					pyautogui.press('tab')
					pyautogui.write(password, interval = 0.1)
					pyautogui.press('tab')
					pyautogui.write(init['fbrefer'], interval = 0.1)
					solution = ''
					try:
						captcha = visitor_lib.screenshot_relative("freebitcoin/signup2.png", 131, -128, 237, 80, crt=0.7)
						buffered = BytesIO()
						captcha.save(buffered, format="JPEG")
						img_str = base64.b64encode(buffered.getvalue())
						request = {
							"clientKey": init['captcha_api']+"__recognizingthreshold_70",
							"task": {
								"type": "ImageToTextTask",
								"body": img_str.decode('ascii'),
								"CapMonsterModule": "botdetect"
							}
						};
						resp = requests.post('https://api.capmonster.cloud/createTask', json=request);
						request = {
							"clientKey": init['captcha_api'],
							"taskId": resp.json()['taskId']
						};
						time.sleep(10)
						resp = requests.post('https://api.capmonster.cloud/getTaskResult', json=request);
						solution = resp.json()['solution']['text']
					except:
						pass
					visitor_lib.move_to_area_relative("freebitcoin/gotit.png", 14, 18, 108, 23, True, crt=0.7)
					visitor_lib.move_to_area_relative("freebitcoin/signup2.png", 144, -42, 154, 21, True, crt=0.7)
					pyautogui.write(solution, interval = 0.1)
					time.sleep(1)
					visitor_lib.move_to_area_relative("freebitcoin/signup2.png", 11, 16, 528, 39, True, crt=0.7)
					time.sleep(random.randint(10000, 12000)/1000)
					logdin2 = visitor_lib.move_to_area_relative("freebitcoin/power.png", 2, 2, 18, 29, False)
					if logdin2 == "success":
						break
			
			if logdin == "success":
				visitor_lib.move_to_area_relative("freebitcoin/power.png", -196, 4, 47, 26, False)
				time.sleep(random.randint(1000,2000)/1000)
				visitor_lib.move_to_area_relative("freebitcoin/power.png", -197, 47, 52, 30, True)
				time.sleep(random.randint(2000, 3000)/1000)
				pyautogui.scroll(-2)
				time.sleep(random.randint(2000, 3000)/1000)
				visitor_lib.move_to_area_relative("freebitcoin/rp.png", -73, 55, 7, 9, True)
				pyautogui.click()
				pyautogui.click()
				pyautogui.hotkey('ctrl', 'c')
				rps = int(str(pyperclip.paste().rstrip()).replace(',', ''))
				time.sleep(2)
				# if rps >= 300:
				# 	pyautogui.scroll(-20)
				# 	time.sleep(random.randint(3000,4000)/1000)
				# 	move_to_area(596, 560, 155, 24, 20, random.randint(1, 2))
				# 	pyautogui.mouseDown()
				# 	time.sleep(random.randint(20, 100)/1000)
				# 	pyautogui.mouseUp()
				# 	time.sleep(random.randint(3000,4000)/1000)
				# 	pyautogui.scroll(-20)
				# 	time.sleep(random.randint(3000,4000)/1000)
				# 	move_to_area(830, 233, 76, 35, 20, random.randint(1, 2))
				# 	pyautogui.mouseDown()
				# 	time.sleep(random.randint(20, 100)/1000)
				# 	pyautogui.mouseUp()
				fborlt = random.randint(1,3)
				if rps >= 120:
					visitor_lib.browser_open_url('https://freebitco.in/')
					time.sleep(random.randint(8000, 10000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/power.png", -196, 4, 47, 26, False)
					time.sleep(random.randint(1000,2000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/power.png", -197, 47, 52, 30, True)
					time.sleep(random.randint(3000,4000)/1000)
					pyautogui.scroll(-20)
					time.sleep(random.randint(3000,4000)/1000)
					if False:
						move_to_area(605, 514, 113, 20, 20, random.randint(1, 2))
						pyautogui.mouseDown()
						time.sleep(random.randint(20, 100)/1000)
						pyautogui.mouseUp()
						time.sleep(random.randint(3000,4000)/1000)
						pyautogui.scroll(-20)
						time.sleep(random.randint(3000,4000)/1000)
						move_to_area(840, 333, 56, 15, 20, random.randint(1, 2))
						pyautogui.mouseDown()
						time.sleep(random.randint(20, 100)/1000)
						pyautogui.mouseUp()
					elif rps >= 160:
						move_to_area(615, 469, 104, 15, 20, random.randint(1, 2))
						pyautogui.mouseDown()
						time.sleep(random.randint(20, 100)/1000)
						pyautogui.mouseUp()
						time.sleep(random.randint(3000,4000)/1000)
						pyautogui.scroll(-20)
						time.sleep(random.randint(3000,4000)/1000)
						move_to_area(835, 284, 62, 14, 20, random.randint(1, 2))
						pyautogui.mouseDown()
						time.sleep(random.randint(20, 100)/1000)
						pyautogui.mouseUp()

			login_atmps += 1
			continue

		else:
			login_atmps = 0
			time.sleep(10)

			if secret == "":
				visitor_lib.move_to_area_relative("freebitcoin/gotit.png", 14, 18, 108, 23, True, crt=0.7)
				visitor_lib.move_to_area_relative("freebitcoin/power.png", -196, 4, 47, 26, False)
				time.sleep(random.randint(1000,2000)/1000)
				visitor_lib.move_to_area_relative("freebitcoin/power.png", -195, 138, 53, 29, True)
				time.sleep(3)
				pyautogui.scroll(-20)
				time.sleep(random.randint(1000,2000)/1000)
				visitor_lib.move_to_area_relative("freebitcoin/2fa.png", -46, 6, 337, 27, True, crt=0.8)
				try:
					requests.get(init['supervisor_url']+"/email?name="+username+"&email_subject=Email confirmation to enable 2-factor authentication")
				except:
					pass
				time.sleep(8)
				visitor_lib.move_to_area_relative("freebitcoin/sendem.png", -29, -4, 158, 30, True)
				email_text = ''
				for z in range(0, 6):
					resp = requests.get(init['supervisor_url']+
						"/email?name="+username+"&email_subject=Email confirmation to enable 2-factor authentication")
					if resp.status_code == 200:
						message = resp.json()['message']
						if message == "success":
							email_text = resp.json()['data']
							break
					time.sleep(60)
				if email_text != "":
					try:
						confirm = re.search("(?<=(authentication: <\\r\\n<))(https:\/\/freebitco.in\/\?op=email_verify)(.*?)(?=(>))", email_text).group(0)
					except:
						confirm = ""
					print(confirm)
					visitor_lib.browser_open_url(confirm)
					time.sleep(random.randint(10000, 12000)/1000)
					visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", 657, 243, 12, 11, True, crt=0.65)
					time.sleep(random.randint(2000, 3000)/1000)
					visitor_lib.browser_open_url('https://freebitco.in/')
					time.sleep(random.randint(10000, 12000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/power.png", -196, 4, 47, 26, True)
					visitor_lib.move_to_area_relative("freebitcoin/power.png", -195, 138, 53, 29, True)
					time.sleep(5)
					pyautogui.scroll(-20)
					time.sleep(random.randint(2000,3000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/2fa.png", -46, 6, 337, 27, True, crt=0.8)
					pyautogui.scroll(-20)
					time.sleep(random.randint(2000, 3000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/enable2fa.png", -33, -3, 167, 34, True)
					time.sleep(random.randint(2000, 3000)/1000)
					pyautogui.scroll(-20)
					time.sleep(random.randint(2000, 3000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/enable2fa.png", 43, -97, 111, 11, True)
					pyautogui.click()
					pyautogui.click()
					pyautogui.hotkey('ctrl', 'c')
					time.sleep(3)
					secret = pyperclip.paste().rstrip()
					visitor_lib.move_to_area_relative("freebitcoin/enable2fa.png", -27, -51, 170, 20, True)
					try:
						totp = pyotp.TOTP(secret)
						time.sleep(random.randint(2000, 3000)/1000)
						pyautogui.write(totp.now(), interval = 0.1)
						time.sleep(random.randint(2000, 3000)/1000)
						visitor_lib.move_to_area_relative("freebitcoin/enable2fa.png", -33, -3, 167, 34, True)
					except:
						pass
					requests.get(init['supervisor_url']+"/accdata?name="+username+"&key=fbsecret&value="+secret+"&get=0")
					
					visitor_lib.browser_open_url('https://freebitco.in/')
					time.sleep(random.randint(10000, 12000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/power.png", -196, 4, 47, 26, True)
					visitor_lib.move_to_area_relative("freebitcoin/power.png", -195, 138, 53, 29, True)
					time.sleep(random.randint(3000, 4000)/1000)
					pyautogui.scroll(-15)
					time.sleep(random.randint(2000, 3000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/2fa.png", -7, 140, 301, 30, True, crt=0.8)
					time.sleep(random.randint(2000, 3000)/1000)
					pyautogui.scroll(-2)
					time.sleep(random.randint(2000, 3000)/1000)
					visitor_lib.move_to_area_relative("freebitcoin/2fa.png", -112, 215, 3, 3, True, crt=0.8)
					time.sleep(random.randint(2000, 3000)/1000)
					visitor_lib.browser_open_url('https://freebitco.in/')
					time.sleep(random.randint(8000, 10000)/1000)

			visitor_lib.move_to_area_relative("freebitcoin/nothanks.png", 6, 5, 73, 17, True)
			visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", -8, 92, 205, 152, False)

			visitor_lib.move_to_area_relative("freebitcoin/power.png", -114, 11, 53, 10, True)
			pyautogui.click()
			pyautogui.hotkey('ctrl', 'c')
			balance = pyperclip.paste().rstrip()
			try:
				requests.get(init['supervisor_url']+"/accdata?name="+username+"&key=fbbalance&value="+balance+"&get=0")
			except:
				pass
			pyautogui.scroll(-random.randint(80, 100))

			time.sleep(1)

			visitor_lib.move_to_area_relative("freebitcoin/gotit.png", 14, 18, 108, 23, True, crt=0.7)
			solved = visitor_lib.solve_captcha_buster()
			if os.getenv("FBPASSES") is not None:
				passes = int(os.getenv('FBPASSES'))
			else:
				os.environ["FBPASSES"] = "0"
				passes = 0
			if not solved and passes < 5: 
				visitor_lib.move_to_area_relative("freebitcoin/play_without_capt.png", -6, 3, 226, 36, True)
				time.sleep(3)
				pyautogui.scroll(-random.randint(8, 10))
				os.environ["FBPASSES"] = str(passes+1)

			time.sleep(3)
			visitor_lib.move_to_area_relative("freebitcoin/nothanks.png", 6, 5, 73, 17, True)
			visitor_lib.move_to_area_relative("freebitcoin/gotit.png", 14, 18, 108, 23, True, crt=0.7)
			time.sleep(1)
			move_to_area(648, 696, 52, 18, 20, random.randint(1, 2))
			pyautogui.mouseDown()
			time.sleep(random.randint(20, 100)/1000)
			pyautogui.mouseUp()



			time.sleep(4)

			visitor_lib.move_to_area_relative("freebitcoin/pn.png", 499, -143, 6, 8, True)

			time.sleep(1)
			pyautogui.scroll(-random.randint(80, 100))

			time.sleep(1)

			success = visitor_lib.move_to_area_relative("freebitcoin/success.png", -16, -4, 305, 33, False, crt=0.7)

			time.sleep((random.randint(1000, 2000)/1000)*60)

			return success




freebitcoin_settings = {
	'collection_amount_usd': 2,
	'collection_interval_minutes': 60,
	'collection_interval_additional_minutes_max': 4,
	'rest_at_hour_min': 8,
	'rest_at_hour_max': 9,
	'hours_rest_min': 1,
	'hours_rest_max': 2,
	'skip_every_min_collections': 7,
	'skip_every_max_collections': 10,
	'skip_by_min_minutes': 10,
	'skip_by_max_minutes': 30
}

