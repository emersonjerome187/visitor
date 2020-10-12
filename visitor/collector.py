from bezmouse import *
import pyautogui
from pynput import keyboard
import time
from datetime import datetime, timedelta
import random
import importlib.machinery
import json
import os
import pyscreenshot as ImageGrab
import Xlib.display

pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ['DISPLAY'])
print('collecting...')

visit_list = [
"cointiply",
#"bonus_bitcoin",
"freebitcoin"
#"satoshilabs",
#"bitearn",
#"faucetclaims",
#"moremoney",
#"bitcoinvigil",
#"cryptoearns",
# "bitcoinker"
]

collector_modules = {}
timeouts = {}
sleep_times = {}
skips = {}
prev_day = 0
ss_count = 0

for i, x in enumerate(visit_list):
	collector_modules[x] = importlib.machinery.SourceFileLoader(x, x+'/'+x+'.py').load_module()

init_mod = importlib.machinery.SourceFileLoader("init", 'init/init.py').load_module()

init = getattr(init_mod, "init")
init()


#get/create list of collector time-until-ready values, account balance list, and log files
try:
	with open('timeouts.txt', 'x') as newfile:
		with open('timeouts.txt', 'w') as outfile:
			data = {}
			for y in visit_list:
				data[y] = str(time.strftime("%b %d %H:%M:%S %Y"))
			json.dump(data, outfile)
except:
	pass

try:
	with open('collections.txt', 'x') as newfile:
		with open('collections.txt', 'w') as outfile:
			data = {}
			for y in visit_list:
				data[y] = [[str(time.strftime("%b %d %H:%M:%S %Y")), "0 |0"]]
			json.dump(data, outfile)
except:
	pass

try:
	with open('log.txt', 'x') as newfile:
		with open('log.txt', 'w') as outfile:
			data = {"log": []}
			json.dump(data, outfile)
except:
	pass

for x in visit_list:
	snmin = int(getattr(collector_modules[x], x +'_settings')['skip_every_min_collections'])
	snmax = int(getattr(collector_modules[x], x +'_settings')['skip_every_max_collections'])

	sbmin = int(getattr(collector_modules[x], x +'_settings')['skip_by_min_minutes'])
	sbmax = int(getattr(collector_modules[x], x +'_settings')['skip_by_max_minutes'])

	skips[x] = [0, random.randint(snmin, snmax), random.randint(sbmin, sbmax)]


running = True
def on_release(key):
	if key == keyboard.Key.esc:
		global running
		running = False
		return False

listener = keyboard.Listener(
    on_release=on_release)
listener.start()

while running:
	day = int(time.strftime('%e'))

	if(prev_day != day):
		prev_day = day
		for x in visit_list:
			smin = getattr(collector_modules[x], x+'_settings')['rest_at_hour_min']
			smax = getattr(collector_modules[x], x+'_settings')['rest_at_hour_max']
			sleep_times[x] = [random.randint(smin, smax-1), random.randint(0, 59)]

	
	#sort ready collectors from highest value to lowest
	with open('timeouts.txt', 'r') as infile:
		timeouts = json.load(infile)

	def ready(item):
		timeout = timeouts[item]
		t1 = datetime.strptime(timeout, "%b %d %H:%M:%S %Y")
		t2 = datetime.strptime(time.strftime("%b %d %H:%M:%S %Y"), "%b %d %H:%M:%S %Y")

		latest = max((t1, t2))
		if latest == t2:
			return True

		return False

	ready_list = filter(ready, visit_list)

	def value_key(x):
		return getattr(collector_modules[x], x+'_settings')['collection_amount_usd']

	ready_list = list(ready_list)

	ready_list.sort(key=value_key, reverse=True)

	if len(ready_list) == 0:
		continue

	collector = ready_list[0]

	#start highest value collector
	hvc = getattr(collector_modules[collector], collector)
	state = hvc()

	#store collection success/failure
	rest = False
	with open('collections.txt', 'r') as outfile:
		collections = json.load(outfile)
		if len(collections[collector]) == 10:
			os.remove(collector + '/screenshots/' + collections[collector][1][0] + '.png')
			del collections[collector][0]

		runs = int(collections[collector][-1][1].split("|",1)[1])
		runs += 1
		if hasattr(getattr(collector_modules[collector], collector +'_settings'), 'max_daily_runs'):
			max_daily_runs = getattr(collector_modules[collector], collector +'_settings')['max_daily_runs']
			if runs == max_daily_runs:
				runs = 0
				rest = True

		collections[collector].append([time.strftime("%b %d %H:%M:%S %Y"), str(state) + " |" + str(runs)])
		im = ImageGrab.grab()
		im.save(collector + '/screenshots/' + collections[collector][-1][0] + '.png')
		try:
			os.remove(collector + '/screenshots/current.png')
		except:
			pass
		


	with open('collections.txt', 'w') as outfile:
		json.dump(collections, outfile)


	#calculate and update time-until-ready value
	with open('timeouts.txt', 'w') as outfile:
		timeout = timeouts[collector]
		begin = datetime.strptime(time.strftime("%b %d ") + str(sleep_times[collector][0]) + ':' + str(sleep_times[collector][1]) + time.strftime(':%S %Y'), "%b %d %H:%M:%S %Y")
		minutes_rest = random.randint(getattr(collector_modules[collector], collector + '_settings')['hours_rest_min'], getattr(collector_modules[collector], collector + '_settings')['hours_rest_max']-1)*60 + random.randint(0,60)
		end = begin + timedelta(minutes=minutes_rest)
		current = datetime.strptime(time.strftime("%b %d %H:%M:%S %Y"), "%b %d %H:%M:%S %Y")

		skip = False
		skips[collector][0] += 1

		if skips[collector][0] == skips[collector][1]:
			snmin = int(getattr(collector_modules[collector], collector +'_settings')['skip_every_min_collections'])
			snmax = int(getattr(collector_modules[collector], collector +'_settings')['skip_every_max_collections'])

			sbmin = int(getattr(collector_modules[collector], collector +'_settings')['skip_by_min_minutes'])
			sbmax = int(getattr(collector_modules[collector], collector +'_settings')['skip_by_max_minutes'])

			skips[collector][0] = 0
			skips[collector][1] = random.randint(snmin, snmax)
			skips[collector][2] = random.randint(sbmin, sbmax)

			skip = True

		if not rest:
			if max((current, begin)) == current and max((current, end)) == end:
				timeouts[collector] = end.strftime("%b %d %H:%M:%S %Y")
			else:
				additional = random.randint(0, getattr(collector_modules[collector], collector +'_settings')['collection_interval_additional_minutes_max'])
				minutes = getattr(collector_modules[collector], collector +'_settings')['collection_interval_minutes']
				if skip:
					minutes += skips[collector][2]
				end = current + timedelta(minutes=minutes+additional)
				timeouts[collector] = end.strftime("%b %d %H:%M:%S %Y")
		else:
			end = current + timedelta(minutes=1440)
			timeouts[collector] = end.strftime("%b %d %H:%M:%S %Y")

		json.dump(timeouts, outfile)

	time.sleep(1)


	log_text = current.strftime("%b %d %H:%M:%S %Y") + " : " + collector + ' : ' + str(state)
	with open('log.txt', 'r') as outfile:
		log = json.load(outfile)
		if len(log["log"]) == 100:
			del log["log"][0]
		log["log"].append(log_text)
		if skip:
			print(log_text + " - skiping next")
		else:
			print(log_text)

	with open('log.txt', 'w') as outfile:
		json.dump(log, outfile)