from bezmouse import *
import pyautogui
import time
from os import path
import random
import importlib.machinery
import json
import requests
import re


username = os.getenv('USERNAME')
dbid = os.getenv('DBID')

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()

def init():

	time.sleep(random.randint(25000, 26000)/1000)
	visitor_lib.move_to_area_relative("visitor_lib/mp.png", 41, 51, 17, 16, True, crt=0.65)
	time.sleep(random.randint(2000, 3000)/1000)

	#install buster addon
	visitor_lib.browser_open_url('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl')
	time.sleep(random.randint(15000, 16000)/1000)
	visitor_lib.move_to_area_relative("init/atc.png", 23, 18, 118, 24, True)
	time.sleep(random.randint(12000, 13000)/1000)
	visitor_lib.move_to_area_relative("init/cancel.png", 105, 15, 114, 18, True, crt=0.8)
	time.sleep(random.randint(10000, 11000)/1000)


	if path.exists('../init.txt'):
		with open('../init.txt', 'r') as infile:
			init = json.load(infile)

	if path.exists('../ip.txt'):
		with open('../ip.txt', 'r') as infile:
			ip = infile.read()

	tries = 3
	attempted = []

	try:
		resp = requests.get(init['supervisor_url']+"/accdata?name="+username+"&get=0&key=ip&value="+ip)
		resp = requests.get(init['supervisor_url']+"/status?set=1&name="+username+"&down_status=0&status=up")
	except:
		pass
	
	email_domain = init['email_domain']
	if (dbid%2) == 0:	
		email_domain = init['email_domain2']

	if init['reproduce']:
		while True:

			resp = requests.get(init['supervisor_url']+"/account?name="+username)
			if resp.status_code != 200:
				break
			
			accounts = resp.json()

			for x in accounts['data']:
				resp = requests.get("https://"+ x[0] + ".herokuapp.com/ip.txt")
				if resp.status_code == 200:
					attempted.append(x)

			acct = []
			for x in accounts['data']:
				atmptd = False
				for y in attempted:
					if x[0] == y[0]:
						atmptd = True
				if not atmptd:
					acct = x
					attempted.append(x)
					break

			if len(acct) == 0:
				print("all account created")
				break

			fn = acct[2]
			ln = acct[3]
			un = acct[0]
			pw = acct[1]
			em = acct[0]+"@"+email_domain

			#heroku
			for x in range(0, tries):
				visitor_lib.browser_open_url('https://signup.heroku.com/')
				time.sleep(random.randint(8000, 10000)/1000)
				visitor_lib.move_to_area_relative("init/fracc.png", 434, 27, 278, 19, True)
				pyautogui.write(fn, interval = 0.1)
				pyautogui.press('tab')
				pyautogui.write(ln, interval = 0.1)
				pyautogui.press('tab')
				pyautogui.write(em, interval = 0.1)
				pyautogui.scroll(-10)
				time.sleep(random.randint(4000, 5000)/1000)
				visitor_lib.move_to_area_relative("init/dn.png", 428, -36, 280, 35, True)
				pyautogui.press('down')
				pyautogui.press('down')
				pyautogui.press('enter')
				time.sleep(random.randint(1000, 2000)/1000)
				visitor_lib.move_to_area_relative("init/dn.png", 429, 133, 286, 32, True)
				pyautogui.press('down')
				pyautogui.press('down')
				pyautogui.press('down')
				pyautogui.press('enter')
				time.sleep(random.randint(1000, 2000)/1000)
				cpt = visitor_lib.solve_captcha_buster()
				time.sleep(random.randint(1000, 2000)/1000)
				if cpt:
					resp = requests.get(init['supervisor_url']+
						"/email?name="+un+"&email_subject=Confirm your account on Heroku")
					time.sleep(random.randint(6000, 7000)/1000)
					visitor_lib.move_to_area_relative("init/cfa.png", 16, 17, 286, 34, True)
					time.sleep(random.randint(8000, 10000)/1000)

					email_text = ""
					for z in range(0, 6):
						resp = requests.get(init['supervisor_url']+
							"/email?name="+un+"&email_subject=Confirm your account on Heroku")
						if resp.status_code == 200:
							message = resp.json()['message']
							if message == "success":
								email_text = resp.json()['data']
								break
						time.sleep(60)

					if email_text != "":

						# code = re.search("(?<=(>https:\/\/id.heroku.com\/account\/accept\/))(.*?)(?=<)", email_text)
						try:
							confirm = re.search("(https:\/\/id.heroku.com\/account\/accept\/)(.*?)(?=(\\n))", email_text).group(0)
						except:
							confirm = ""

						visitor_lib.browser_open_url(confirm)
						time.sleep(random.randint(16000, 18000)/1000)
						visitor_lib.move_to_area_relative("init/sp.png", -48, 210, 96, 21, True)
						pyautogui.write(pw, interval = 0.1)
						pyautogui.press('tab')
						pyautogui.write(pw, interval = 0.1)
						pyautogui.scroll(-4)
						time.sleep(random.randint(3000, 4000)/1000)
						visitor_lib.move_to_area_relative("init/spli.png", 25, 37, 374, 30, True)
						time.sleep(random.randint(8000, 9000)/1000)
						visitor_lib.move_to_area_relative("init/proceed.png", 33, 224, 237, 27, True)
						time.sleep(random.randint(35000, 36000)/1000)
						visitor_lib.move_to_area_relative("visitor_lib/home_chrome.png", -8, 92, 205, 152, False)
						pyautogui.scroll(-20)
						move_to_area(504, 642, 36, 10, 20, random.randint(4, 12))
						pyautogui.mouseDown()
						time.sleep(random.randint(20, 100)/1000)
						pyautogui.mouseUp()
						move_to_area(504, 642, 36, 10, 20, random.randint(4, 12))
						pyautogui.mouseDown()
						time.sleep(random.randint(20, 100)/1000)
						pyautogui.mouseUp()
						time.sleep(random.randint(15000, 16000)/1000)
						hs = visitor_lib.move_to_area_relative("init/hm.png", -207, 11, 102, 24, False)
						if hs == "success":
							visitor_lib.browser_open_url(init['deploy_url'])
							time.sleep(random.randint(8000, 9000)/1000)
							visitor_lib.move_to_area_relative("init/gl.png", 9, 155, 104, 17, True)
							time.sleep(random.randint(1000, 2000)/1000)
							pyautogui.write(un, interval = 0.1)
							pyautogui.press('tab')
							pyautogui.press('tab')
							pyautogui.write(fn, interval = 0.1)
							pyautogui.press('tab')
							pyautogui.write(ln, interval = 0.1)
							pyautogui.press('tab')
							pyautogui.write(pw, interval = 0.1)
							pyautogui.press('tab')
							pyautogui.press('tab')
							pyautogui.press('tab')
							pyautogui.write(un, interval = 0.1)
							pyautogui.press('tab')
							pyautogui.scroll(-8)
							time.sleep(random.randint(3000, 4000)/1000)
							done = visitor_lib.move_to_area_relative("init/da.png", 10, 16, 90, 22, True)
							if done == 'success':
								if x == 1: ac1 = 1
								if x == 2: ac2 = 1
							break
						else:
							visitor_lib.browser_open_url('https://id.heroku.com/login')
							time.sleep(random.randint(20000, 21000)/1000)
							pyautogui.write(em, interval = 0.1)
							pyautogui.press('tab')
							pyautogui.write(pw, interval = 0.1)
							pyautogui.press('tab')
							pyautogui.press('enter')
							time.sleep(random.randint(20000, 21000)/1000)
							hs = visitor_lib.move_to_area_relative("init/hm.png", -207, 11, 102, 24, False)
							if hs == "success":
								visitor_lib.browser_open_url(init['deploy_url'])
								time.sleep(random.randint(8000, 9000)/1000)
								visitor_lib.move_to_area_relative("init/gl.png", 9, 155, 104, 17, True)
								time.sleep(random.randint(1000, 2000)/1000)
								pyautogui.write(un, interval = 0.1)
								pyautogui.press('tab')
								pyautogui.press('tab')
								pyautogui.write(fn, interval = 0.1)
								pyautogui.press('tab')
								pyautogui.write(ln, interval = 0.1)
								pyautogui.press('tab')
								pyautogui.write(pw, interval = 0.1)
								pyautogui.press('tab')
								pyautogui.press('tab')
								pyautogui.press('tab')
								pyautogui.write(un, interval = 0.1)
								pyautogui.press('tab')
								pyautogui.scroll(-8)
								time.sleep(random.randint(3000, 4000)/1000)
								done = visitor_lib.move_to_area_relative("init/da.png", 10, 16, 90, 22, True)
								if done == 'success':
									if x == 1: ac1 = 1
									if x == 2: ac2 = 1
								break
