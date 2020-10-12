from bezmouse import *
import pyautogui
import time
import random
import importlib.machinery

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()


def bitcoinker():

	captcha_reps = 0

	while True:
		visitor_lib.browser_open_url('https://bitcoinker.com/')

		time.sleep(random.randint(8000, 10000)/1000)

		visitor_lib.move_to_area_relative("visitor_lib/home.png", -63, 54, 1057, 522, True)

		time.sleep(1)

		pyautogui.scroll(random.randint(80, 100))
		pyautogui.scroll(-random.randint(17, 22))

		time.sleep(random.randint(5000, 6000)/1000)

		if not visitor_lib.solve_captcha_buster() and captcha_reps < 3:
			captcha_reps += 1
			time.sleep(random.randint(10, 20))
			continue

		time.sleep(random.randint(3000, 4000)/1000)

		pyautogui.scroll(-random.randint(50, 60))

		pyautogui.scroll(random.randint(7, 11))

		time.sleep(random.randint(1000, 2000)/1000)

		visitor_lib.move_to_area_relative("bitcoinker/claim.png", 11, 16, 101, 25, True)

		time.sleep(random.randint(8000, 10000)/1000)

		pyautogui.scroll(random.randint(80, 100))
		pyautogui.scroll(-random.randint(17, 22))

		time.sleep(random.randint(1000, 2000)/1000)

		success = visitor_lib.move_to_area_relative("bitcoinker/success.png", 46, 66, 264, 55, False)

		time.sleep((random.randint(200, 1000)/1000)*60)

		return success



bitcoinker_settings = {
	'collection_amount_usd': 0.0011,
	'collection_interval_minutes': 6,
	'collection_interval_additional_minutes_max': 2,
	'rest_at_hour_min': 10,
	'rest_at_hour_max': 12,
	'hours_rest_min': 4,
	'hours_rest_max': 6,
	'skip_every_min_collections': 9,
	'skip_every_max_collections': 17,
	'skip_by_min_minutes': 4,
	'skip_by_max_minutes': 10,
	'max_daily_runs': 120
}

