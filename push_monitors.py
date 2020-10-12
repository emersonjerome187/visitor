from uptimerobot.uptimerobot import UptimeRobot
import json
import requests
import time

with open('accounts.json', 'r') as infile:
	accs = json.load(infile)

# up = UptimeRobot('')
num=0
for x in accs:
# 	up.addMonitor(x[0], "https://" + x[0] + '.herokuapp.com')
	url = "https://calm-bobcat-56.loca.lt"
	requests.get(url+"/status?set=1&name="+x[0]+"&down_status=0&status=up")
	num += 1

# requests.get(url+"/status?set=1&name="+"williselvis556"+"&status="+str(int(time.time())))
