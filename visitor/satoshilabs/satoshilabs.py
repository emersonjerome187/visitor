from bezmouse import *
import pyautogui
import time
import random
import importlib.machinery

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()


def satoshilabs():

	captcha_reps = 0
	reps = 0

	while True:

		visitor_lib.browser_open_url('https://satoshilabs.net/faucet.php')

		time.sleep(5)

		sc = visitor_lib.move_to_area_relative("satoshilabs/logo.png", -17, 57, 195, 83, True)

		time.sleep(2)

		if(sc != 'success') and reps < 3:
			reps += 1
			continue

		if not visitor_lib.solve_captcha_buster() and captcha_reps < 3:
			captcha_reps += 1
			time.sleep(random.randint(10, 20))
			continue

		visitor_lib.move_to_area_relative("satoshilabs/submit.png", 4, 4, 141, 33, True)

		time.sleep(4)

		visitor_lib.solve_captcha_buster()

		time.sleep(3)

		visitor_lib.move_to_area_relative("satoshilabs/reward.png", 0, 2, 113, 31, True)

		time.sleep(10)

		success = visitor_lib.move_to_area_relative("satoshilabs/success.png", -134, 4, 123, 31, False)

		time.sleep((random.randint(1000, 2000)/1000)*60)

		return success




satoshilabs_settings = {
	'collection_amount_usd': 0.0005,
	'collection_interval_minutes': 8,
	'collection_interval_additional_minutes_max': 4,
	'rest_at_hour_min': 8,
	'rest_at_hour_max': 9,
	'hours_rest_min': 1,
	'hours_rest_max': 2,
	'skip_every_min_collections': 4,
	'skip_every_max_collections': 8,
	'skip_by_min_minutes': 8,
	'skip_by_max_minutes': 12
}

