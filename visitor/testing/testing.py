from bezmouse import *
import pyautogui
import time
import random
import importlib.machinery

visitor_lib = importlib.machinery.SourceFileLoader('visitor_lib', 'visitor_lib/visitor_lib.py').load_module()


def testing():
	visitor_lib.browser_open_url('https://freebitco.in/?op=signup_page')
	time.sleep(random.randint(10000, 12000)/1000)
	visitor_lib.move_to_area_relative("freebitcoin/gotit.png", 14, 18, 108, 23, True, crt=0.7)

	visitor_lib.move_to_area_relative("freebitcoin/signup2.png", 11, 16, 528, 39, True, crt=0.7)








testing_settings = {
	'collection_amount_usd': 0.0022,
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

