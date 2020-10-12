import requests
from os import path
import os
import json
import time

if path.exists('init.txt'):
	with open('init.txt', 'r') as infile:
		init = json.load(infile)

username = os.getenv('USERNAME')
url = init['supervisor_url']
while True:
	try:
		resp = requests.get(url+"/status?set=0&name="+username)
		if resp.status_code == 200:

			accounts = resp.json()

			for x in accounts['data']:
				resp = requests.get("https://"+ x[0] + ".herokuapp.com/ip.txt")
				if resp.status_code == 200:
					requests.get(url+"/status?set=1&name="+x[0]+"&status=up&down_status=0")
				else:
					if(x[1] < 2):
						requests.get(url+"/status?set=1&name="+x[0]+"&status=up&down_status="+str(x[1]+1))
					else:
						requests.get(url+"/status?set=1&name="+x[0]+"&status=down&down_status=0")
	except:
		pass
	time.sleep(15*60)

	