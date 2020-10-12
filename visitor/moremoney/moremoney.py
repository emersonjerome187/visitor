from bezmouse import *
import pyautogui
import time
import random
import importlib.machinery

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()


def moremoney():

	captcha_reps = 0

	while True:
		visitor_lib.browser_open_url('https://moremoney.io/?page=faucet')

		time.sleep(random.randint(6000, 10000)/1000)

		visitor_lib.move_to_area_relative("moremoney/logo.png", 57, 116, 754, 241, False)

		pyautogui.scroll(-random.randint(80, 100))
		pyautogui.scroll(random.randint(4, 6))

		time.sleep(random.randint(2000, 3000)/1000)

		if not visitor_lib.solve_captcha_buster() and captcha_reps < 3:
			captcha_reps += 1
			time.sleep(random.randint(10, 20))
			continue

		time.sleep(random.randint(4000, 6000)/1000)

		visitor_lib.move_to_area_relative("moremoney/roll.png", -116, 5, 376, 21, True)

		time.sleep(random.randint(3000, 4000)/1000)

		success = visitor_lib.move_to_area_relative("moremoney/success.png", 1, 1, 47, 47, False)

		time.sleep((random.randint(1000, 2500)/1000)*60)

		return success



moremoney_settings = {
	'collection_amount_usd': 0.0025,
	'collection_interval_minutes': 60,
	'collection_interval_additional_minutes_max': 5,
	'rest_at_hour_min': 1,
	'rest_at_hour_max': 3,
	'hours_rest_min': 4,
	'hours_rest_max': 5,
	'skip_every_min_collections': 10,
	'skip_every_max_collections': 15,
	'skip_by_min_minutes': 10,
	'skip_by_max_minutes': 20
}

