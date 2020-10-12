from bezmouse import *
import pyautogui
import time
import random
import importlib.machinery

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()


def bitearn():

	captcha_reps = 0

	while True:
		visitor_lib.browser_open_url('https://bitearn.io/page/dashboard/')

		time.sleep(random.randint(6000, 10000)/1000)

		if not visitor_lib.solve_captcha_buster() and captcha_reps < 3:
			captcha_reps += 1
			time.sleep(random.randint(10, 20))
			continue

		time.sleep(random.randint(4000, 6000)/1000)

		visitor_lib.move_to_area_relative("bitearn/claim.png", -443, -1, 1103, 45, True)

		time.sleep(random.randint(7000, 8000)/1000)

		success = visitor_lib.move_to_area_relative("bitearn/success.png", 82, 25, 149, 25, False)

		time.sleep((random.randint(200, 1000)/1000)*60)

		return success



bitearn_settings = {
	'collection_amount_usd': 0.001,
	'collection_interval_minutes': 30,
	'collection_interval_additional_minutes_max': 2,
	'rest_at_hour_min': 20,
	'rest_at_hour_max': 21,
	'hours_rest_min': 0,
	'hours_rest_max': 1,
	'skip_every_min_collections': 15,
	'skip_every_max_collections': 20,
	'skip_by_min_minutes': 10,
	'skip_by_max_minutes': 20
}

