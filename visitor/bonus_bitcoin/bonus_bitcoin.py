from bezmouse import *
import pyautogui
import time
import random
import pyscreenshot as ImageGrab
import pyperclip
import importlib.machinery

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()

def bonus_bitcoin():
	capt_reps = 0
	reps = 0

	while True:
		visitor_lib.browser_open_url("https://bonusbitcoin.co/faucet")

		visitor_lib.move_to_area_relative("visitor_lib/home.png", -63, 54, 1057, 522, False)

		pyautogui.scroll(random.randint(80, 100))

		visitor_lib.move_to_area_relative("visitor_lib/home.png", -63, 54, 1057, 522, False)

		pyautogui.scroll(-random.randint(17, 20))

		if not visitor_lib.solve_captcha_buster():
			time.sleep(random.randint(10, 20))
			if capt_reps < 3:
				capt_reps += 1
				print(capt_reps)
				continue

		ready = visitor_lib.move_to_area_relative("bonus_bitcoin/claim.png", 4, 8, 230, 31, True)

		if ready == "not found":
			return ready

		time.sleep(6)

		success = visitor_lib.move_to_area_relative("bonus_bitcoin/success.png", 403, 66, 42, 16, False)

		if(success == "not found"):
			if reps < 3:
				reps += 1
				print(reps)
				continue

		time.sleep(random.randint(60*1, 60*2))
		return success




bonus_bitcoin_settings = {
	'collection_amount_usd': 0.0018,
	'collection_interval_minutes': 15,
	'collection_interval_additional_minutes_max': 4,
	'rest_at_hour_min': 8,
	'rest_at_hour_max': 9,
	'hours_rest_min': 4,
	'hours_rest_max': 5,
	'skip_every_min_collections': 4,
	'skip_every_max_collections': 10,
	'skip_by_min_minutes': 10,
	'skip_by_max_minutes': 20
}


