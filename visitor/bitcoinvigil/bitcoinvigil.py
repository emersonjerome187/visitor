from bezmouse import *
import pyautogui
import time
import random
import importlib.machinery

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()


def bitcoinvigil():

	captcha_reps = 0

	while True:
		visitor_lib.browser_open_url('https://www.bitcoinvigil.com/faucet.php')

		time.sleep(random.randint(6000, 10000)/1000)

		visitor_lib.move_to_area_relative("bitcoinvigil/claim.png", -241, 3, 656, 32, True)
		time.sleep(random.randint(2000, 3000)/1000)

		if not visitor_lib.solve_captcha_buster() and captcha_reps < 3:
			captcha_reps += 1
			time.sleep(random.randint(10, 20))
			continue

		time.sleep(random.randint(4000, 6000)/1000)

		visitor_lib.move_to_area_relative("bitcoinvigil/claim2.png", -324, 3, 821, 34, True)

		time.sleep(random.randint(7000, 8000)/1000)

		success = visitor_lib.move_to_area_relative("bitcoinvigil/success.png", -66, 5, 56, 25, False)

		time.sleep((random.randint(200, 1000)/1000)*60)

		return success



bitcoinvigil_settings = {
	'collection_amount_usd': 0.001,
	'collection_interval_minutes': 60,
	'collection_interval_additional_minutes_max': 2,
	'rest_at_hour_min': 4,
	'rest_at_hour_max': 5,
	'hours_rest_min': 2,
	'hours_rest_max': 3,
	'skip_every_min_collections': 15,
	'skip_every_max_collections': 20,
	'skip_by_min_minutes': 10,
	'skip_by_max_minutes': 20
}

