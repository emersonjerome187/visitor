from bezmouse import *
import pyautogui
import time
import random
import importlib.machinery
import requests
import json
from os import path
import os
import re
import pyperclip



visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()

firstname = os.getenv('FIRSTNAME')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
dbid = os.getenv('DBID')

def cointiply():

	if path.exists('../init.txt'):
		with open('../init.txt', 'r') as infile:
			init = json.load(infile)

	os.environ['XDG_SESSION_TYPE'] = "vlaue"

	email_domain = init['email_domain']
	if (dbid%2) == 0:
		email_domain = init['email_domain2']

	login_atmps = 0
	while True:
		visitor_lib.browser_open_url('https://cointiply.com/home')

		time.sleep(random.randint(10000, 12000)/1000)

		visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", -89, 46, 16, 28, True)
		logd = visitor_lib.move_to_area_relative("cointiply/faucet.png", -251, 1, 252, 29, False)
		if logd == 'not found' and login_atmps < 3:
			visitor_lib.browser_open_url('https://cointiply.com/login')
			time.sleep(random.randint(6000, 10000)/1000)
			visitor_lib.move_to_area_relative("cointiply/email.png", 18, 21, 124, 20, True)
			time.sleep(random.randint(1000, 2000)/1000)
			pyautogui.write(username+"@"+email_domain, interval = 0.1)
			pyautogui.press('tab')
			pyautogui.write(password, interval = 0.1)
			pyautogui.scroll(-random.randint(5, 6))
			time.sleep(3)
			visitor_lib.move_to_area_relative("cointiply/ct.png", -117, -1, 242, 26, True)
			time.sleep(random.randint(1000, 2000)/1000)
			visitor_lib.move_to_area_relative("cointiply/ct.png", -135, 61, 104, 29, True)
			time.sleep(random.randint(1000, 2000)/1000)
			lic = visitor_lib.solve_captcha_buster()
			pyautogui.scroll(-random.randint(4, 5))
			time.sleep(random.randint(1000, 2000)/1000)
			visitor_lib.move_to_area_relative("cointiply/login.png", -4, 1, 77, 25, True)
			time.sleep(random.randint(10000, 12000)/1000)
			visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", -89, 46, 16, 28, True)
			logdin = visitor_lib.move_to_area_relative("cointiply/faucet.png", -251, 1, 252, 29, False)
			if logdin == "not found" and lic and init['register_accounts']:
				for x in range(0, 3):
					visitor_lib.browser_open_url(init['ctprefer'])
					time.sleep(random.randint(8000, 9000)/1000)
					visitor_lib.browser_open_url('https://cointiply.com/register')
					time.sleep(random.randint(10000, 12000)/1000)
					visitor_lib.move_to_area_relative("cointiply/fn.png", -24, 8, 113, 17, True)
					pyautogui.write(firstname, interval = 0.1)
					pyautogui.press('tab')
					pyautogui.write(username+"@"+email_domain, interval = 0.1)
					pyautogui.press('tab')
					pyautogui.write(password, interval = 0.1)
					pyautogui.press('tab')
					pyautogui.write(password, interval = 0.1)
					pyautogui.scroll(-random.randint(8, 9))
					time.sleep(3)
					visitor_lib.move_to_area_relative("cointiply/ct.png", -117, -1, 242, 26, True)
					time.sleep(random.randint(1000, 2000)/1000)
					visitor_lib.move_to_area_relative("cointiply/ct.png", -135, 61, 104, 29, True)
					rc = visitor_lib.solve_captcha_buster()
					time.sleep(random.randint(1000, 2000)/1000)
					requests.get(init['supervisor_url']+
									"/email?name="+username+"&email_subject=Action Required: Verify Your Email Address")
					time.sleep(random.randint(1000, 2000)/1000)
					visitor_lib.move_to_area_relative("cointiply/cya.png", -68, 6, 199, 25, True)
					time.sleep(random.randint(10000, 12000)/1000)
					if rc:
						visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", -89, 46, 16, 28, True)
						rlogd = visitor_lib.move_to_area_relative("cointiply/faucet.png", -251, 1, 252, 29, False)
						if rlogd == "success":

							email_text = ""
							for z in range(0, 6):
								resp = requests.get(init['supervisor_url']+
									"/email?name="+username+"&email_subject=Action Required: Verify Your Email Address")
								if resp.status_code == 200:
									message = resp.json()['message']
									if message == "success":
										email_text = resp.json()['data']
										break
								time.sleep(60)

							if email_text != "":
								try:
									confirm = re.search("(?<=(Verify Your Email: ))(http:\/\/email.mg.cointiply.com)(.*?)(?=(\\n))", email_text).group(0)
								except:
									confirm = ""
								print(confirm)
								visitor_lib.browser_open_url(confirm)
								time.sleep(random.randint(10000, 12000)/1000)
							break
			login_atmps += 1
			continue
		else:
	
			login_atmps = 0

			visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", -89, 46, 16, 28, True)
			
			visitor_lib.move_to_area_relative("cointiply/faucet.png", 915, -393, 18, 5, False)
			pyautogui.click()
			pyautogui.click()
			pyautogui.hotkey('ctrl', 'c')
			balance = pyperclip.paste().rstrip()
			requests.get(init['supervisor_url']+"/accdata?name="+username+"&key=ctpbalance&value="+balance+"&get=0")

			visitor_lib.move_to_area_relative("cointiply/faucet.png", -209, 0, 170, 29, True, crt=0.65)

			time.sleep(random.randint(500, 2000)/1000)
			visitor_lib.move_to_area_relative("cointiply/roll.png", -350, -225, 1064, 603, False)
			time.sleep(random.randint(500, 2000)/1000)
			
			visitor_lib.move_to_area_relative("cointiply/roll.png", 13, 7, 267, 22, True)

			time.sleep(random.randint(2000, 4000)/1000)

			visitor_lib.move_to_area_relative("cointiply/capaw.png", -101, 10, 66, 18, True, crt=0.7)

			time.sleep(random.randint(500, 2000)/1000)

			visitor_lib.move_to_area_relative("cointiply/capaw.png", -247, 54, 88, 28, True, crt=0.7)

			time.sleep(random.randint(3000, 4000)/1000)

			visitor_lib.solve_captcha_buster()

			visitor_lib.move_to_area_relative("cointiply/roll_final.png", 4, 4, 277, 24, True)

			time.sleep(random.randint(25000, 30000)/1000)

			success = visitor_lib.move_to_area_relative("cointiply/success.png", -392, 3, 431, 28, False)

			time.sleep((random.randint(1000, 2000)/1000)*60)

			return success




cointiply_settings = {
	'collection_amount_usd': 1,
	'collection_interval_minutes': 60,
	'collection_interval_additional_minutes_max': 4,
	'rest_at_hour_min': 20,
	'rest_at_hour_max': 21,
	'hours_rest_min': 5,
	'hours_rest_max': 6,
	'skip_every_min_collections': 4,
	'skip_every_max_collections': 10,
	'skip_by_min_minutes': 10,
	'skip_by_max_minutes': 20
}

